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
from src.const import Return, Error, Window
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

    return Return.OK