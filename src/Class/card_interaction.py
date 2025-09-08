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
##  card_interaction.py

File Description:
##  Class with method to interact with the arduino card
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
# Import that can't be in the try
from src.const import Error, Return, Math
from sys import exit

# Import that can be checked
try:
    import customtkinter as ctk # Used for the graphics interface / GUI
    from window_build import device # Build of the window items
    from threading import Thread # to run the reading of the port in a thread
    from serial import Serial, serialutil  # Used to interact with the arduino
except ImportError as e:
    print(f"Import Error: {e}")
    exit(Error.FATAL_ERROR)

""" Class """
class Card:
    """
        Class to interact with the arduino card
    """

    def __init__(self, scrollable_frame):
        """
            Initialisation of the class
        """
        # Global var
        self.serial_port = None # Connection to the port
        self.running = False # Is the thread running
        self.thread = None # The thread to read the port
        self.thread_status = Return.OK # The thread status
        self.scrollable_frame = scrollable_frame # Frame parent of the device frames

        # Pins data
        self.end_init = False # If the card initialisation is finish
        self.values_memory = {} # Store the values {index: value}

    def serial_port_open(self):
        """
            Open the serial port of the card
        """
        # Open the serial port
        self.end_init = False
        try:
            self.serial_port = Serial(
                port="COM3",  # Default windows port
                baudrate=38400, # Comunication speed
                timeout=1  # Timout of the connection
            )
        except serialutil.SerialException as e:
            print(f"Serial port connection error: {e}")
            return Error.ACTION_ERROR
        return Return.OK

    def start_serial_port_read(self):
        """
            Start the serial port reading
        """
        if not self.running:
            self.running = True
            self.thread_status = Return.OK
            self.thread = Thread(target=self.serial_port_read, daemon=True)
            self.thread.start()

    def stop_serial_port_read(self):
        """
            Stop the serial port reading
        """
        if self.running:
            self.running = False
            self.thread.join(timeout=1)
            self.serial_port.close()

    def update_value_display(self, indice, value):
        """
            Update the value display of the device frames
        """
        found = False
        label = None
        for frame in self.scrollable_frame.winfo_children():
            for widget in frame.winfo_children():
                if not isinstance(widget, ctk.CTkLabel):
                    continue
                text = widget.cget("text")
                if text.__contains__("n°" + indice):
                    found = True
                elif text != "":
                    label = widget
            if found and label:
                break

        if found and label:
            if indice.__contains__("A"):
                label.configure(text=f"{round(((value - Math.POTENTIOMETER_CORRECTIF) * 100) / 1023)}%")
            else:
                label.configure(text=("High" if value == 1 else "Low"))
        else:
            if indice.__contains__("A"):
                device.add_device(self.scrollable_frame, indice, value, "Potentiometer")
            else:
                device.add_device(self.scrollable_frame, indice, value, "Button")

    def serial_port_read(self):
        """
            Read the serial port of the card
        """
        try:
            while self.running and self.serial_port.is_open:
                if self.serial_port.in_waiting > 0:  # If there is data to read
                    # Get the line
                    line = self.serial_port.readline().decode(errors='ignore').strip()

                    # Dispatch the line
                    if line:
                        if line == "[Start Void Setup]": # Start of the program setup or reset
                            self.end_init = False
                            self.values_memory = {}

                        elif self.end_init: # Line of data 'index:value'
                            line_splited = line.split(":")
                            value = int(line_splited[1])
                            self.values_memory[line_splited[0]] = value
                            self.update_value_display(line_splited[0], value)

                        elif line == "[End Void Setup]": # End of the program setup
                            self.end_init = True
                        # Debug line
                        print("Arduino: '" + line + "' -> ", self.values_memory)
        except serialutil.SerialException as e:
            print(f"Serial port reading error: {e}")
            self.thread_status = Error.ACTION_ERROR
        finally:
            if self.serial_port.is_open:
                self.serial_port.close()

    def serial_port_close(self):
        """
            Close the port of the card
        """
        try:
            if self.serial_port.is_open:
                self.serial_port.close()
        except serialutil.SerialException as e:
            print(f"Serial port connection error: {e}")
            return Error.ACTION_ERROR
        return Return.OK
