import subprocess
import errant

def compare_m2_files(hyp_file, ref_file, output_file, category=None, detection_span=False):
    """
    Compare two M2 files using errant_compare.
    
    :param hyp_file: Path to the hypothesis M2 file.
    :param ref_file: Path to the reference M2 file.
    :param output_file: File to store the comparison results.
    :param category: Error category granularity (1, 2, or 3).
    :param detection_span: Evaluate span-based detection instead of correction.
    """
    # Base command
    command = ["errant_compare", "-hyp", hyp_file, "-ref", ref_file]
    
    # Add category flag if provided
    if category:
        command += ["-cat", str(category)]
    
    # Add detection span flag if specified
    if detection_span:
        command.append("-ds")
    
    # Run the command and capture output
    try:
        with open(output_file, "w") as output:
            subprocess.run(command, stdout=output, stderr=subprocess.PIPE, check=True)
        print(f"Comparison results saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error running errant_compare: {e.stderr.decode()}")

if __name__ == "__main__":
    # Paths to the M2 files
    hyp_file = "output.m2"  # Replace with the path to your hypothesis M2 file
    ref_file = "ABC.train.gold.bea19.m2"  # Replace with the path to your reference M2 file
    output_file = "comparison_results.txt"  # File to save the comparison results

    # Example usage
    compare_m2_files(hyp_file, ref_file, output_file, category=2, detection_span=True)
