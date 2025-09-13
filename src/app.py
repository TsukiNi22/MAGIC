"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

 ██╗  ██╗ █████╗ ██████╗ ████████╗ █████╗ ███╗   ██╗██╗ █████╗ 
 ╚██╗██╔╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗████╗  ██║██║██╔══██╗
  ╚███╔╝ ███████║██████╔╝   ██║   ███████║██╔██╗ ██║██║███████║
  ██╔██╗ ██╔══██║██╔══██╗   ██║   ██╔══██║██║╚██╗██║██║██╔══██║
 ██╔╝ ██╗██║  ██║██║  ██║   ██║   ██║  ██║██║ ╚████║██║██║  ██║
 ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝

Edition:
##  13/09/2025 by Tsukini

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
    from window_build import main_window, port_selection_window, upload_window, settings_window # Build of the window items
    from tool.reset_card import reset_card # Use to initialise/reset the card connection
    from tool.video_display import video_display # Used to display video
    from Class.card_interaction import Card # Used for the card interaction
    from Class.parameters import Parameters # Used to read the parameters
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
    tab, scrollable_frame, sort_list, card_upload, card_manual_port = main_window.build(window)

    # Setup the card
    card = Card(window, scrollable_frame)

    # Display the loading screen if activated else just setup card
    window.update()
    loading = Parameters().get_parameter("loading")
    if loading is not None and loading == "1":
        video_display(window, "data\\video\\loading-animation_resized.mp4", card=[window, sort_list, card]) # resized version: 1920x1080 -> 1603x1080
    else:
        reset_card(window, sort_list, card)

    # Connect the different button to the tool
    functions = [print('Nop'), print('Nop'), lambda: settings_window.build(window), lambda: reset_card(window, sort_list, card)] # Save Parameter, Parameter Manager, Script Editor, Update Card
    buttons_name = Text.LANGUAGES[Text.LANGUAGE]["Tab Buttons"]
    buttons_function = {}
    for i in range(len(functions)):
        buttons_function[buttons_name[i]] = functions[i]
    for button in tab.winfo_children():
        button.configure(command=buttons_function[button.cget("text")])
    card_upload.configure(command=lambda: upload_window.build(window, card))
    card_manual_port.configure(command=lambda: port_selection_window.build(window, scrollable_frame, card))

    return Return.OK