import gzip
import shutil
import os

def compress_file(input_file_path, output_file_path, target_size):
    compress_level = 1  # Starting compression level (1 to 9, where 1 is the fastest but least compression)
    while True:
        with open(input_file_path, 'rb') as file_in:
            with gzip.open(output_file_path, 'wb', compresslevel=compress_level) as file_out:
                shutil.copyfileobj(file_in, file_out)
        compressed_size = os.path.getsize(output_file_path)
        if compressed_size < target_size:
            break
        compress_level += 1
        if compress_level > 9:
            print("Target size not achievable. Compressed file is still larger than the target.")
            break

if __name__ == "__main__":
    
    input_file_path = r"C:\Users\adity\Downloads\ython\output_compresed.txt"
    output_file_path = r"C:\Users\adity\Downloads\ython\output_compressed.txt"
    target_size_in_mb = 2
    target_size_mb = 2

    target_size_bytes = target_size_mb * 1024 * 1024
    compress_file(input_file, output_file, target_size_bytes)

    # Rename the compressed file to have .txt extension
    compressed_txt_file = output_file[:-3]  # Remove the .gz extension
    compressed_txt_file += ".txt"
    shutil.move(output_file, compressed_txt_file)

    print(f"Compression complete. Compressed file saved as: {compressed_txt_file}")