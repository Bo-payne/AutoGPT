import os
import csv

# Define the directory to scan
directory = "C:/Users/bomac"

# Define the output CSV file
output_csv = "enhanced_file_list_V1.02.csv"

# Open the CSV file for writing
with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write the CSV header
    writer.writerow(["Type", "FullName", "Name", "Length", "LastWriteTime", 
                     "Function of Code", "Code Snip"])
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for name in files:
            if name.endswith('.py'):
                full_path = os.path.join(root, name)
                try:
                    with open(full_path, 'r', encoding='utf-8') as code_file:
                        lines = code_file.readlines()
                        function_lines = [line for line in lines if line.strip().startswith("def")]
                        if function_lines:
                            function_of_code = function_lines[0].strip()
                            code_snip = ''.join(function_lines[0:5])
                            writer.writerow(["File", full_path, name,
                                             os.path.getsize(full_path),
                                             os.path.getmtime(full_path),
                                             function_of_code,
                                             code_snip])
                except Exception as e:
                    print(f"Error processing file {full_path}: {e}")

        for dir_name in dirs:
            dir_full_path = os.path.join(root, dir_name)
            writer.writerow(["Folder", dir_full_path, "", "", "", "", ""])