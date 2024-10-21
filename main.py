import os
from pathlib import Path
import zipfile

def ad():
    current_file = os.path.realpath(__file__)
    current_directory = os.path.dirname(current_file)

    return current_directory

zip_file_name='croco-blitz-source.zip'
def print_zip():
    with zipfile.ZipFile(Path(ad()) / 'src' / zip_file_name,'r') as zip_file:
        file = zip_file.namelist()
    print("список файлов")
    for f in file:
        print(f)

if __name__=='__main__':
    print_zip()