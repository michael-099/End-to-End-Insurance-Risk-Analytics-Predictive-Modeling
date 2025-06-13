import os

def txt_to_csv(path_to_txt_file, output_file=None):
    
    if output_file is None:
        output_file = path_to_txt_file.replace(".txt", ".csv")

    if not os.path.exists(output_file):
        with open(path_to_txt_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
            for line in infile:
                line = line.strip()
                if line:
                    csv_line = line.replace("|", ",")
                    outfile.write(csv_line + "\n")
        print(f"✅ '{output_file}' created successfully.")
    else:
        print(f"⚠️ File '{output_file}' already exists. No changes made.")
