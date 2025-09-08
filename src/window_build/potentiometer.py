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
##  potentiometer.py

File Description:
##  Build a potentiometer frame
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from tkinter import Widget

""" Import """
# Import that can't be in the try
from src.const import Error, Window, Color, Text
from sys import exit

# Import that can be checked
try:
    import customtkinter as ctk  # Used for the graphics interface / GUI
    from PIL import Image # Used to load the pictures
except ImportError as e:
    print(f"Import Error: {e}")
    exit(Error.FATAL_ERROR)

def add_potentiometer(scrollbar: ctk.CTkScrollableFrame, n):
    """
        Setup the default position and size of the given window
        :param scrollbar: Parent scrollbar
        :param n: Potentiometer number
    """

    # Creation of the frame
    frame = ctk.CTkFrame(scrollbar, fg_color=Color.DARK, corner_radius=10,
        width=Window.DEVICE_WIDTH, height=Window.DEVICE_HEIGHT)

    # Placement of the frame
    index = len(scrollbar.winfo_children()) - 1
    row = index // Window.NB_DEVICE_LINE
    col = index % Window.NB_DEVICE_LINE
    frame.grid(row=row, column=col, padx=Window.DEVICE_PADX, pady=Window.DEVICE_PADY, sticky="nsew")

    # Setup of the text
    coef = .9 # To not override the frame corner
    potentiometer_name = ctk.CTkLabel(frame, text_color=Color.WHITE, text=Text.LANGUAGES[Text.LANGUAGE]["Potentiometer"] + f" n°A{index}", fg_color='transparent',
        width=int(Window.DEVICE_WIDTH * coef), height=Window.LABEL_HEIGHT, font=Window.LABEL_FONT)
    potentiometer_name.place(x=int(Window.DEVICE_WIDTH * (1 - coef)) // 2, y=0)
    potentiometer_value = ctk.CTkLabel(frame, text_color=Color.WHITE, text="0%", fg_color='transparent',
        width=int(Window.DEVICE_WIDTH * coef), height=Window.LABEL_HEIGHT, font=Window.LABEL_FONT)
    potentiometer_value.place(x=int(Window.DEVICE_WIDTH * (1 - coef)) // 2, y=Window.LABEL_HEIGHT)

    # Setup of the picture
    img = ctk.CTkImage(size=Window.POTENTIOMETER_PICTURE_SIZE,
        light_image=Image.open("data\\img\\potentiometer.png"),
        dark_image=Image.open("data\\img\\potentiometer.png"))
    picture = ctk.CTkLabel(frame, image=img, text="", fg_color='transparent')
    picture.place(x=(Window.DEVICE_WIDTH - Window.POTENTIOMETER_PICTURE_SIZE[0]) // 2,
        y=Window.DEVICE_HEIGHT - (Window.BUTTON_HEIGHT + Window.BUTTON_PADY * 2 + Window.POTENTIOMETER_PICTURE_SIZE[1]))

    # Setup of the parameter button
    parameters = ctk.CTkButton(frame, fg_color=Color.BLUE, text=Text.LANGUAGES[Text.LANGUAGE]["Parameters"],
        width=Window.DEVICE_WIDTH - (Window.BUTTON_PADX * 2), height=Window.BUTTON_HEIGHT, corner_radius=10,
        font=Window.BUTTON_FONT, command=print("Nop"))
    parameters.place(x=Window.BUTTON_PADX, y=Window.DEVICE_HEIGHT - (Window.BUTTON_HEIGHT + Window.BUTTON_PADY))

    return potentiometer_value