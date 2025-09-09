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
##  reset_card.py

File Description:
##  Reset the card program
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
# Import that can't be in the try
from src.const import Error, Return, Text
from sys import exit

# Import that can be checked
try:
    from window_build import device # Build of the window items
    from Class.loading import LoadingOverlay # Used to display the loading frame
    from Class.popup import Popup # Used to display information
    from time import sleep # Used to wait
except ImportError as e:
    print(f"Import Error: {e}")
    exit(Error.FATAL_ERROR)

""" Program """
def reset_card(window, scrollable_frame, card):
    """
        Reset the card connection & the scrollbar child
        :param window: Main program window
        :param scrollable_frame: Parent scrollbar
        :param card: Card interaction class
    """

    # Init the loading overlay
    loading = LoadingOverlay(window, "Serial port connection, Loading")
    loading.start()

    # If the card is already connected, disconnect it
    if card.running:
        card.stop_serial_port_read()
        # Wait for the end of the ancient port
        while card.running or card.serial_port.is_open:
            sleep(.1)
        card.serial_port_close()

    # Try to connect to the port 'COM3'
    if card.serial_port_open() == Return.OK:
        # Start the reading of the 'COM3'
        card.start_serial_port_read()
        loading.stop()

        # Check if the thread has encoutered an error
        if card.thread_status != Return.OK:
            # Error of reading in the thread
            Popup("Warning", Text.LANGUAGES[Text.LANGUAGE]["Default Port Connection Warning"], ("Ok",))
    else:
        loading.stop()
        Popup("Warning", Text.LANGUAGES[Text.LANGUAGE]["Default Port Connection Warning"], ("Ok",))