import os
import shutil

def convert_files_to_txt(input_folder_path, output_folder_path):
    # Check if the provided input folder path exists
    if not os.path.exists(input_folder_path):
        print(f"The input folder path '{input_folder_path}' does not exist.")
        return

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder_path, exist_ok=True)

    for root, _, files in os.walk(input_folder_path):
        for file_name in files:
            input_file_path = os.path.join(root, file_name)

            # Change the extension of the file to '.txt'
            new_file_name = os.path.splitext(file_name)[0] + ".txt"
            output_file_path = os.path.join(output_folder_path, new_file_name)

            try:
                # Copy the file to the output folder with the new name
                shutil.copy(input_file_path, output_file_path)
                print(f"Converted '{input_file_path}' to '{output_file_path}'")
            except Exception as e:
                print(f"Error converting '{input_file_path}': {e}")

if __name__ == "__main__":
    input_folder_path = r"C:\Users\adity\Downloads\allherea"  # Replace with the actual input folder path
    output_folder_path =   r"C:\Users\adity\Downloads\allhere" # Replace with the desired output folder path

    convert_files_to_txt(input_folder_path, output_folder_path)
