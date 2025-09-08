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
import time

""" Import """
# Import that can't be in the try
from const import Return, Error, Text
from sys import exit

# Import that can be checked
try:
    from window_build import main_window, device # Build of the window items
    from Class.card_interaction import Card # Used for the card interaction
    from Class.loading import LoadingOverlay # Used to display the loading frame
    from Class.popup import Popup # Used to display information
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

    # Setup of the main window
    scrollable_frame = main_window.build(window)
    window.update()

    # Setup the card & loadind calss
    card = Card(scrollable_frame)
    loading = LoadingOverlay(window, "Serial port connection, Loading")
    loading.start()

    # Try to connect to the port 'COM3'
    if card.serial_port_open() == Return.OK:
        # Start the reading of the 'COM3'
        card.start_serial_port_read()

        # Wait~~ for the end of the void setup
        while not card.end_init and card.thread_status == Return.OK:
            window.update() # Update the loading overlay
            time.sleep(.1)
        loading.stop()

        # Check if the thread has encoutered an error
        if card.thread_status != Return.OK:
            # Error of reading in the thread
            Popup("Warning", Text.LANGUAGES[Text.LANGUAGE]["Init Port Connection Warning"], ("Ok",))
    else:
        loading.stop()
        Popup("Warning", Text.LANGUAGES[Text.LANGUAGE]["Init Port Connection Warning"], ("Ok",))

    return Return.OK