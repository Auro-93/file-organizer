import os
import shutil
import csv

from utilities import file_types, work_directory, work_dir_elements


###### CREATING A GENERAL FUNC TO ORGANIZE FILES AND UPDATE RECAP FOR BOTH PROJECT STEP ONE AND TWO ######


# logic for directories creation: if directory already exists do nothing, otherwhise create it
def create_directories(files_dir_path):
    for dictionary in file_types:
        directory = ""
        for type_key in dictionary:
            if(type_key == "type"):
                directory = dictionary[type_key]
            try:
                path = os.path.join(files_dir_path, directory)
                os.mkdir(path) #create directory     
            except FileExistsError: #directory already exists: pass
                pass
            except Exception as e:
                print("Something went wrong: {}".format(e))
                

 
 # logic for csv recap file    
def manage_csv_recap(header, data):
                    
    # Creating csv file with nothing inside               
    if("recap.csv" not in work_dir_elements):
        with open ("recap.csv", "a") as recap:
            pass
                
    # Read mode : checking if header and specific file data are already in the csv file
    header_in_csv = False
    file_data_in_csv = False
    
    with open ("recap.csv", "r") as recap:
        
        reader = list(csv.reader(recap))
        
        if(header in reader):
             header_in_csv = True
        else:
             header_in_csv = False       
        if(data in reader):
             file_data_in_csv = True
        else:
             file_data_in_csv = False
       
             
    # Append mode : if header or file data are not in the csv file add them                   
    with open("recap.csv", "a", newline='') as recap:
        
        writer = csv.writer(recap)
        
        if(header_in_csv == False):       
            writer.writerow(header)
        if(file_data_in_csv == False):       
            writer.writerow(data) 
                                        

                
# logic for file moving
def move_files(files, files_dir_path):
    
    for file in files: 
        # original file path
        file_path = os.path.join(files_dir_path, file)
        # file name
        file_name = os.path.splitext(file)[0]
        # file extension
        file_extension = os.path.splitext(file)[1]
        #file size
        file_size = os.path.getsize(file_path)
        #file type
        file_type = ""
        
        for obj in file_types:
            for extension in obj["extensions"]:
                
                if(file_extension == extension): # if the file has a recognizable extension findable in "file_types" 
                    file_type = extension     
                    #if file already exists in the specific folder, print an error
                    if(file in os.listdir(os.path.join(files_dir_path, obj["type"]))):
                        print("Operation failed: {} already exists in {} folder".format(file, obj["type"]))
                    else:
                        # moving file to a specific directory based on its extension 
                        shutil.move(os.path.join(files_dir_path, file), os.path.join(files_dir_path, obj["type"], file))
                        # print file info
                        print("{} type:{} size:{}".format(file_name, file_type, file_size))
                        
                        file_header = ["name", "type" , "size(B)"] # header tags for csv file
                        file_data = [file_name, file_type, str(file_size)] # data info for csv file
                        # calling manage_csv_recap func
                        manage_csv_recap(file_header, file_data)
                        

                        
# MAIN FUNC
def file_organizer(files, files_dir_path = os.path.join(work_directory, "files")): 
    
    # calling create_directories func (if directories don't exist create them)
    create_directories(files_dir_path)
                
    # if argument is a string (step 2) create a list with only that string element (to iterate in the next move_files func)
    files_list = []
    if(type(files) == str):
        file = files
        if( os.path.isfile(os.path.join(files_dir_path, file))):
             files_list = [file]      
    if(type(files) == list):
        files_list = files
        
    # calling move_files func
    move_files(files_list, files_dir_path)
     
            