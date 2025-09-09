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
##  main.py

File Description:
##  Main file of project
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
# Import that can't be in the try
from const import Return, Error
from sys import exit

# Import that can be checked
try:
    import customtkinter as ctk # Used for the graphics interface / GUI
    from app import app # Main app setup & call of functions
    from tkinter import TclError # Error handling
except ImportError as e:
    print(f"Import Error: {e}")
    exit(Error.FATAL_ERROR)

""" Program """
# Check if the program is call from the right thing
if __name__ != "__main__":
    print("MAGIC can only be executed and not call!")
    exit(Error.FATAL_ERROR)

# Setup the default them & color
ctk.set_appearance_mode("dark")  # dark | light
ctk.set_default_color_theme("dark-blue")  # blue | green | dark-blue

# Setup of the main window
try:
    window = ctk.CTk()
except TclError as e:
    print(f"Tkinter initialisation Error: {e}")
    exit(Error.FATAL_ERROR)

# Call of the main program
ret = app(window)
if ret != Return.OK:
    exit(ret)

# Loop to keep the main window alive
window.mainloop()

# Program end
exit(Return.OK)