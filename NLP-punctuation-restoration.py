from deepmultilingualpunctuation import PunctuationModel


def capitalize_sentences(text):
    """
    Capitalizes the first word of every sentence in the text.

    Args:
        text (str): Text with sentences to capitalize.

    Returns:
        str: Text with each sentence's first word capitalized.
    """
    sentences = text.split('. ')
    capitalized_sentences = [
        sentence[0].capitalize() + sentence[1:] if sentence else sentence
        for sentence in sentences
    ]
    return '. '.join(capitalized_sentences)


def process_text(input_file, output_file):
    """
    Reads text from a file, restores punctuation, capitalizes sentences,
    and writes the result to an output file.

    Args:
        input_file (str): Path to the input text file.
        output_file (str): Path to the output text file.
    """
    # Initialize the punctuation restoration model
    model = PunctuationModel()

    # Read the input text from the file
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Restore punctuation
    punctuated_text = model.restore_punctuation(text)

    # Capitalize the first word of each sentence
    formatted_text = capitalize_sentences(punctuated_text)

    # Write the output to a new file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(formatted_text)


if __name__ == "__main__":
    # File paths
    input_file = r"C:\Users\guophie\Downloads\sample.txt"
    output_file = r"C:\Users\guophie\Downloads\sample-edited.txt"

    # Process the text
    process_text(input_file, output_file)
    print(f"Processed text saved to: {output_file}")
