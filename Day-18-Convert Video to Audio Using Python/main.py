from moviepy import VideoFileClip
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Hide main tkinter window
Tk().withdraw()

# Open file dialog
vid = askopenfilename(title="Select MP4 file", filetypes=[("MP4 files", "*.mp4")])

if vid:  # check if file selected
    video = VideoFileClip(vid)
    
    aud = video.audio
    aud.write_audiofile("demo.mp3")
    
    print("----Convert mp4 to mp3 successfully----")
else:
    print("No file selected")