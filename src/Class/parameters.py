"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

 ██╗  ██╗ █████╗ ██████╗ ████████╗ █████╗ ███╗   ██╗██╗ █████╗ 
 ╚██╗██╔╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗████╗  ██║██║██╔══██╗
  ╚███╔╝ ███████║██████╔╝   ██║   ███████║██╔██╗ ██║██║███████║
  ██╔██╗ ██╔══██║██╔══██╗   ██║   ██╔══██║██║╚██╗██║██║██╔══██║
 ██╔╝ ██╗██║  ██║██║  ██║   ██║   ██║  ██║██║ ╚████║██║██║  ██║
 ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝

Edition:
##  10/09/2025 by Tsukini

File Name:
##  popup.py

File Description:
##  Class to handle the parameters.save file
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
# Import that can't be in the try
from src.const import Error
from sys import exit

# Import that can be checked
try:
    pass
except ImportError as e:
    print(f"Import Error: {e}")
    exit(Error.FATAL_ERROR)

""" Class """
class Parameters:
    """
        Class to handle the parameters edition/reading
    """

    def __init__(self):
        """
            Initialisation of the class
        """
        self.lignes = None
        pass

    def get_parameters(self):
        """
            Get the parameters content
        """
        with open("data\\parameters.save", "r", encoding="utf-8") as file:
            self.lignes = file.readlines()

    def save_parameters(self):
        """
            Save the parameters
        """
        if self.lignes is None:
            return
        with open("data\\parameters.save", "w", encoding="utf-8") as file:
            file.writelines(self.lignes)
        self.lignes = None

    def get_parameter(self, name):
        """
            Get the value of a parameter
        """
        self.get_parameters()
        for line in self.lignes:
            line_splited = line.split("=")
            if line_splited[0] == name:
                return line_splited[1]
        return None

    def set_parameter(self, name, value):
        """
            Change the value of a parameter
        """
        self.get_parameters()
        found = False
        for i in range(len(self.lignes)):
            if self.lignes[i].split("=")[0] == name:
                self.lignes[i] = f"{name}={value}"
                found = True
                break
        if not found:
            self.lignes.append(f"\n{name}={value}")
        self.save_parameters()
