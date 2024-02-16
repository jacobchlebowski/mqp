import zipfile
import os

def unzip_file(zip_file, extract_to):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

if __name__ == "__main__":
    # Replace 'your_file.zip' with the name of your zip file
    zip_file = 'C:/Users/Administrator/Desktop/benign.zip'
    
    # Replace 'extracted_directory' with the directory where you want to extract the contents
    extract_to = 'C:/Users/Administrator/Desktop/'

    # Create the destination directory if it doesn't exist
    os.makedirs(extract_to, exist_ok=True)

    # Call the function to unzip the file
    unzip_file(zip_file, extract_to)

    print(f"Successfully unzipped '{zip_file}' to '{extract_to}'.")

