import subprocess

input_file = r'C:\Users\adity\Music\hello\input.txt'
video_file = r'C:\Users\adity\Music\hello\s1.mp4'
output_directory = r'C:\Users\adity\Music\hello\output'

with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    line = line.strip()
    output_file = f'{output_directory}\\output_{i+1}.mp4'

    merge_command = (
        f'ffmpeg -i "{line}" -i "{video_file}" '
        f'-filter_complex "[0:v]scale=640:480[v0];[v0][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a];[a][1:a]amerge=inputs=2[a]" '
        f'-map "[v]" -map "[a]" -c:v libx264 -crf 23 -preset medium "{output_file}"'
    )

    subprocess.run(merge_command, shell=True, check=True)
