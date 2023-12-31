import os
import subprocess

folder_path = r'C:\Users\adity\Music\hello\badres'
output_folder_path = r'C:\Users\adity\Music\hello\p1output'
aspect_ratio = 9 / 16
target_width = 720
target_height = 1280

def check_video_aspect_ratio(video_path):
    try:
        cmd = ['ffprobe', '-v', 'error', '-show_entries', 'stream=width,height', '-of', 'csv=p=0', video_path]
        output = subprocess.check_output(cmd).decode('utf-8').strip()
        width, height = map(int, output.split(','))

        calculated_aspect_ratio = width / height
        
        if (
            calculated_aspect_ratio == aspect_ratio
            and width == target_width
            and height == target_height
        ):
            return True
        
        return False
    except Exception as e:
        print(f"Error checking video: {video_path}")
        print(str(e))
        return False

def resize_video(video_path, output_path):
    try:
        cmd = [
            'ffmpeg', '-i', video_path, '-vf', f'scale={target_width}:{target_height}:force_original_aspect_ratio=decrease', output_path
        ]
        subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        return True
    except Exception as e:
        print(f"Error resizing video: {video_path}")
        print(str(e))
        return False

# Create output folder if it doesn't exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Check if the file is a video file
    if os.path.isfile(file_path) and filename.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
        if check_video_aspect_ratio(file_path):
            print(f"{filename} meets the criteria")
        else:
            print(f"{filename} does not meet the criteria. Resizing...")
            output_filename = os.path.splitext(filename)[0] + '_resized.mp4'
            output_path = os.path.join(output_folder_path, output_filename)
            resize_video(file_path, output_path)
            print(f"Resized video saved as: {output_filename}")
