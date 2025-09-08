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
##  device.py

File Description:
##  Build a potentiometer frame
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from tkinter import Widget

""" Import """
# Import that can't be in the try
from src.const import Error, Window, Color, Math, Text
from sys import exit

# Import that can be checked
try:
    import customtkinter as ctk  # Used for the graphics interface / GUI
    from PIL import Image # Used to load the pictures
except ImportError as e:
    print(f"Import Error: {e}")
    exit(Error.FATAL_ERROR)

def add_device(scrollbar, indice, value, type):
    """
        Setup the default position and size of the given window
        :param scrollbar: Parent scrollbar
        :param indice: Indice for the Button or Potentiometer
        :param value: Default value
        :param type: Type can only be 'Potentiometer' or 'Button' else there will be an unknow device
    """

    # Setup of the var from the type
    if type == "Button":
        basic_value = ("High" if value == 1 else "Low")
        picture = "data\\img\\button.png"
        picture_size = Window.BUTTON_PICTURE_SIZE
    elif type == "Potentiometer":
        basic_value = f"{round(((value - Math.POTENTIOMETER_CORRECTIF) * 100) / 1023)}%"
        picture = "data\\img\\potentiometer.png"
        picture_size = Window.POTENTIOMETER_PICTURE_SIZE
    else:
        basic_value = "[None]"
        indice = "-1"
        picture = "data\\img\\none.png"
        picture_size = Window.NONE_PICTURE_SIZE
        type = "Unknown"

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
    name_label = ctk.CTkLabel(frame, text_color=Color.WHITE, text=Text.LANGUAGES[Text.LANGUAGE][type] + indice, fg_color='transparent',
        width=int(Window.DEVICE_WIDTH * coef), height=Window.LABEL_HEIGHT, font=Window.LABEL_FONT)
    name_label.place(x=int(Window.DEVICE_WIDTH * (1 - coef)) // 2, y=0)
    value_label = ctk.CTkLabel(frame, text_color=Color.WHITE, text=basic_value, fg_color='transparent',
        width=int(Window.DEVICE_WIDTH * coef), height=Window.LABEL_HEIGHT, font=Window.LABEL_FONT)
    value_label.place(x=int(Window.DEVICE_WIDTH * (1 - coef)) // 2, y=Window.LABEL_HEIGHT)

    # Setup of the picture
    img = ctk.CTkImage(size=picture_size, light_image=Image.open(picture), dark_image=Image.open(picture))
    picture = ctk.CTkLabel(frame, image=img, text="", fg_color='transparent')
    picture.place(x=(Window.DEVICE_WIDTH - picture_size[0]) // 2,
        y=(Window.LABEL_HEIGHT * 2) + ((Window.DEVICE_HEIGHT - ((Window.LABEL_HEIGHT * 2) + Window.BUTTON_HEIGHT + (Window.BUTTON_PADY * 2))) // 2) - (picture_size[1] // 2))

    # Setup of the parameter button
    parameters = ctk.CTkButton(frame, fg_color=Color.BLUE, text=Text.LANGUAGES[Text.LANGUAGE]["Parameters"],
        width=Window.DEVICE_WIDTH - (Window.BUTTON_PADX * 2), height=Window.BUTTON_HEIGHT, corner_radius=10,
        font=Window.BUTTON_FONT, command=print("Nop"))
    parameters.place(x=Window.BUTTON_PADX, y=Window.DEVICE_HEIGHT - (Window.BUTTON_HEIGHT + Window.BUTTON_PADY))

    return value_label