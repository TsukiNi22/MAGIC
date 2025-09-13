"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

 ██╗  ██╗ █████╗ ██████╗ ████████╗ █████╗ ███╗   ██╗██╗ █████╗ 
 ╚██╗██╔╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗████╗  ██║██║██╔══██╗
  ╚███╔╝ ███████║██████╔╝   ██║   ███████║██╔██╗ ██║██║███████║
  ██╔██╗ ██╔══██║██╔══██╗   ██║   ██╔══██║██║╚██╗██║██║██╔══██║
 ██╔╝ ██╗██║  ██║██║  ██║   ██║   ██║  ██║██║ ╚████║██║██║  ██║
 ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝

Edition:
##  10/09/2025 by Tsukini

File Name:
##  script_selection_window.py

File Description:
##  Build of the device script selection window items
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from src.Class.popup import Popup

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
except ImportError as e:
    print(f"Import Error: {e}")
    exit(Error.FATAL_ERROR)

""" Program """
def build(window, indice):
    """
        Build the manual port selection window items
        :param window: Main window of the app
        :param indice: Indice of the linked device
        :return: success or error
    """

    # Init the parameters
    parameters = Parameters()

    # Create & Setup the subwindow parameters
    subwindow = ctk.CTkToplevel(window)
    subwindow.title(Text.LANGUAGES[Text.LANGUAGE]["Script Selection"] + f" n°{indice}")
    subwindow.iconbitmap(default="data\\img\\MAGIC_icon_v3.ico")
    subwindow.resizable(width=False, height=False)
    setup_geometry(subwindow, Window.SUBWINDOW_WIDTH, Window.SUBWINDOW_HEIGHT)
    subwindow.grab_set()

    # Sort options setup
    script_list_var = ctk.StringVar()
    dossier = (Path("data\\scripts\\potentiometer") if indice.__contains__("A") else Path("data\\scripts\\button"))
    options = ["[None]"] + [file.name for file in dossier.iterdir() if file.is_file()]
    script_list = ctk.CTkOptionMenu(subwindow, hover=False, fg_color=Color.DARK_GREY, button_color=Color.DARK_GREY, font=Window.POPUP_FONT,
        width=Window.BUTTON_WIDTH, height=Window.BUTTON_HEIGHT, corner_radius=10,
        variable=script_list_var, values=options)
    value = parameters.get_parameter(indice)
    default_text = "三 " + Text.LANGUAGES[Text.LANGUAGE]["Select Script"] + "..."
    script_list.set(default_text if value is None else value)
    script_list.pack(pady=10)

    # Frame for the buttons
    frame = ctk.CTkFrame(subwindow, fg_color="transparent")
    frame.pack(pady=10)

    # Cancel button
    cancel_button = ctk.CTkButton(frame, text=Text.LANGUAGES[Text.LANGUAGE]["Cancel"], font=Window.BUTTON_FONT, command=subwindow.destroy)
    cancel_button.pack(side="left", padx=10)

    # Try button
    try_button = ctk.CTkButton(frame, text=Text.LANGUAGES[Text.LANGUAGE]["Save"], font=Window.BUTTON_FONT,
        command=lambda: (
            parameters.set_parameter(indice, script_list_var.get()),
            subwindow.destroy()
        ) if default_text != script_list_var.get() else Popup("Error", Text.LANGUAGES[Text.LANGUAGE]["Nothing Seleted"].replace("WHAT", Text.LANGUAGES[Text.LANGUAGE]["script"]), ("Ok",))
    )
    try_button.pack(side="left", padx=10)