def caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shifted = ord(char) + shift

            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26

            encrypted_text += chr(shifted)
        else:
            encrypted_text += char  # If the character is not a letter, keep it unchanged

    return encrypted_text


secret_message = input("Enter the secret message: ")
secret_code = input("Enter the secret code: ")
plaintext = secret_message+secret_code
shift = 3
cipher_text = caesar_cipher(plaintext, shift)
print("Original Text:", plaintext)
print("Cipher Text:", cipher_text)
