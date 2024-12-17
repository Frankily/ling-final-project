import subprocess

file_names = ['base', 'finetuned', 'finetuned_all', 'base_prompt']
annotations = ['0', '1', 'combined']

num_scores = 0
print("starting scores")
with open('results.txt', 'a') as file:
    for name in file_names:
        for ann in annotations:
            file.write(f"{name} model and {ann} annotation results:\n")
            # Run the script with subprocess
            result = subprocess.run(
                ['python3', 'scripts/m2scorer.py', f'evaluate_files/{name}.txt', f'noalt/official.{ann}.m2'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            # Write the output to the file
            file.write(result.stdout)
            if result.stderr:  # Log errors if there are any
                file.write("\n[ERROR]\n")
                file.write(result.stderr)
            file.write("\n=====================\n")
            num_scores += 1
            print(num_scores)