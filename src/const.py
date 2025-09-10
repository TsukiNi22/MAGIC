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
    WIDTH = 1150 # X size of the window
    HEIGHT = 775 # Y size of the window

    # Scrollable Frame
    SCROLLABLE_FRAME_WIDTH = 1050 # X size of the scrollable frame
    SCROLLABLE_FRAME_HEIGHT = 550 # Y size of the scrollable frame

    # Frame
    FRAME_PADX = 15 # Padding X of the frames
    FRAME_PADY = 15 # Padding Y of the frames

    # SubWindow
    SUBWINDOW_WIDTH = 325 # X size of the subwindow
    SUBWINDOW_HEIGHT = 110 # Y size of the subwindow

    # Device
    NB_DEVICE_LINE = 5 # Number of device display per line
    DEVICE_PADX = 10 # Padding X of the devices
    DEVICE_PADY = 15 # Padding Y of the devices
    DEVICE_WIDTH = (SCROLLABLE_FRAME_WIDTH / NB_DEVICE_LINE) - (DEVICE_PADX * 2) # X size of the scrollable devices
    DEVICE_HEIGHT = 250 # Y size of the scrollable devices
    BUTTON_PICTURE_SIZE = (75, 75) # Size of the picture
    POTENTIOMETER_PICTURE_SIZE = (70, 125) # Size of the picture
    NONE_PICTURE_SIZE = (75, 75) # Size of the picture

    # Button
    BUTTON_FONT = ("Arial", 25) # Font used for the buttons
    BUTTON_WIDTH = 250 # X size of the buttons
    BUTTON_HEIGHT = 40 # Y size of the buttons
    BUTTON_PADX = 15 # Padding X of the buttons
    BUTTON_PADY = 10 # Padding Y of the buttons

    # Label
    LABEL_FONT = ("Arial", 20) # Font used for the labels
    LABEL_WIDTH = 250 # X size of the labels
    LABEL_HEIGHT = 30 # Y size of the labels
    LABEL_PADX = 15 # Padding X of the labels
    LABEL_PADY = 12.5 # Padding Y of the labels

    # Popup
    POPUP_FONT = ("Arial", 15) # Font used for the popup
    POPUP_WIDTH = 400 # X size of the popup
    POPUP_HEIGHT = 175 # Y size of the popup

    # Loading Overlay
    LOADING_OVERLAY_FONT = ("Arial", 18) # Font used for the loading overlay
    LOADING_OVERLAY_PADX = 30 # Padding X of the loading overlay
    LOADING_OVERLAY_PADY = 15 # Padding Y of the loading overlay

class Color:
    """
        Different colors
    """
    DARK = "#111111"
    WHITE = "#FFFFFF"
    DARK_GREY = "#222222"
    GREY = "#2D2D2D"
    DARK_RED = "#550E0E"
    RED = "#741010"
    BLUE = "#2F64B4"

class Math:
    """
        Different math value used
    """
    POTENTIOMETER_CORRECTIF = 3 # Used to have the 0% and the 100%

class Board:
    """
        Different value used for the card
    """
    # Path
    PROGRAM_FILE = "arduino\\arduino.ino" # Path of the program
    ARDUINO_CLI = "arduino\\arduino-cli.exe" # Path of the executable used to upload the program

    # List of the board for the arduini-cli
    BOARDS = {
        "Arduino Uno": "arduino:avr:uno",
        "Arduino Nano": "arduino:avr:nano",
        "Arduino Mega 2560": "arduino:avr:mega",
        "Arduino Leonardo": "arduino:avr:leonardo",
        "Arduino Micro": "arduino:avr:micro",
        "Arduino Mini": "arduino:avr:mini",
        "Arduino Ethernet": "arduino:avr:ethernet",
        "Arduino Fio": "arduino:avr:fio",
        "Arduino BT": "arduino:avr:bt",
        "Arduino Duemilanove": "arduino:avr:diecimila",
        "Arduino Pro / Pro Mini": "arduino:avr:pro",
        "Arduino Yun": "arduino:avr:yun",
        "Arduino Esplora": "arduino:avr:esplora",
        "Arduino Zero": "arduino:samd:arduino_zero_native",
        "Arduino MKR1000": "arduino:samd:mkr1000",
        "Arduino MKR WiFi 1010": "arduino:samd:mkrwifi1010",
        "Arduino Nano 33 IoT": "arduino:samd:nano_33_iot",
        "Arduino Nano 33 BLE": "arduino:mbed:nano33ble",
        "Arduino Nano 33 BLE Sense": "arduino:mbed:nano33blesense",
    }

class Text:
    """
        Text in the different languages
    """
    LANGUAGE = "eng" # Language used

    # English version
    english = {
        # Button/Label text
        "Tab Buttons": ["Save Parameter", "Parameter Manager", "Script Editor", "Update Card"],
        "Sort": "Short By",
        "Sort N": "Number",
        "Sort Type": "Short By Type",
        "Sort B/P": "Button / Potentiometer",
        "Sort P/B": "Potentiometer / Button",
        "Card Upload": "Upload Card Program",
        "Manual Port": "Manual Card Port Selection",
        "Manual Port Selection": "Select Port",
        "Warning": "If something don\'t work there some chance that\nyour port is already connected to another thing",
        "Potentiometer": "Potentiometer n°",
        "Button": "Button n°",
        "Parameters": "Parameters",
        "Unknown": "Unknown",

        # Popup button text
        "Cancel": "Cancel",
        "Try": "Try",
        "Upload": "Upload",

        # Loading overlay message
        "Port Connection Loading": "Serial port connection, Loading",
        "Upload Loading": "Program upload, Loading",

        # Popup message
        "Upload Success": "The program have been successfully uploaded on the card named 'CARD'",
        "Upload Error": "The upload of the program on the card 'CARD' with the port 'PORT' have failed! Error: INFO",
        "Port No Device Found Warning": "The connection to the serial port 'PORT' haven't found any peripheral device after 5s, retry on another port with the 'Manual Card Port Selection'!",
        "Default Port Connection Warning": "The connection to the serial port 'PORT' wasn't succeful, retry, if that still doesn't work retry with the 'Manual Card Port Selection'!",

        # Instructions:
        #   - STRING -> Textbox with any string
        #   - INT -> Textbox that only accept int
        #   - UINT -> Textbox that only accept int above 0
        #   - PERCENTAGE -> Textbox that only accept int from 0 to 100
        #   - PATH -> Button to choice a file
        #   - LIST -> list of choice
        #   - KEY -> Button that take the next key press
        # Script text, cut on the ':'
        #---------------  Action  ---------------
        "Move To": "Move to:INT:x:INT:y",
        "Move of To": "Move of:INT:to:LIST",
        "Set Sound": "Set sound to:PERCENTAGE:%",
        "Set Sound Percentage": "Set sound to potentiometer percentage",
        "Write": "Write:STRING",
        "Open Link": "Open:STRING",
        "Execute": "Execute:PATH",
        #--------------- Keyboard ---------------
        "Press Key": "Press:KEY",
        "Press Key For": "Press:KEY:for:UINT:ms",
        "Key D/U": "KEY:LIST",
        "Click": "LIST:Click",
        "Double Click": "Double:LIST:Click",
        "Click D/U": "Click:LIST",
        "Click At": "LIST:Click at:INT:x:INT:y",
        #---------------  Others  ---------------
        "Popup": "Popup:STRING",
        "Wait": "Wait:UINT:ms",
        "Invert Value": "Invert potentiometer value",
        #--------------- Advenced ---------------
        "Label": "Label:STRING",
        "GoTo": "Goto label:STRING",
        "For": "For:UINT:time",
        "End For": "End For",
    }

    # Language selection
    LANGUAGES = {
        "eng": english,
    }