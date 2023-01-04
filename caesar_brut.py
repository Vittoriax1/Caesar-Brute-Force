import enchant

def caesar_brute_force(ciphertext):
    # Create a list to store the possible plaintexts
    plaintexts = []

    # Create a dictionary for English words
    dictionary = enchant.Dict("en_US")

    # Try all possible shift values
    for shift in range(26):
        # Initialize a blank result string
        result = ""

        # Iterate over each character in the ciphertext
        for char in ciphertext:
            # If the character is a letter, shift it by the current shift value
            if char.isalpha():
                # Get the ASCII value of the character
                ascii_value = ord(char)

                # Shift the ASCII value by the current shift value
                if char.isupper():
                    ascii_value = (ascii_value - 65 - shift) % 26 + 65
                else:
                    ascii_value = (ascii_value - 97 - shift) % 26 + 97

                # Convert the shifted ASCII value back to a character and add it to the result
                result += chr(ascii_value)
            # If the character is not a letter, just add it to the result
            else:
                result += char

        # Add the result to the list of possible plaintexts
        plaintexts.append(result)

    # Identify the correct plaintext by counting the number of recognizable words in each plaintext
    correct_index = 0
    max_recognizable_words = 0
    for i, plaintext in enumerate(plaintexts):
        recognizable_words = 0
        for word in plaintext.split():
            if dictionary.check(word):
                recognizable_words += 1
        if recognizable_words > max_recognizable_words:
            correct_index = i
            max_recognizable_words = recognizable_words

    # Print all of the possible plaintexts and highlight the correct one
    for i, plaintext in enumerate(plaintexts):
        if i == correct_index:
            print(f'===> Shift {i}: {plaintext}')
        else:
            print(f"Shift {i}: {plaintext}")

# Get the user's ciphertext
ciphertext = input("Enter the ciphertext: ")
print('')

# Decrypt the ciphertext using brute force
caesar_brute_force(ciphertext)
