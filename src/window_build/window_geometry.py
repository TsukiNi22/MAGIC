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
##  window_geometry.py

File Description:
##  Build of the main window items
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
# Import that can't be in the try
from src.const import Error, Return
from sys import exit

# Import that can be checked
try:
    from screeninfo import get_monitors # Get the monitors
    from pyautogui import position # Get the mouse position
except ImportError as e:
    print(f"Import Error: {e}")
    exit(Error.FATAL_ERROR)

""" Program """
def get_actual_monitor():
    """
        Get the monitor who contain the mouse
        :return: Monitor where the mouse is located
    """

    # Get the mouse position
    mouse_x, mouse_y = position()

    # For each monitor try to find the one who have the mouse in it
    for monitor in get_monitors():
        if monitor.x <= mouse_x <= monitor.x + monitor.width and monitor.y <= mouse_y <= monitor.y + monitor.height:
            return monitor

    # If no one was found set the first in the list
    return get_monitors()[0]

def setup_geometry(window, width, height):
    """
        Setup the default position and size of the given window
        :param window: Window to setup the size & position
    """

    # Get the monitor where the mouse is positioned
    monitor = get_actual_monitor()

    # Get the central position of the minitor
    x = monitor.x + (monitor.width // 2) - (width // 2)
    y = monitor.y + (monitor.height // 2) - (height // 2)

    # Setup the geometry of the window
    window.geometry(f"{width}x{height}+{x}+{y}")
