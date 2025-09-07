"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

 ██╗  ██╗ █████╗ ██████╗ ████████╗ █████╗ ███╗   ██╗██╗ █████╗ 
 ╚██╗██╔╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗████╗  ██║██║██╔══██╗
  ╚███╔╝ ███████║██████╔╝   ██║   ███████║██╔██╗ ██║██║███████║
  ██╔██╗ ██╔══██║██╔══██╗   ██║   ██╔══██║██║╚██╗██║██║██╔══██║
 ██╔╝ ██╗██║  ██║██║  ██║   ██║   ██║  ██║██║ ╚████║██║██║  ██║
 ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝

Edition:
##  07/09/2025 by Tsukini

File Name:
##  main_window.py

File Description:
##  Build of the main window items
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
# Import that can't be in the try
from src.const import Return, Error, Window, Text
from sys import exit

# Import that can be checked
try:
    import customtkinter as ctk # Used for the graphics interface / GUI
    from screeninfo import get_monitors # Get the monitors
    from pyautogui import position # Get the mouse position
except ImportError as e:
    print(f"Import Error: {e}")
    exit(Error.FATAL_ERROR)

""" Program """
def get_actual_monitor():
    # Get the mouse position
    mouse_x, mouse_y = position()

    # For each monitor try to find the one who have the mouse in it
    for monitor in get_monitors():
        if monitor.x <= mouse_x <= monitor.x + monitor.width and monitor.y <= mouse_y <= monitor.y + monitor.height:
            return monitor

    # If no one was found set the first in the list
    return get_monitors()[0]

def setup_geometry(window):
    # Get the monitor where the mouse is positioned
    monitor = get_actual_monitor()

    # Get the central position of the minitor
    x = monitor.x + (monitor.width // 2) - (Window.WIDTH // 2)
    y = monitor.y + (monitor.height // 2) - (Window.HEIGHT // 2)

    # Setup the geometry of the window
    window.geometry(f"{Window.WIDTH}x{Window.HEIGHT}+{x}+{y}")

def setup_tab(window):
    """
    Build the tab with the buttons: Save Parameter, Parameter Manager, Script Editor and Update Card Material

    :param window: Main window of the app
    """

    # Tab that will contain the button
    tab = ctk.CTkFrame(window, fg_color=Window.FRAME_COLOR, corner_radius=10)

    # Build the different button
    button_names = ["Save Parameter", "Parameter Manager", "Script Editor", "Update Card Material"]
    button_functions = [print("Nop"), print("Nop"), print("Nop"), print("Nop")]
    for i in range(len(button_names)):
        button = ctk.CTkButton(tab, fg_color=Window.BUTTON_COLOR, text=Text.LANGUAGES["eng"][button_names[i]],
            width=Window.BUTTON_WIDTH, height=Window.BUTTON_HEIGHT, corner_radius=10,
            font=Window.BUTTON_FONT, command=lambda: button_functions[i])
        button.grid(column=i, row=0, padx=Window.BUTTON_PADX, pady=Window.BUTTON_PADY)

    # Setup the place of the tab
    tab.place(x=(Window.WIDTH - (Window.BUTTON_PADX * len(button_names) * 2) - (Window.BUTTON_WIDTH * 4)) // 2, y=Window.FRAME_PADY)

def setup_peripheral_device_list(window):
    """
    Build the list used for the peripheral device information display

    :param window: Main window of the app
    """

    pass

def setup_card_tab(window):
    """
    Build the tab with the buttons to setup / update the card connection

    :param window: Main window of the app
    """

    pass

def build(window):
    """
    Build the main window items (dispatch to sub functions)

    :param window: Main window of the app
    :return: success or error
    """

    # Setup main window parameters
    window.title("MAGIC")
    window.iconbitmap(default="data\\img\\MAGIC_icon_v3.ico")
    window.resizable(width=False, height=False) # To change in the future
    setup_geometry(window)

    # Setup the interface
    setup_tab(window)
    setup_peripheral_device_list(window)
    setup_card_tab(window)

    return Return.OK