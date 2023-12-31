import os
import shutil
from moviepy.editor import VideoFileClip

def check_and_move_corrupted_videos(folder_path, corrupt_folder_name):
    # Create "corrupt" folder if it doesn't exist
    corrupt_folder_path = os.path.join(folder_path, corrupt_folder_name)
    if not os.path.exists(corrupt_folder_path):
        os.makedirs(corrupt_folder_path)

    # Iterate through the files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if the file is a video with the ".mp4" extension
        if os.path.isfile(file_path) and filename.lower().endswith('.mp4'):

            # Try opening the video file
            try:
                clip = VideoFileClip(file_path)
                # Check if the video duration is valid
                if clip.duration != 0:
                    print(f"Valid video: {filename}")
                else:
                    print(f"Corrupted video: {filename}")
                    # Move the corrupted video to the "corrupt" folder
                    new_file_path = os.path.join(corrupt_folder_path, filename)
                    shutil.move(file_path, new_file_path)
                    print(f"Moved {filename} to {corrupt_folder_name} folder.")
                clip.close()
            except Exception as e:
                print(f"Corrupted video: {filename}")
                # Move the corrupted video to the "corrupt" folder
                new_file_path = os.path.join(corrupt_folder_path, filename)
                shutil.move(file_path, new_file_path)
                print(f"Moved {filename} to {corrupt_folder_name} folder.")
                print(f"Error: {str(e)}")

# Example usage
folder_path = r"C:\Users\adity\Music\hello\p1output"
corrupt_folder_name = "corrupt"
check_and_move_corrupted_videos(folder_path, corrupt_folder_name)
