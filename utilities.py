import os


# creating a support list of dictionaries for files types and extensions
file_types = [
                {
                  "type": "audio",
                  "extensions": [".mp3", ".ogg", ".wav", "..wma", ".aiff"]
                },
                {
                   "type": "docs",
                   "extensions": [".doc", ".docx", ".odt", ".pdf", ".txt"]
                },
                {
                   "type": "images",
                   
                   "extensions": [".jpeg", ".jpg", ".png", ".svg", ".gif", ".ai", ".bmp", ".ico"]
                },
             ]


# getting relative path of this directory
work_directory = os.getcwd()

    
# getting a list of the files in work-directory
work_dir_elements = os.listdir(work_directory)


# checking if "files" directory exists func
def files_dir_exists():
    
    # if "files" dir exists, return a dictionary with path ("files" dir path) and files (list of files inside "files" dir path) key-value
    if(os.path.isdir(os.path.join(work_directory, "files"))):
        
        dir_path = os.path.join(work_directory, "files")
        dir_elements = os.listdir(dir_path)
        
        # make a list only of elements that are files (not subfolders)
        dir_files = [file for file in dir_elements if os.path.isfile(os.path.join(dir_path, file))]
        
        # sorting files list alphabetically
        dir_files = sorted(dir_files)
        
        return {"path" : dir_path, "files" : dir_files}
    
    # else return False
    else:
        return False

    


     


