"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

 ██╗  ██╗ █████╗ ██████╗ ████████╗ █████╗ ███╗   ██╗██╗ █████╗ 
 ╚██╗██╔╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗████╗  ██║██║██╔══██╗
  ╚███╔╝ ███████║██████╔╝   ██║   ███████║██╔██╗ ██║██║███████║
  ██╔██╗ ██╔══██║██╔══██╗   ██║   ██╔══██║██║╚██╗██║██║██╔══██║
 ██╔╝ ██╗██║  ██║██║  ██║   ██║   ██║  ██║██║ ╚████║██║██║  ██║
 ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝

Edition:
##  09/09/2025 by Tsukini

File Name:
##  port_selection_window.py

File Description:
##  Build of the manual port selection window items
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
# Import that can't be in the try
from src.const import Error, Window, Color, Text
from sys import exit

# Import that can be checked
try:
    import customtkinter as ctk # Used for the graphics interface / GUI
    from serial.tools.list_ports import comports # Obtains the list of the port
    from window_build.window_geometry import setup_geometry # Used to setup the default size & position
    from tool.reset_card import reset_card # Use to initialise/reset the card connection
except ImportError as e:
    print(f"Import Error: {e}")
    exit(Error.FATAL_ERROR)

""" Program """
def build(window, scrollable_frame, card):
    """
        Build the manual port selection window items
        :param window: Main window of the app
        :param scrollable_frame: Parent scrollbar
        :param card: Card interaction class
        :return: success or error
    """

    # Create & Setup the subwindow parameters
    subwindow = ctk.CTkToplevel(window)
    subwindow.title(Text.LANGUAGES[Text.LANGUAGE]["Manual Port"])
    subwindow.iconbitmap(default="data\\img\\MAGIC_icon_v3.ico")
    subwindow.resizable(width=False, height=False)
    setup_geometry(subwindow, Window.SUBWINDOW_WIDTH, Window.SUBWINDOW_HEIGHT)
    subwindow.grab_set()

    # Sort options setup
    sort_list_var = ctk.StringVar()
    options = [port.description for port in comports()]
    port_list = ctk.CTkOptionMenu(subwindow, hover=False, fg_color=Color.DARK_GREY, button_color=Color.DARK_GREY, font=Window.POPUP_FONT,
        width=Window.BUTTON_WIDTH, height=Window.BUTTON_HEIGHT, corner_radius=10,
        variable=sort_list_var, values=options)
    port_list.set("三 " + Text.LANGUAGES[Text.LANGUAGE]["Manual Port Selection"] + "...")
    port_list.pack(pady=10)

    # Frame for the buttons
    frame = ctk.CTkFrame(subwindow, fg_color="transparent")
    frame.pack(pady=10)

    # Cancel button
    cancel_button = ctk.CTkButton(frame, text=Text.LANGUAGES[Text.LANGUAGE]["Cancel"], font=Window.BUTTON_FONT, command=subwindow.destroy)
    cancel_button.pack(side="left", padx=10)

    # Try button
    try_button = ctk.CTkButton(frame, text=Text.LANGUAGES[Text.LANGUAGE]["Try"], font=Window.BUTTON_FONT,
        command=lambda: (
            reset_card(window, scrollable_frame, card, port=sort_list_var.get().split("(")[1].split(")")[0]),
            subwindow.destroy()
        )
    )
    try_button.pack(side="left", padx=10)