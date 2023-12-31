import os

folder_path = r'C:\Users\adity\Music\hello\g1'
output_file = r'C:\Users\adity\Music\hello\input.txt'

with open(output_file, 'w') as file:
    for filename in os.listdir(folder_path):
        if filename.endswith('.mp4'):
            file.write(f"file '{os.path.join(folder_path, filename)}'\n")

