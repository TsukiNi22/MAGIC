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
    from window_build import main_window # Build of the window items
    from event.reset_card import reset_card # Use to initialise/reset the card connection
    from Class.card_interaction import Card # Used for the card interaction
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
    tab, scrollable_frame, card_upload, card_manual_port = main_window.build(window)
    window.update()

    # Setup the card & loadind calss
    card = Card(scrollable_frame)
    reset_card(window, scrollable_frame, card)

    # Connect the different button to the event
    functions = [print('Nop'), print('Nop'), print('Nop'), lambda: reset_card(window, scrollable_frame, card)] # Save Parameter, Parameter Manager, Script Editor, Update Card
    buttons_name = Text.LANGUAGES[Text.LANGUAGE]["Tab Buttons"]
    buttons_function = {}
    for i in range(len(functions)):
        buttons_function[buttons_name[i]] = functions[i]
    for button in tab.winfo_children():
        button.configure(command=buttons_function[button.cget("text")])

    return Return.OK