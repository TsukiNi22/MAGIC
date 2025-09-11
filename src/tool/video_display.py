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
except ImportError as e:
    print(f"Import Error: {e}")
    exit(Error.FATAL_ERROR)

""" Program """
def video_display(parent, video_path):
    """
        Display a video in a frame
        :param parent: Parent window where the video will be displayed
        :param video_path: Path to the video file
    """

    # Create the frame that take the whole parent
    video_frame = ctk.CTkFrame(parent, bg_color="transparent", fg_color="transparent")
    video_frame.pack(fill="both", expand=True)

    # Create the video
    videoplayer = TkinterVideo(master=video_frame, scaled=True, background=Color.DARK_GREY)
    videoplayer.load(video_path)
    videoplayer.pack(expand=True, fill="both")

    # Bind the end of the video to the destroy of the video
    def on_end(event):
        video_frame.destroy()
    videoplayer.bind("<<Ended>>", on_end)

    # Start the video
    videoplayer.play()