# ling-final-project

requirements:
torch, errant, modal, nltk

Original data are in benchmark_data (CoNLL 2014 Shared Task), release3.3 (NUCLE dataset), and wi+locness(BEA Train dataset), folders. Scripts to retrieve these and several other datasets are found in get_data_scripts. Training data csv files with columns 'Before Statements' with errors, "After Statements" with corrections, and "Error Correction" with a list of edits, are found in the csv_data folder. Data formatted in a jsonl for finetuning can be found in llm-finetuning/data. 

Finetuning scripts on the NousResearch/Meta-Llama-3-8B-Instruct pretrained model with Modal can be found in llm-finetuning. An example finetuning command-line script with modal is 'modal run --detach src.train --config=config/llama-3-instruct_2.yml --data=data/cleaned_data.jsonl' (cleaned_data.jsonl can be created with data scripts described above, but could not be added here due to size of dataset). Deploying the model for inference can be done with 'modal deploy src.inference'.

Generated outputs are in the generated_outputs and evalute_files subdirectories of the inference_results and m2scorer folders. One can perform inference with modal deployed model with the get_outputs.py script in inference_results. parse_output.ipynb parses the outputs in the text and m2 format for evaluation. One can run errant on the files in inference_results and get_scores.py in m2scorer to attain evaluation metrics. Our results can be found in results.txt in inference_results and m2scorer for the errant and m2 evaluations, respectively.