import os
import requests
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor

# Define the input file path
input_file_path = r'C:\Users\adity\Music\hello\input.txt'

# Define the output folder path
output_folder_path = r'C:\Users\adity\Music\hello\reel output'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Read the links from the input file
with open(input_file_path, 'r') as file:
    links = file.readlines()

def download_video(link):
    try:
        link = link.strip()  # Remove any leading/trailing whitespace or newlines
        video_id = urlparse(link).path.split('/')[-1]  # Extract the video ID from the URL

        # Generate a unique filename based on the video ID
        filename = os.path.join(output_folder_path, f'{video_id}.mp4')

        # Download the video using the link
        response = requests.get(link, stream=True)
        response.raise_for_status()

        with open(filename, 'wb') as video_file:
            for chunk in response.iter_content(chunk_size=4096):
                video_file.write(chunk)

        return f"Video downloaded: {filename}"
    except Exception as e:
        return f"Error downloading video from {link}: {e}"

# Create a ThreadPoolExecutor with a maximum of 5 worker threads
with ThreadPoolExecutor(max_workers=5) as executor:
    # Submit the download tasks to the executor
    download_tasks = [executor.submit(download_video, link) for link in links]

    # Process the completed download tasks
    for task in download_tasks:
        result = task.result()
        print(result)
