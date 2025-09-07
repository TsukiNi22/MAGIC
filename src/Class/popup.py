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
##  main_window.py

File Description:
##  Popup class used to display:
##      - information
##      - question
##      - warning
##      - error
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
# Import that can't be in the try
from src.const import Error, Window
from sys import exit

# Import that can be checked
try:
    import customtkinter as ctk # Used for the graphics interface / GUI
except ImportError as e:
    print(f"Import Error: {e}")
    exit(Error.FATAL_ERROR)

""" Class """
class Popup(ctk.CTkToplevel):
    """
        Class to display information, warning or error
    """

    def __init__(self, popup_type="Information", message="", buttons=("Ok",)):
        """
            Initialisation of the class

            :param popup_type: Type of the window, 'Information', 'Question', 'Warning' or 'Error'
            :param message: Message to display
            :param buttons: List of the button to show
        """
        super().__init__()

        # Setup the main parameter
        self.title(popup_type)
        self.resizable(False, False)

        # Take the focus
        self.grab_set()
        self.focus_force()

        # Choice made by the user
        self.ouput = None

        # Set the appearance from the type
        colors = {
            "Information": ("#1B70AB", "ℹ️"),   # Blue
            "Question": ("#515759", "❔"),       # White
            "Warning": ("#9C7E08", "⚠️"),       # Yellow
            "Error": ("#9E1B0D", "❌")          # Red
        }
        color, icon = colors.get(popup_type, ("#515759", "[None]"))

        # Frame message
        message_frame = ctk.CTkFrame(self, width=10, height=10, corner_radius=10, fg_color=color)
        message_frame.pack(side="top", fill="both", expand=True, padx=10, pady=(10, 5))

        # Icon display
        icon_label = ctk.CTkLabel(message_frame, text=icon, font=("Arial", 32))
        icon_label.pack(side="left", padx=5)

        # Message display
        message_label = ctk.CTkLabel(message_frame, text=message, wraplength=300, justify="left", font=Window.POPUP_FONT)
        message_label.pack(side="left", padx=5)

        # Frame for the buttons
        buttons_frame = ctk.CTkFrame(self, fg_color="transparent",
            width=Window.POPUP_WIDTH - Window.BUTTON_PADX * 2, height=Window.BUTTON_HEIGHT + Window.BUTTON_PADY * 2)
        buttons_frame.pack(side="bottom", pady=(10, 5))

        # setup of the buttons
        for button_name in buttons:
            button = ctk.CTkButton(buttons_frame, text=button_name, font=Window.POPUP_FONT, command=lambda x=button_name: self._set_result(x))
            button.pack(side="left", padx=Window.BUTTON_PADX, pady=Window.BUTTON_PADY)

        # Setup the default size and position
        self.update_idletasks()
        w, h = self.winfo_width(), self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"{Window.POPUP_WIDTH}x{Window.POPUP_HEIGHT}+{x}+{y}")

        self.protocol("WM_DELETE_WINDOW", self._on_close)

        # Wait for the awnser
        self.wait_window(self)

    def _set_result(self, value):
        self.result = value
        self.destroy()

    def _on_close(self):
        self.result = None
        self.destroy()