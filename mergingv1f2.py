import os
import cv2
from moviepy.editor import *

folder_1080p = r"C:\Users\adity\Music\hello\1080p"
video_start1080_path = r"C:\Users\adity\Music\hello\start1080.mp4"
output_directory = r"C:\Users\adity\Music\hello\output1080pfull"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

video_start1080 = VideoFileClip(video_start1080_path)

videos_not_merged = []  # List to store names and paths of videos that could not be merged

for video_file in os.listdir(folder_1080p):
    if video_file.endswith(".mp4"):
        video_path = os.path.join(folder_1080p, video_file)
        output_filename = "merged_" + video_file
        output_path = os.path.join(output_directory, output_filename)

        try:
            # Load the start1080 video
            start1080_video = VideoFileClip(video_start1080_path)

            # Load the 1080p video
            video_1080p = VideoFileClip(video_path)

            # Combine video and audio of start1080 and 1080p videos
            final_video = concatenate_videoclips([start1080_video, video_1080p])
            final_video = final_video.set_audio(final_video.audio)

            # Write the merged video with original audio
            final_video.write_videofile(output_path, codec="libx264", audio_codec="aac", temp_audiofile="temp-audio.m4a", remove_temp=True)

            # Clear the loaded video clips from memory
            final_video.close()
            del final_video
        except Exception as e:
            videos_not_merged.append((video_file, video_path))
            print(f"Error occurred while merging {video_file}: {str(e)}")

        # Clear the loaded video clips from memory
        start1080_video.close()
        del start1080_video
        video_1080p.close()
        del video_1080p

# Clear the loaded start1080 video from memory
video_start1080.close()
del video_start1080

# Print the names and paths of videos that could not be merged
print("Videos that could not be merged:")
for video in videos_not_merged:
    print(f"Name: {video[0]}, Path: {video[1]}")
