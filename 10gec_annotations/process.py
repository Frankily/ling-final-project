import os
import csv

def parse_m2_file_to_csv(m2_file_path, csv_file_path):
    """
    Parse an .m2 file and generate a CSV file with columns: source, target, annotation.
    """
    rows = []
    
    with open(m2_file_path, 'r', encoding='utf-8') as file:
        source = ""
        annotations = []
        
        for line in file:
            line = line.strip()
            
            if line.startswith("S"):
                # New sentence, process the previous one if exists
                if source:
                    if annotations:
                        target = apply_corrections(source, annotations)
                        annotation_str = "; ".join(annotations)
                    else:
                        target = source
                        annotation_str = "NONE"
                    rows.append([source, target, annotation_str])
                
                # Set the new source sentence
                source = line[2:]
                annotations = []

            elif line.startswith("A"):
                # Collect annotation
                annotations.append(line)

        # Process the last sentence
        if source:
            if annotations:
                target = apply_corrections(source, annotations)
                annotation_str = "; ".join(annotations)
            else:
                target = source
                annotation_str = "NONE"
            rows.append([source, target, annotation_str])

    # Write to CSV
    with open(csv_file_path, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["source", "target", "annotation"])
        writer.writerows(rows)

def apply_corrections(sentence, annotations):
    """
    Apply corrections to a sentence based on the provided annotations.
    """
    tokens = sentence.split()
    for annotation in annotations:
        parts = annotation.split("|||")
        token_span = list(map(int, parts[0].split()[1:]))
        replacement = parts[2]
        if token_span:
            tokens[token_span[0]:token_span[1]] = [replacement] if replacement else []
    return " ".join(tokens)

def process_m2_folder(folder_path):
    """
    Process all .m2 files in a folder, generating a corresponding CSV file for each.
    """
    for filename in os.listdir(folder_path):
        if filename.endswith(".m2"):
            m2_file_path = os.path.join(folder_path, filename)
            csv_file_path = os.path.splitext(m2_file_path)[0] + ".csv"
            parse_m2_file_to_csv(m2_file_path, csv_file_path)
            print(f"Processed: {m2_file_path} -> {csv_file_path}")

# Specify the folder containing the .m2 files
folder_path = os.getcwd()  # Adjust the folder path as needed
process_m2_folder(folder_path)
