"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

 ██╗  ██╗ █████╗ ██████╗ ████████╗ █████╗ ███╗   ██╗██╗ █████╗ 
 ╚██╗██╔╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗████╗  ██║██║██╔══██╗
  ╚███╔╝ ███████║██████╔╝   ██║   ███████║██╔██╗ ██║██║███████║
  ██╔██╗ ██╔══██║██╔══██╗   ██║   ██╔══██║██║╚██╗██║██║██╔══██║
 ██╔╝ ██╗██║  ██║██║  ██║   ██║   ██║  ██║██║ ╚████║██║██║  ██║
 ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝

Edition:
##  11/09/2025 by Tsukini

File Name:
##  sort_device.py

File Description:
##  Sort the device frame from the selected option
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
# Import that can't be in the try
from src.const import Error, Text
from sys import exit

# Import that can be checked
try:
    import customtkinter as ctk # Used for the graphics interface / GUI
    from window_build import device # Build of the window items
except ImportError as e:
    print(f"Import Error: {e}")
    exit(Error.FATAL_ERROR)

""" Program """
def sort_device(window, sort_list, scrollable_frame, option):
    """
        Reset the card connection & the scrollbar child
        :param window: Main program window
        :param sort_list: List of the sort options
        :param scrollable_frame: Parent scrollbar of the frame device
        :param option: Option selected for the sort
    """
    # Set the text of the sort list
    sort_list.set("三 " + option + "...")

    # Get the list of the frame sorted
    device_indices = []
    device_values = {}
    for frame in scrollable_frame.winfo_children():
        for widget in frame.winfo_children():
            if not isinstance(widget, ctk.CTkLabel):
                continue
            text = widget.cget("text")
            if text.__contains__("n°"):
                device_indices.append(text.split("n°")[1])
                frame.destroy()
                break

    # Sort the indice get from the frame
    def parse_indice(indice):
        if indice.startswith("A"): # Potentiometer
            return ("A", int(indice[1:]))
        else: # Button
            return ("D", int(indice))

    parsed = [parse_indice(indice) for indice in device_indices]
    if option == Text.LANGUAGES[Text.LANGUAGE]["Sort"] + " " + Text.LANGUAGES[Text.LANGUAGE]["Sort N"]:
        parsed.sort(key=lambda x: (x[0], x[1]))
    elif option == Text.LANGUAGES[Text.LANGUAGE]["Sort Type"] + " " + Text.LANGUAGES[Text.LANGUAGE]["Sort B/P"]:
        parsed.sort(key=lambda x: (0 if x[0] == "D" else 1, x[1]))
    elif option == Text.LANGUAGES[Text.LANGUAGE]["Sort Type"] + " " + Text.LANGUAGES[Text.LANGUAGE]["Sort P/B"]:
        parsed.sort(key=lambda x: (0 if x[0] == "A" else 1, x[1]))
    device_indices = [f"{'A' if type == 'A' else ''}{number}" for type, number in parsed]

    # Rebuild the frames sorted
    for indice in device_indices:
        if indice.__contains__("A"):
            device.add_device(window, scrollable_frame, indice, 1, "Potentiometer")
        else:
            device.add_device(window, scrollable_frame, indice, 1, "Button")