import os
import shutil
from moviepy.editor import VideoFileClip

# Specify the path of the folder containing the videos
folder_path = r"C:\Users\adity\Music\hello\output720p"

# Create a list of all video files in the folder
video_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Create a function to get the duration of a video in seconds
def get_video_duration(file_path):
    clip = VideoFileClip(file_path)
    return int(clip.duration)

# Iterate over each video file
for video_file in video_files:
    # Get the full path of the current video file
    video_file_path = os.path.join(folder_path, video_file)
    
    # Get the duration of the video in seconds
    duration = get_video_duration(video_file_path)
    
    # Create a folder based on the duration if it doesn't exist
    duration_folder = os.path.join(r"C:\Users\adity\Music\hello", f"{duration}secs")
    if not os.path.exists(duration_folder):
        os.makedirs(duration_folder)
    
    # Copy the video file to the corresponding duration folder
    destination_path = os.path.join(duration_folder, video_file)
    shutil.copy2(video_file_path, destination_path)
