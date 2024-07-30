# DNA Encryption Method

## Description

The DNA encryption method leverages the concept of mapping characters to unique pairs of characters, inspired by the way biological DNA sequences encode information. Each character in the message is encoded using a predefined dictionary that maps characters to two-character sequences. This method ensures that the original message is transformed into an encoded string, which can then be decoded back to the original message using the reverse mapping dictionary.

- **Encryption**: Each character in the input message is replaced with a corresponding two-character sequence from the encoding dictionary.
- **Decryption**: The encoded message is split into pairs of characters, and each pair is mapped back to the original character using the decoding dictionary.

This approach allows for secure and reversible transformation of messages, ensuring that the information can be safely encoded and later decoded.

## Installation

To run the DNA encryption method on your local machine, follow these steps:

### Prerequisites

- Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Setup

1. **Create a Project Directory**:
   - Create a new directory for your project.
   - Inside this directory, create a new Python file, e.g., `dna_encryption.py`.

2. **Copy the Code**:
   - Copy the following code into your `dna_encryption.py` file:

   ```python
   import random

   # Define the DNA encoding and decoding dictionaries for all possible characters
   encoding_dict = {
       'A': 'AT', 'B': 'BW', 'C': 'CG', 'D': 'DT', 'E': 'EA', 'F': 'FT', 'G': 'GT', 'H': 'HT', 'I': 'IY',
       'J': 'JT', 'K': 'KT', 'L': 'LG', 'M': 'MT', 'N': 'NT', 'O': 'OT', 'P': 'PT', 'Q': 'QT', 'R': 'RT',
       'S': 'SZ', 'T': 'UI', 'U': 'UY', 'V': 'VA', 'W': 'WT', 'X': 'XT', 'Y': 'YT', 'Z': 'ZT',
       'a': 'aT', 'b': 'bW', 'c': 'cG', 'd': 'dT', 'e': 'eA', 'f': 'fT', 'g': 'gT', 'h': 'hT', 'i': 'iY',
       'j': 'jT', 'k': 'kT', 'l': 'lG', 'm': 'mT', 'n': 'nT', 'o': 'oT', 'p': 'pT', 'q': 'qT', 'r': 'rT',
       's': 'sZ', 't': 'uI', 'u': 'uY', 'v': 'vA', 'w': 'wT', 'x': 'xT', 'y': 'yT', 'z': 'zT',
       '0': '0T', '1': '1T', '2': '2T', '3': '3T', '4': '4T', '5': '5T', '6': '6T', '7': '7T', '8': '8T', '9': '9T',
       ' ': 'SP', '!': 'EX', '@': 'AT', '#': 'HS', '$': 'DL', '%': 'PC', '^': 'CR', '&': 'AN', '*': 'AS', '(': 'LP', ')': 'RP',
       '-': 'DS', '_': 'US', '+': 'PL', '=': 'EQ', '{': 'LB', '}': 'RB', '[': 'LS', ']': 'RS', ':': 'CL', ';': 'SC', '"': 'QT',
       "'": 'SQ', '<': 'LT', '>': 'GT', ',': 'CM', '.': 'DT', '?': 'QM', '/': 'FS', '\\': 'BS', '|': 'PP'
   }
   decoding_dict = {v: k for k, v in encoding_dict.items()}

   # Function to encrypt a message using DNA encoding
   def encrypt(message):
       encrypted = ''
       for char in message:
           if char in encoding_dict:
               encrypted += encoding_dict[char]
           else:
               print(f"Character '{char}' cannot be encrypted.")
               return ''
       return encrypted

   # Function to decrypt a DNA-encoded message
   def decrypt(encrypted):
       decrypted = ''
       for i in range(0, len(encrypted), 2):
           pair = encrypted[i: i + 2]
           if pair in decoding_dict:
               decrypted += decoding_dict[pair]
           else:
               print(f"Pair '{pair}' cannot be decrypted.")
               return ''
       return decrypted

   # Prompt the user for input
   message = input("Enter the message to be encrypted: ")

   # Display the original message
   print("Original Message:", message)

   # Encryption
   encrypted_message = encrypt(message)
   if encrypted_message:
       print("Encrypted Message:", encrypted_message)

       # Decryption
       decrypted_message = decrypt(encrypted_message)
       if decrypted_message:
           print("Decrypted Message:", decrypted_message)
   else:
       print("Encryption error. Please check the message and try again.")


3. **Run the Script**:

Open a terminal or command prompt.
Navigate to the directory where you saved dna_encryption.py.
Run the script using the command:
python dna_encryption.py

3. **Enter the Message**:

When prompted, enter the message you wish to encrypt.
The script will display the original message, the encrypted message, and the decrypted message.

4. **Usage**:

After following the installation steps, you can use the script to encrypt and decrypt messages. Simply run the script and input the message you want to process.

