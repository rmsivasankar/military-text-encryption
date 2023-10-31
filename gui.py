import hashlib

def convert_to_md5(plain_text):
    md5_hash = hashlib.md5(plain_text.encode()).hexdigest()  # Calculate the MD5 hash
    return md5_hash

# Get input from the user
text = input("Enter the Message: ")
code = input("Enter the Code: ")
# Generate the MD5 hash
md5_first = convert_to_md5(text)
md5_second = convert_to_md5(code)

print(f"The encrypted text is: {md5_first}+{md5_second}")
