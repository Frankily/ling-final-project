import csv
import errant

# Function to generate the M2 file
def generate_m2_file(csv_file, output_m2_file):
    # Load the errant annotator
    annotator = errant.load("en")

    # Open the CSV file
    with open(csv_file, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        
        # Open the output M2 file
        with open(output_m2_file, "w", encoding="utf-8") as m2file:
            for row in reader:
                # Get source and target sentences
                source = row["Before Statements"]
                target = row["After Statements"]

                # Tokenize the source and target sentences
                src_tokens = annotator.parse(source)
                tgt_tokens = annotator.parse(target)

                # Align the source and target sentences and extract edits
                edits = annotator.annotate(src_tokens, tgt_tokens)

                # Write the source sentence to the M2 file
                m2file.write(f"S {source.strip()}\n")

                # Write each edit to the M2 file in the required format
                for edit in edits:
                    # Extract necessary details from the edit
                    o_start, o_end = edit.o_start, edit.o_end
                    correction = " ".join([token.text for token in edit.c_toks]) if edit.c_toks else ""
                    edit_type = edit.type

                    # Format the edit line according to the M2 format
                    m2file.write(f"A {o_start} {o_end}|||{edit_type}|||{correction}|||REQUIRED|||-NONE-|||0\n")

                # Write a newline after each sentence pair
                m2file.write("\n")

if __name__ == "__main__":
    # Specify the input CSV file and output M2 file
    input_csv = "examples_a4.csv"  # Replace with your CSV file name
    output_m2 = "output.m2"  # Desired output M2 file name

    # Generate the M2 file
    generate_m2_file(input_csv, output_m2)
    print(f"M2 file has been generated: {output_m2}")
