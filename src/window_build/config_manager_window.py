"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

 ██╗  ██╗ █████╗ ██████╗ ████████╗ █████╗ ███╗   ██╗██╗ █████╗ 
 ╚██╗██╔╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗████╗  ██║██║██╔══██╗
  ╚███╔╝ ███████║██████╔╝   ██║   ███████║██╔██╗ ██║██║███████║
  ██╔██╗ ██╔══██║██╔══██╗   ██║   ██╔══██║██║╚██╗██║██║██╔══██║
 ██╔╝ ██╗██║  ██║██║  ██║   ██║   ██║  ██║██║ ╚████║██║██║  ██║
 ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝

Edition:
##  14/09/2025 by Tsukini

File Name:
##  config_manager_window.py

File Description:
##  Build of the config manager window items
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
# Import that can't be in the try
from src.const import Error, Window, Color, Text
from sys import exit

# Import that can be checked
try:
    import customtkinter as ctk # Used for the graphics interface / GUI
    from window_build.window_geometry import setup_geometry # Used to setup the default size & position
    from Class.parameters import Parameters # Used to read the parameters
    from Class.popup import Popup # Used to display information
    from pathlib import Path # Used to get the list of the script
    import os # Used to make operation on file
except ImportError as e:
    print(f"Import Error: {e}")
    exit(Error.FATAL_ERROR)

""" Program """
def build(window):
    """
        Build the config manager window items
        :param window: Main window of the app
    """

    # Init the global variable
    parameters = Parameters()

    # Setup the window
    subwindow = ctk.CTkToplevel(window)
    subwindow.title(Text.LANGUAGES[Text.LANGUAGE]["Config Manager"])
    subwindow.iconbitmap(default="data\\img\\MAGIC_icon_v3.ico")
    subwindow.resizable(width=False, height=False)
    setup_geometry(subwindow, Window.CONFIG_WIDTH, Window.CONFIG_HEIGHT)
    subwindow.grab_set()

    # Global frame
    main_frame = ctk.CTkFrame(subwindow)
    main_frame.pack(fill="both", expand=True)

    # Left frame
    config_scroll = ctk.CTkScrollableFrame(main_frame, width=200, label_text=Text.LANGUAGES[Text.LANGUAGE]["Configurations"])
    config_scroll.pack(side="left", fill="y", padx=(5, 2.5), pady=5)

    # PopUp to delete or load config
    def config_option(self, path):
        res = Popup("Question", Text.LANGUAGES[Text.LANGUAGE]["Config Question"].replace("NAME", os.path.basename(path)), ("Cancel", "Load", "Delete")).result
        subwindow.grab_set()
        if res == "Load":
            parameters.get_parameters()
            parameters.lignes = [line for line in parameters.lignes if line.split("=")[0] in ("language", "loading")]
            with open(path, "r", encoding="utf-8") as file:
                for line in file.read().splitlines():
                    parameters.lignes.append(line + "\n")
            parameters.save_parameters()
            setup_actual_config_content()
        elif res == "Delete":
            os.remove(path)
            self.destroy()

    # Setup the button of the different config
    path = "data\\configs"
    for file in Path(path).iterdir():
        if file.is_file():
            name = file.name
            config_name = ctk.CTkButton(config_scroll, text=name)
            config_name.configure(command=lambda self=config_name, full_path=path + "\\" + name: config_option(self, full_path))
            config_name.pack(pady=5, fill="x")

    # Right side of the subwindow
    right_frame = ctk.CTkFrame(main_frame)
    right_frame.pack(side="right", fill="both", expand=True, padx=(2.5, 5), pady=5)

    #Top part of the right side to save the actual config
    top_frame = ctk.CTkFrame(right_frame)
    top_frame.pack(fill="x", padx=5, pady=(10, 0))

    # Textbox for a config saving
    save_config_name = ctk.CTkTextbox(top_frame, width=Window.TEXTBOX_HEIGHT, height=Window.TEXTBOX_HEIGHT)
    save_config_name.pack(fill="x", padx=10, pady=(10, 0))

    # Nettoyage automatique des caractères interdits
    def valid_filename(event=None):
        text = save_config_name.get("0.0", "end").strip()
        clean = "".join(c for c in text if c not in Window.INVALID_FILENAME_CHARS)
        if text != clean:
            save_config_name.delete("0.0", "end")
            save_config_name.insert("0.0", clean)
    save_config_name.bind("<KeyRelease>", valid_filename)

    # To save the actual config
    def save_as():
        file_name = save_config_name.get("0.0", "end").strip()
        path = "data\\configs\\" + file_name
        if len(file_name) == 0:
            Popup("Error", Text.LANGUAGES[Text.LANGUAGE]["Save Actual Config Error Name"])
            subwindow.grab_set()
            return
        elif os.path.isfile(path):
            Popup("Error", Text.LANGUAGES[Text.LANGUAGE]["Save Actual Config Error"])
            subwindow.grab_set()
            return
        parameters.get_parameters()
        with open(path, "w", encoding="utf-8") as file:
            for line in parameters.lignes:
                line_splited = line.split("=")
                if line_splited[0] != "language" and line_splited[0] != "loading":
                    file.write(line)
            new_config_name = ctk.CTkButton(config_scroll, text=file_name)
            new_config_name.configure(command=lambda self=config_name, full_path=path: config_option(self, full_path))
            new_config_name.pack(pady=5, fill="x")
        parameters.lignes = None

    #Button to save the config
    save_button = ctk.CTkButton(top_frame, text=Text.LANGUAGES[Text.LANGUAGE]["Save Actual Config"], command=save_as)
    save_button.pack(pady=10)

    # List of the actual config status
    actual_config_scroll = ctk.CTkScrollableFrame(right_frame, label_text=Text.LANGUAGES[Text.LANGUAGE]["Actual Configuration"])
    actual_config_scroll.pack(fill="both", expand=True, padx=5, pady=10)

    # Add each line of the config
    def setup_actual_config_content():
        for child in actual_config_scroll.winfo_children():
            child.destroy()
        parameters.get_parameters()
        for line in parameters.lignes:
            line_splited = line.split("=")
            if line_splited[0] != "language" and line_splited[0] != "loading":
                config = ctk.CTkLabel(actual_config_scroll, text=f"n°{line_splited[0]} -> {line_splited[1]}", anchor="n")
                config.pack(fill="x", pady=0)
        parameters.lignes = None
    setup_actual_config_content()