import random
message = "test"

# Define the DNA encoding and decoding dictionaries
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


#encoding_dict = {'A': 'AT', 'T': 'UI', 'C': 'CG', 'H': 'HT', 'E': 'EA', 'L': 'LG', 'O': 'OT', 'W': 'WT', 'R': 'RT', 'D': 'DT', ' ': 'SP', 'V': 'VA', 'S': 'SZ', 'B': 'BW', 'I': 'IY'}
#encoding_dict = {'A': 'AT', 'T': 'TA', 'C': 'CG', 'G': 'GC'}
decoding_dict = {v: k for k, v in encoding_dict.items()}

# Function to encrypt a message using DNA encoding
def encrypt(message):
    encrypted = ''
    for char in message:
        if char in encoding_dict:
            encrypted += encoding_dict[char]
    return encrypted

# Function to decrypt a DNA-encoded message
def decrypt(encrypted):
    decrypted = ''
    for i in range(0, len(encrypted), 2):
        pair = encrypted[i: i + 2]
        if pair in decoding_dict:
            decrypted += decoding_dict[pair]
    return decrypted

# Example usage
print("Original Message:", message)

# Encryption
encrypted_message = encrypt(message)
print("Encrypted Message:", encrypted_message)

# Decryption
decrypted_message = decrypt(encrypted_message)
print("Decrypted Message:", decrypted_message)