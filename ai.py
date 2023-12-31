# Import necessary libraries
import cv2
from moviepy.editor import *

# Define the file paths
photo_path = r"C:\Users\adity\Downloads\8x - a sexy girl in pink wired bra with fair whiti (2).png"
voiceover_path = r"C:\Users\adity\Downloads\anan (enhanced).wav"
output_path = r"C:\Users\adity\Music\hello.mp4"

# Load the photo
photo = cv2.imread(photo_path)

# Resize the photo to match the desired video resolution
video_width = 1280
video_height = 720
resized_photo = cv2.resize(photo, (video_width, video_height))

# Create a blank video with the same resolution as the photo
video_duration = 10  # Duration of the video in seconds
video_fps = 30  # Frames per second
video = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*"mp4v"), video_fps, (video_width, video_height))

# Add the resized photo frames to the video
for _ in range(int(video_duration * video_fps)):
    video.write(resized_photo)

# Release the video object
video.release()

# Load the video with the resized photo
video_clip = VideoFileClip(output_path)

# Load the voiceover
voiceover_clip = AudioFileClip(voiceover_path)

# Set the voiceover duration to match the video duration
voiceover_duration = video_clip.duration
voiceover_clip = voiceover_clip.set_duration(voiceover_duration)

# Add the voiceover to the video
video_with_voiceover = video_clip.set_audio(voiceover_clip)

# Save the final video with the voiceover
video_with_voiceover.write_videofile(output_path, codec="libx264", audio_codec="aac")

# Clean up temporary files
video_clip.close()
