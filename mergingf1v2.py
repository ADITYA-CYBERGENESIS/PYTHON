import os
from moviepy.editor import *

folder_p11 = r"C:\Users\adity\Music\hello\p11"
video_PPI_path = r"C:\Users\adity\Music\hello\PPI.mp4"
output_directory = r"C:\Users\adity\Music\hello\p11full"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

video_PPI = VideoFileClip(video_PPI_path)

videos_not_merged = []  # List to store names and paths of videos that could not be merged

video_files = [name for name in os.listdir(folder_p11) if name.endswith(".mp4")]
num_videos_total = len(video_files)
num_videos_processed = 0

for video_file in video_files:
    if video_file.endswith(".mp4"):
        video_path = os.path.join(folder_p11, video_file)
        output_filename = "merged_" + video_file
        output_path = os.path.join(output_directory, output_filename)

        try:
            # Load the 1080p video
            video_1080p = VideoFileClip(video_path)

            # Combine video and audio of 1080p video and PPI video
            final_video = concatenate_videoclips([video_1080p, video_PPI])
            final_video = final_video.set_audio(final_video.audio)

            # Write the merged video with original audio
            final_video.write_videofile(
                output_path,
                codec="libx264",
                audio_codec="aac",
                temp_audiofile="temp-audio.m4a",
                remove_temp=True,
                fps=video_1080p.fps,  # Use the same FPS as the input video
                preset="ultrafast"  # Use a fast encoding preset
            )

            # Clear the loaded video clips from memory
            final_video.close()

            num_videos_processed += 1
            num_videos_remaining = num_videos_total - num_videos_processed
            print(f"Successfully merged video {num_videos_processed} of {num_videos_total}. {num_videos_remaining} videos remaining.")

        except Exception as e:
            videos_not_merged.append((video_file, video_path))
            print(f"Error occurred while merging {video_file}: {str(e)}")

        # Clear the loaded video clip from memory
        video_1080p.close()

# Clear the loaded PPI video from memory
video_PPI.close()

# Print the names and paths of videos that could not be merged
print("Videos that could not be merged:")
for video in videos_not_merged:
    print(f"Name: {video[0]}, Path: {video[1]}")
