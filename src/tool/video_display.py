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
##  video_display.py

File Description:
##  Display a video in a frame
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
# Import that can't be in the try
from src.const import Error, Color
from sys import exit

# Import that can be checked
try:
    import customtkinter as ctk # Used for the graphics interface / GUI
    from tkVideoPlayer import TkinterVideo # Used to display video
    from tool.reset_card import reset_card # Use to initialise/reset the card connection
    from time import sleep # Used to wait
except ImportError as e:
    print(f"Import Error: {e}")
    exit(Error.FATAL_ERROR)

""" Program """
def video_display(parent, video_path, card=None):
    """
        Display a video in a frame
        :param parent: Parent window where the video will be displayed
        :param video_path: Path to the video file
        :param card: Information for the card reset when used
    """
    # Create the frame that take the whole parent
    video_frame = ctk.CTkFrame(parent, bg_color="transparent", fg_color="transparent")
    video_frame.pack(fill="both", expand=True)

    # Create the video
    videoplayer = TkinterVideo(master=video_frame, scaled=True, consistant_frame_rate=True, background="#202020")
    videoplayer.load(video_path)
    videoplayer.pack(expand=True, fill="both")

    # Bind the end of the video to the destroy of the video
    def on_end(event):
        video_frame.destroy()
        if card is not None:
            reset_card(card[0], card[1], card[2])
    videoplayer.bind("<<Ended>>", on_end)

    # Start the video
    videoplayer.play()