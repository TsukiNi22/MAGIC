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
import serial

""" Import """
# Import that can't be in the try
from src.const import Error, Return
from sys import exit

# Import that can be checked
try:
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

    def __init__(self):
        """
            Initialisation of the class
        """
        # Global var
        self.serial_port = None # Connection to the port
        self.running = False # Is the thread running
        self.thread = None # The thread to read the port
        self.thread_status = Return.OK # The thread status

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
        self.running = False
        if self.thread:
            self.thread.join(timeout=1)
        if self.serial_port.is_open:
            self.serial_port.close()

    def serial_port_read(self) :
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
                            self.values_memory[line_splited[0]] = int(line_splited[1])
                        elif line == "[End Void Setup]": # End of the program setup
                            self.end_init = True
                        print("Arduino: '" + line + "' -> ", self.values_memory)
        except serial.SerialException as e:
            print(f"Serial port reading error: {e}")
            self.thread_status = Error.ACTION_ERROR
        finally:
            if self.serial_port.is_open:
                self.serial_port.close()

    def serial_port_close(self):
        """
            Close the port of the card
        """
        self.serial_port.close()
