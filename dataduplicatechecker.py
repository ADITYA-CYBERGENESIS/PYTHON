import csv

def count_occurrences(csv_file):
    occurrences = {}
    duplicates = set()
    
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Store the header
        value_index = 1  # Assuming the second column contains the values
        
        for row in reader:
            value = row[value_index].strip()
            if value in occurrences:
                duplicates.add(value)
            occurrences[value] = row
    
    return occurrences, duplicates, header

def write_modified_data(original_csv, output_csv, occurrences, duplicates, header):
    rows_deleted = 0
    
    with open(original_csv, 'r', encoding='utf-8') as infile, open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        writer.writerow(header)  # Write the header to the new file
        
        for row in reader:
            value = row[1].strip()  # Assuming the second column contains the values
            if value in duplicates:
                # If value is a duplicate, skip writing this row and count it as deleted
                rows_deleted += 1
                continue
            
            # Otherwise, write the row to the new file
            writer.writerow(row)

    return rows_deleted

if __name__ == "__main__":
    csv_file_path = r"C:\Users\adity\OneDrive\Desktop\TeleGram-Scraper-master\members.csv"
    output_csv_path = r"C:\Users\adity\OneDrive\Desktop\TeleGram-Scraper-master\k3.csv"
    
    occurrences, duplicates, header = count_occurrences(csv_file_path)
    rows_deleted = write_modified_data(csv_file_path, output_csv_path, occurrences, duplicates, header)
    
    print(f"Number of rows deleted: {rows_deleted}")
