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
    WIDTH = 1200 # X size of the window
    HEIGHT = 800 # Y size of the window

    # Frame
    FRAME_COLOR = "#2D2D2D" # Background color of the frames
    FRAME_PADX = 15 # Padding X of the frames
    FRAME_PADY = 15 # Padding Y of the frames

    # Button
    BUTTON_COLOR = "#2F64B4" # Background color of the buttons
    BUTTON_FONT = ("Arial", 25) # Font used for the buttons
    BUTTON_WIDTH = 250 # X size of the buttons
    BUTTON_HEIGHT = 40 # Y size of the buttons
    BUTTON_PADX = 15 # Padding X of the buttons
    BUTTON_PADY = 7.5 # Padding Y of the buttons

class Text:
    """
        Text in the different languages
    """

    # English version
    english = {
        "Save Parameter": "Save Parameter",
        "Parameter Manager": "Parameter Manager",
        "Script Editor": "Script Editor",
        "Update Card Material": "Update Card Material",
        "Sort": "Short By",
        "Sort N": "Number",
        "Sort Type": "Short By Type",
        "Sort B/P": "Button / Potentiometer",
        "Sort P/B": "Potentiometer / Button",
    }

    # Language selection
    LANGUAGES = {
        "eng": english,
    }