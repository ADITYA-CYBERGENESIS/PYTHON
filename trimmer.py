import os
import subprocess
import shutil

input_folder = r'C:\Users\adity\Music\hello\pp1'
output_folder = r'C:\Users\adity\Music\hello\p1output'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

for file_name in os.listdir(input_folder):
    input_file_path = os.path.join(input_folder, file_name)
    if os.path.isfile(input_file_path):
        try:
            output_file_path = os.path.join(output_folder, file_name)
            cmd = f'ffmpeg -i "{input_file_path}" -ss 0 -t 3.5 -c:v copy -c:a copy "{output_file_path}"'
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while processing {input_file_path}: {e}")
        except Exception as e:
            print(f"Error occurred while processing {input_file_path}: {e}")

print("Videos trimmed and saved to", output_folder)
