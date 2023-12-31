import os

def merge_text_files(folder_path, output_filename):
    # Get a list of all files in the specified folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith('.txt')]

    if not files:
        print("No text files found in the specified folder.")
        return

    # Sort the files for merging in alphabetical order
    files.sort()

    # Open the output file in 'append' mode to merge the content of all text files
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        for file in files:
            with open(os.path.join(folder_path, file), 'r', encoding='utf-8', errors='ignore') as input_file:
                output_file.write(input_file.read())

    print(f"All text files in '{folder_path}' merged into '{output_filename}'.")

if __name__ == "__main__":
    # Specify the folder path containing the text files and the output filename
    folder_path = r"C:\Users\adity\Downloads\allhere"
    output_filename = r"C:\Users\adity\Downloads\allherea\merged.txt"

    merge_text_files(folder_path, output_filename)
