"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

 ██╗  ██╗ █████╗ ██████╗ ████████╗ █████╗ ███╗   ██╗██╗ █████╗ 
 ╚██╗██╔╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗████╗  ██║██║██╔══██╗
  ╚███╔╝ ███████║██████╔╝   ██║   ███████║██╔██╗ ██║██║███████║
  ██╔██╗ ██╔══██║██╔══██╗   ██║   ██╔══██║██║╚██╗██║██║██╔══██║
 ██╔╝ ██╗██║  ██║██║  ██║   ██║   ██║  ██║██║ ╚████║██║██║  ██║
 ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝

Edition:
##  13/09/2025 by Tsukini

File Name:
##  upload_window.py

File Description:
##  Build of the upload window items
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
# Import that can't be in the try
from src.const import Error, Window, Text
from sys import exit

# Import that can be checked
try:
    import customtkinter as ctk # Used for the graphics interface / GUI
    from window_build.window_geometry import setup_geometry # Used to setup the default size & position
    from Class.parameters import Parameters # Used to read the parameters
except ImportError as e:
    print(f"Import Error: {e}")
    exit(Error.FATAL_ERROR)

""" Program """
def build(window):
    """
        Build the setting editor window items
        :param window: Main window of the app
    """

    # Init the global variable
    parameters = Parameters()

    # Setup the window
    subwindow = ctk.CTkToplevel(window)
    subwindow.title(Text.LANGUAGES[Text.LANGUAGE]["Settings"])
    subwindow.iconbitmap(default="data\\img\\MAGIC_icon_v3.ico")
    subwindow.resizable(width=False, height=False)
    setup_geometry(subwindow, Window.SETTING_WIDTH, Window.SETTING_HEIGHT)
    subwindow.grab_set()

    # Language label
    label1 = ctk.CTkLabel(subwindow, text=Text.LANGUAGES[Text.LANGUAGE]["Language"] + " :")
    label1.grid(row=0, column=0, padx=Window.SETTING_PAD, pady=Window.SETTING_PAD, sticky="w")

    # When the language list option selection is changed
    def language_list_update(choice):
        parameters.set_parameter("language", choice)

    # Language list of option
    choice_var = ctk.StringVar(value=Text.LANGUAGE)
    option_menu = ctk.CTkOptionMenu(subwindow, values=Text.AUTHORIZED_LANGUAGES, variable=choice_var, command=language_list_update)
    option_menu.grid(row=0, column=1, padx=Window.SETTING_PAD, pady=Window.SETTING_PAD, sticky="ew")

    # Loading screen
    label2 = ctk.CTkLabel(subwindow, text=Text.LANGUAGES[Text.LANGUAGE]["Loading Screen"] + " :")
    label2.grid(row=1, column=0, padx=Window.SETTING_PAD, pady=Window.SETTING_PAD, sticky="w")

    # When the loading screen option is changed
    def loading_screen_update():
        text = button.cget("text")
        if text == Text.LANGUAGES[Text.LANGUAGE]["Disabled"]:
            status = Text.LANGUAGES[Text.LANGUAGE]["Enabled"]
            parameters.set_parameter("loading", "1")
        else:
            status = Text.LANGUAGES[Text.LANGUAGE]["Disabled"]
            parameters.set_parameter("loading", "0")
        button.configure(text=status)

    # Loading screen option
    button = ctk.CTkButton(subwindow, text=(Text.LANGUAGES[Text.LANGUAGE]["Enabled"] if parameters.get_parameter("loading") == "1" else Text.LANGUAGES[Text.LANGUAGE]["Disabled"]), command=loading_screen_update)
    button.grid(row=1, column=1, padx=Window.SETTING_PAD, pady=Window.SETTING_PAD, sticky="ew")

    # Display of the actual config
    scroll_frame = ctk.CTkScrollableFrame(subwindow, label_text=Text.LANGUAGES[Text.LANGUAGE]["Actual Configuration"])
    scroll_frame.grid(row=2, column=0, columnspan=2, padx=Window.SETTING_PAD, pady=Window.SETTING_PAD, sticky="nsew")

    # Add each line of the config
    parameters.get_parameters()
    for line in parameters.lignes:
        line_splited = line.split("=")
        if line_splited[0] != "language" and line_splited[0] != "loading":
            lbl = ctk.CTkLabel(scroll_frame, text=f"n°{line_splited[0]} -> {line_splited[1]}", anchor="n")
            lbl.pack(fill="x", pady=0)
    parameters.lignes = None

    # Setup the grid of the subwindow
    subwindow.grid_rowconfigure(2, weight=1)
    subwindow.grid_columnconfigure(1, weight=1)