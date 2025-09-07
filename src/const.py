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
##  const.py

File Description:
##  Constants of the project
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Return:
    """
    Return values, more details for the values in the original file
    """
    OK = 0 # Return value upon success on a call function
    KO = 1 # Return value upon fail on a call function

class Error:
    """
    Error values, more details for the values in the original file
    """
    FATAL_ERROR = 0b1000 # Global error, the program whole execution won't be able to run after this        (100% execution stop)
    LOCAL_ERROR = 0b100 # Local error, the program local execution won't probably be able to run after this (some chance of execution stop)
    ACTION_ERROR = 0b10 # Same~~ as Return.KO, a program action execution won't be able to run after this   (low chance of execution stop)

class Window:
    WIDTH = 500 # X size of the window
    HEIGHT = 500 # Y size of the window
