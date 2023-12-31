from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
import os
import subprocess

g1_folder = r"C:\Users\adity\Music\hello\g1"
s1_video = r"C:\Users\adity\Music\hello\s1.mp4"
output_directory = r"C:\Users\adity\Music\hello\output"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for video_file in os.listdir(g1_folder):
    if video_file.endswith(".mp4"):
        video_path = os.path.join(g1_folder, video_file)
        output_path = os.path.join(output_directory, "merged_" + video_file)
        
        video_g1 = VideoFileClip(video_path)
        video_s1 = VideoFileClip(s1_video)
        
        final_video = concatenate_videoclips([video_g1, video_s1])
        final_video.write_videofile(output_path, codec="libx264", audio_codec="aac", temp_audiofile="temp-audio.m4a", remove_temp=True)

# Shutdown the computer after the task is done
subprocess.call(["shutdown", "-s", "-t", "0"])
