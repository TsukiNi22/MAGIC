"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

 ██╗  ██╗ █████╗ ██████╗ ████████╗ █████╗ ███╗   ██╗██╗ █████╗ 
 ╚██╗██╔╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗████╗  ██║██║██╔══██╗
  ╚███╔╝ ███████║██████╔╝   ██║   ███████║██╔██╗ ██║██║███████║
  ██╔██╗ ██╔══██║██╔══██╗   ██║   ██╔══██║██║╚██╗██║██║██╔══██║
 ██╔╝ ██╗██║  ██║██║  ██║   ██║   ██║  ██║██║ ╚████║██║██║  ██║
 ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝

Edition:
##  09/09/2025 by Tsukini

File Name:
##  card_interaction.py

File Description:
##  Class with method to interact with the arduino card
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
# Import that can't be in the try
from src.const import Error, Return, Math, Text, Board
from sys import exit

# Import that can be checked
try:
    import customtkinter as ctk # Used for the graphics interface / GUI
    from window_build import device # Build of the window items
    from tool.reset_card import reset_card # Use to initialise/reset the card connection
    from Class.loading import LoadingOverlay # Used to display the loading frame
    from Class.popup import Popup # Used to display information
    from subprocess import run, CalledProcessError # USed to upload the program on the card
    from threading import Thread # to run the reading of the port in a thread
    from serial import Serial, serialutil  # Used to interact with the arduino
    from tkinter import TclError # Error handling
    from time import sleep # Used to wait
except ImportError as e:
    print(f"Import Error: {e}")
    exit(Error.FATAL_ERROR)

""" Class """
class Card:
    """
        Class to interact with the arduino card
    """

    def __init__(self, window, scrollable_frame):
        """
            Initialisation of the class
            :param window: Main program window
            :param scrollable_frame: The scrollable frame used to display the device frames
        """
        # Global var
        self.port = "COM3" # Port name
        self.serial_port = None # Connection to the port
        self.running = False # Is the thread running
        self.thread = None # The thread to read the port
        self.thread_status = Return.OK # The thread status
        self.window = window # Main window
        self.scrollable_frame = scrollable_frame # Frame parent of the device frames

        # Pins data
        self.values_memory = {} # Store the values {index: value}

    def serial_port_open(self, port):
        """
            Open the serial port of the card
            :param port: Serial port to connect to
        """
        # Open the serial port
        self.values_memory = {}
        try:
            self.serial_port = Serial(
                port=port,  # Port value
                baudrate=38400, # Comunication speed
                timeout=1  # Timout of the connection
            )
            self.port = port
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
            :param indice: Index of the device frame
            :param value: New value of the device frame
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

        # Update the text found or create it
        if found and label:
            if indice.__contains__("A"):
                label.configure(text=f"{round(((value - Math.POTENTIOMETER_CORRECTIF) * 100) / 1023)}%")
            else:
                label.configure(text=("High" if value == 1 else "Low"))
        else:
            if indice.__contains__("A"):
                device.add_device(self.window, self.scrollable_frame, indice, value, "Potentiometer")
            else:
                device.add_device(self.window, self.scrollable_frame, indice, value, "Button")

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
                        # Debug line
                        print("Arduino: '" + line + "' -> ", self.values_memory)
                        try:
                            line_splited = line.split(":")
                            value = int(line_splited[1])
                            self.values_memory[line_splited[0]] = value
                            self.update_value_display(line_splited[0], value)
                        except Exception as e:
                            print(f"Serial port, line: '{line}', error: {e}")

        except serialutil.SerialException as e:
            print(f"Serial port reading error: {e}")
            self.thread_status = Error.ACTION_ERROR

        except TclError as e:
            print(f"Update device frame error: {e}")
            self.thread_status = Error.ACTION_ERROR

        finally:
            self.running = False
            self.values_memory = {}
            try:
                if self.serial_port.is_open:
                    self.serial_port.close()
            except Exception as e:
                pass

    def serial_port_close(self):
        """
            Close the port of the card
        """
        # Try to reset the device frame
        for frame in self.scrollable_frame.winfo_children():
            try:
                frame.destroy()
            except Exception as e:
                pass

        # Try to close the port
        try:
            if self.serial_port.is_open:
                self.serial_port.close()
        except serialutil.SerialException as e:
            print(f"Serial port deconnection error: {e}")
            return Error.ACTION_ERROR
        return Return.OK

    def upload_program(self, window, card_name):
        """
            Upload the program to the given card
            :param window: Main program window
            :param card_name: Name of the card
        """
        # Setup the loading overlay
        loading = LoadingOverlay(window, Text.LANGUAGES[Text.LANGUAGE]["Upload Loading"])
        loading.start()

        # Close the port if it's open
        if self.running:
            self.stop_serial_port_read()
            # Wait for the end of the ancient port
            while self.running or self.serial_port.is_open:
                sleep(.1)
        self.serial_port_close()
        window.update()

        # Get the card name for the command
        fqbn = Board.BOARDS[card_name]
        try:
            # Compilation
            compile_cmd = [Board.ARDUINO_CLI, "compile", "--fqbn", fqbn, Board.PROGRAM_FILE]
            run(compile_cmd, check=True, capture_output=True, text=True)

            # Upload
            upload_cmd = [Board.ARDUINO_CLI, "upload", "-p", self.port, "--fqbn", fqbn, Board.PROGRAM_FILE]
            run(upload_cmd, check=True, capture_output=True, text=True)

            Popup("Information", Text.LANGUAGES[Text.LANGUAGE]["Upload Success"].replace("CARD", card_name), ("Ok",))
        except CalledProcessError as e:
            Popup("Error", e.stderr, ("Ok",))

        # Stop the loading overlay
        loading.stop()

        # Reset the port
        reset_card(window, self.scrollable_frame, self, port=self.port)