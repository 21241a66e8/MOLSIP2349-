def count_words_characters(file_p):
    with open(file_p, 'r') as file:
        text = file.read()
        word_count = len(text.split())
        character_count = len(text)
        line_count = text.count('\n') + 1  # Adding 1 to count the last line without newline

    return {
        'Word count': word_count,
        'Character count': character_count,
        'Line count': line_count
    }

# Example usage
file_p = 'C:\Users\sathw\Desktop\MicroOrbitalLabs'  # Replace this with your file path

result = count_words_characters(file_p)
for key, value in result.items():
    print(f'{key}: {value}')