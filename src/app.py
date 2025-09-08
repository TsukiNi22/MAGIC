"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

 ██╗  ██╗ █████╗ ██████╗ ████████╗ █████╗ ███╗   ██╗██╗ █████╗ 
 ╚██╗██╔╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗████╗  ██║██║██╔══██╗
  ╚███╔╝ ███████║██████╔╝   ██║   ███████║██╔██╗ ██║██║███████║
  ██╔██╗ ██╔══██║██╔══██╗   ██║   ██╔══██║██║╚██╗██║██║██╔══██║
 ██╔╝ ██╗██║  ██║██║  ██║   ██║   ██║  ██║██║ ╚████║██║██║  ██║
 ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝

Edition:
##  08/09/2025 by Tsukini

File Name:
##  app.py

File Description:
##  Call of the main function & setup of the app basic things
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
# Import that can't be in the try
from const import Return, Error
from sys import exit

# Import that can be checked
try:
    from window_build import main_window, potentiometer, button # Build of the window items
except ImportError as e:
    print(f"Import Error: {e}")
    exit(Error.FATAL_ERROR)

""" Program """
def app(window):
    """
        Call of the setup function & initialisation of the basic things
        :param window: Main window of the app
        :return: success or error
    """

    # Setup of the window
    scrollable_frame = main_window.build(window)

    for i in range(7):
        potentiometer.add_potentiometer(scrollable_frame, i)
    for i in range(7):
        button.add_button(scrollable_frame, i)

    return Return.OK