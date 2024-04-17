import os
import glob

def count_gpt_tokens(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Tokenize content based on your GPT tokenization method
        tokens = content.split()  # Example tokenization
        return len(tokens)

def main():
    # Get the current working directory
    cwd = os.getcwd()
    
    # List all text files in the current directory
    text_files = glob.glob(os.path.join(cwd, '*.txt'))
    
    if not text_files:
        print("No text files found in the current directory.")
        return
    
    print("Token counts for each text file:")
    for file_path in text_files:
        file_name = os.path.basename(file_path)
        token_count = count_gpt_tokens(file_path)
        print(f"{file_name}: {token_count} tokens")

if __name__ == "__main__":
    main()
