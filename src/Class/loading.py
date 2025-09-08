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
##  loading.py

File Description:
##  Popup class used to display a loading message
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
# Import that can't be in the try
from src.const import Error, Window, Color
from sys import exit

# Import that can be checked
try:
    import customtkinter as ctk # Used for the graphics interface / GUI
    import tkinter as tk # Used for the graphics interface / GUI
    from threading import Thread # Used for the thread
    from time import sleep # Used to wait between each update of the message
except ImportError as e:
    print(f"Import Error: {e}")
    exit(Error.FATAL_ERROR)

""" Class """
class LoadingOverlay(ctk.CTkFrame):

    def __init__(self, parent, message="Loading"):
        super().__init__(parent, fg_color=Color.DARK, border_color=Color.DARK_GREY, border_width=2, corner_radius=10)
        self.place(relx=0.5, rely=0.5, anchor="center")

        # Animated label
        self.label = ctk.CTkLabel(self, text=message, font=Window.LOADING_OVERLAY_FONT)
        self.label.pack(padx=Window.LOADING_OVERLAY_PADX, pady=Window.LOADING_OVERLAY_PADY)

        # Initialisation of the var
        self.message = message
        self.dots = ""

    def start(self):
        self.grab_set()
        self._animate()

    def stop(self):
        self.grab_release()
        self.destroy()

    def _animate(self):
        # Update the point
        self.dots = (self.dots + ".") if len(self.dots) < 3 else ""
        self.label.configure(text=self.message + self.dots)

        # Restart after 500ms
        self.after(500, self._animate)