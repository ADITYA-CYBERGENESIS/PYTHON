import os
import subprocess
import shutil

folder_path = r'C:\Users\adity\Music\hello\NEWL'
resolution_720p = (720, 1280)
aspect_ratio_720p = 9 / 16
resolution_1080p = (1080, 1920)
aspect_ratio_1080p = 9 / 16
folder_720p = r'C:\Users\adity\Music\hello\720p'
folder_1080p = r'C:\Users\adity\Music\hello\1080p'
deleted_videos = 0

# Create the folders if they don't exist
os.makedirs(folder_720p, exist_ok=True)
os.makedirs(folder_1080p, exist_ok=True)

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        try:
            cmd = f'ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate -of csv=p=0 "{file_path}"'
            result = subprocess.check_output(cmd, shell=True, encoding='utf-8')
            width, height, frame_rate = result.strip().split(',')
            width = int(width)
            height = int(height)
            frame_rate = eval(frame_rate)
            aspect = width / height

            if (
                width == resolution_720p[0]
                and height == resolution_720p[1]
                and abs(aspect - aspect_ratio_720p) < 0.001
            ):
                # Move to 720p folder
                shutil.move(file_path, os.path.join(folder_720p, file_name))
            elif (
                width == resolution_1080p[0]
                and height == resolution_1080p[1]
                and abs(aspect - aspect_ratio_1080p) < 0.001
            ):
                # Move to 1080p folder
                shutil.move(file_path, os.path.join(folder_1080p, file_name))
            else:
                # Video doesn't match specified resolutions, leave it untouched
                pass

        except (subprocess.CalledProcessError, ValueError):
            pass

print("Videos moved to 720p folder")
print("Videos moved to 1080p folder")
