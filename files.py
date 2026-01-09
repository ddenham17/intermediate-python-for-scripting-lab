word_count = count_words_in_file("sample.txt")

def count_words_in_file(file_path):
    """
    Reads a text file and returns the total number of words.
    Handles FileNotFoundError if the file does not exist.
    """
    try:
        # Use 'with' to ensure the file is properly closed after reading
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # .split() splits by any whitespace (spaces, tabs, newlines)
            words = content.split()
            return len(words)
            
    except FileNotFoundError:
        print(f"Error! The file at '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred! {e}")
        return None
    
if word_count is not None:
     print(f"Total words: {word_count}")
else:
    print("File not found!")

# Example Usage:
# word_count = count_words_in_file("sample.txt")
# if word_count is not None:
#     print(f"Total words: {word_count}")