def decrypt_caesar_cipher(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift % 26  # Handle large shift values
            if char.isupper():
                shifted = chr(((ord(char) - 65 - shift_amount) % 26) + 65)
            else:
                shifted = chr(((ord(char) - 97 - shift_amount) % 26) + 97)
            plain_text += shifted
        else:
            plain_text += char
    return plain_text

# Example usage
cipher_text = input("Enter the cipher text")
secret_code = input("Enter the secret code: ")
count = len(secret_code)
secret_message = cipher_text[0:-(count)]
shift = 3
plain_text = decrypt_caesar_cipher(secret_message, shift)
print("Cipher text:", secret_message)
print("Shift:", shift)
print("Plain text:", plain_text)
