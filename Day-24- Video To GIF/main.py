from moviepy import VideoFileClip

video = VideoFileClip(r"C:\Users\LENOVO\Downloads\vid.mp4").subclipped(0, 10)

video.write_gif("test1.gif", fps=10)