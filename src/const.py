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
##  const.py

File Description:
##  Constants of the project
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Return:
    """
        Return values
    """
    OK = 0 # Return value upon success on a call function
    KO = 1 # Return value upon fail on a call function

class Error:
    """
        Error values
    """
    FATAL_ERROR = 0b1000 # Global error, the program whole execution won't be able to run after this        (100% execution stop)
    LOCAL_ERROR = 0b100 # Local error, the program local execution won't probably be able to run after this (some chance of execution stop)
    ACTION_ERROR = 0b10 # Same~~ as Return.KO, a program action execution won't be able to run after this   (low chance of execution stop)

class Window:
    """
        Window size, color and other thing for the button, frame, window and other
    """

    # Main
    WIDTH = 1175 # X size of the window
    HEIGHT = 760 # Y size of the window

    # Scrollable Frame
    SCROLLABLE_FRAME_WIDTH = 1075 # X size of the scrollable frame
    SCROLLABLE_FRAME_HEIGHT = 550 # Y size of the scrollable frame

    # Frame
    FRAME_PADX = 15 # Padding X of the frames
    FRAME_PADY = 15 # Padding Y of the frames

    # Button
    BUTTON_FONT = ("Arial", 25) # Font used for the buttons
    BUTTON_WIDTH = 250 # X size of the buttons
    BUTTON_HEIGHT = 40 # Y size of the buttons
    BUTTON_PADX = 15 # Padding X of the buttons
    BUTTON_PADY = 7.5 # Padding Y of the buttons

    # Label
    LABEL_FONT = ("Arial", 20) # Font used for the labels
    LABEL_WIDTH = 250 # X size of the labels
    LABEL_HEIGHT = 40 # Y size of the labels
    LABEL_PADX = 15 # Padding X of the labels
    LABEL_PADY = 12.5 # Padding Y of the labels

    # Popup
    POPUP_FONT = ("Arial", 15) # Font used for the popup
    POPUP_WIDTH = 400 # X size of the popup
    POPUP_HEIGHT = 175 # Y size of the popup

class Color:
    """
        Different colors
    """
    DARK_GREY = "#222222"
    GREY = "#2D2D2D"
    DARK_RED = "#550E0E"
    RED = "#741010"
    BLUE = "#2F64B4"

class Text:
    """
        Text in the different languages
    """

    # English version
    english = {
        "Tab Buttons": ["Save Parameter", "Parameter Manager", "Script Editor", "Update Card Material"],
        "Save Parameter": "Save Parameter",
        "Parameter Manager": "Parameter Manager",
        "Script Editor": "Script Editor",
        "Update Card Material": "Update Card Material",
        "Sort": "Short By",
        "Sort N": "Number",
        "Sort Type": "Short By Type",
        "Sort B/P": "Button / Potentiometer",
        "Sort P/B": "Potentiometer / Button",
        "Card Upload": "Upload Card Program",
        "Manual Port": "Manual Card Port Selection",
        "Warning": "If something don\'t work there some chance that\nyour port is already connected to another thing",
    }

    # Language selection
    LANGUAGES = {
        "eng": english,
    }