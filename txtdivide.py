import os

def split_file(input_file, output_folder, num_files=10):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            content = infile.readlines()

        lines_per_file = len(content) // num_files
        remainder = len(content) % num_files

        start = 0
        for i in range(num_files):
            end = start + lines_per_file + (1 if i < remainder else 0)
            output_file = os.path.join(output_folder, f"part{i+1}.txt")
            with open(output_file, 'w', encoding='utf-8') as outfile:
                outfile.writelines(content[start:end])
            start = end

        print(f"{num_files} files created successfully in {output_folder}.")
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    input_file_path = r"C:\Users\adity\Downloads\allherea\merged.txt"
    output_folder_path = r"C:\Users\adity\Downloads\allhere"
    num_files_to_create = 10

    split_file(input_file_path, output_folder_path, num_files_to_create)
