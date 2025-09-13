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
    from time import sleep, time # Used to wait
except ImportError as e:
    print(f"Import Error: {e}")
    exit(Error.FATAL_ERROR)

""" Program """
def reset_card(window, sort_list_var, card, port="COM3"):
    """
        Reset the card connection & the scrollbar child
        :param window: Main program window
        :param sort_list_var: Var of the sort list choice
        :param card: Card interaction class
        :param port: Port of the card to connect
    """

    # Init the loading overlay
    loading = LoadingOverlay(window, Text.LANGUAGES[Text.LANGUAGE]["Port Connection Loading"])
    loading.start()

    # If the card is already connected, disconnect it
    if card.running:
        card.stop_serial_port_read()
        # Wait for the end of the ancient port
        while card.running or card.serial_port.is_open:
            sleep(.1)
        card.serial_port_close()

    # Reset the sort device choice
    sort_list_var.set("三 " + Text.LANGUAGES[Text.LANGUAGE]["Sort"] + "...")

    # Try to connect to the port
    if card.serial_port_open(port) == Return.OK:
        # Start the reading of the
        card.start_serial_port_read()

        # Wait until at least one device have been found or timeout
        start = time()
        timeout = 5
        while time() - start <= timeout and len(card.values_memory.keys()) == 0:
            window.update()
            sleep(.1)

        loading.stop()
        if card.thread_status != Return.OK: # If the thread has encoutered an error
            Popup("Warning", Text.LANGUAGES[Text.LANGUAGE]["Default Port Connection Warning"].replace("PORT", port), ("Ok",))
        elif time() - start > timeout:
            Popup("Warning", Text.LANGUAGES[Text.LANGUAGE]["Port No Device Found Warning"].replace("PORT", port), ("Ok",))
    else:
        loading.stop()
        Popup("Warning", Text.LANGUAGES[Text.LANGUAGE]["Default Port Connection Warning"].replace("PORT", port), ("Ok",))