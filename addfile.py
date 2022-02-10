import argparse
import os
import shutil
import csv

from utilities import files_dir_exists
from move_files_func import file_organizer


def add_file_CLI(filename):
    
    # checking if "files" directory exists:  if not return
    if(files_dir_exists() == False):
        print("Destination folder not found. You have to create a folder named 'files' in this directory.")
    else:
        # if file doesn't exist in "files" directory
        if(filename not in files_dir_exists()["files"]):
            print("No file at {} with the name of {}" .format(files_dir_exists()["path"], filename))
            return
    
        # calling main file_organizer func with filename as arg
        file_organizer(filename)
           
        
parser = argparse.ArgumentParser(description = "Move a file from the 'files' folder to a subfolder based on its extension. After that, update the recap file with its info." )

parser.add_argument("filename", type = str, help = "Insert a filename (name + extension)")

args = parser.parse_args()


# calling add_file_CLI func
add_file_CLI(args.filename)





