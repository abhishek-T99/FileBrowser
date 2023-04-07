# library imports
import os
import shutil
from random import choices
from string import ascii_lowercase, digits

# class definition 
class FileBrowser:
    
    def __init__(self):
        self.current_path = os.getcwd()
        self.show_hidden = False
        
    def list_contents(self):
        files = os.listdir(self.current_path)
        if not self.show_hidden:
            files = [f for f in files if not f.startswith('.')] 
        for f in files:
            print(f)
            
    def rename_folder(self):
        old_name = input("Enter the name of the folder you want to rename: ")
        new_name = input("Enter the new name of the folder: ")
        os.rename(os.path.join(self.current_path, old_name), os.path.join(self.current_path, new_name))
        print("Folder renamed successfully.")
        
    def rename_file(self):
        old_name = input("Enter the name of the file you want to rename: ")
        new_name = input("Enter the new name of the file: ")
        os.rename(os.path.join(self.current_path, old_name), os.path.join(self.current_path, new_name))
        print("File renamed successfully.")
        
    def create_empty_file(self):
        filename = input("Enter the name of the file to create: ")
        with open(os.path.join(self.current_path, filename), 'w') as f:
            pass
        print(f"File '{filename}' created successfully.")
        
    def create_empty_folder(self):
        foldername = input("Enter the name of the foldere to create: ")
        try:
            os.mkdir(foldername)
            print(f"Folder '{foldername}' created successfully..")
        except:
            print(f"Folder '{foldername}' already exists.")
            
    def copy_file(self):
        file_name = input("Enter file name: ")
        dest_folder = input("Enter destination folder: ")
        try:
            shutil.copy(os.path.join(self.current_path, file_name), os.path.join(dest_folder, file_name))
            print(f"File {file_name} copied to {dest_folder}.")
        except FileNotFoundError:
            print("File not found.")

    def copy_folder(self):
        folder_name = input("Enter folder name: ")
        dest_folder = input("Enter destination folder: ")
        try:
            shutil.copytree(os.path.join(self.current_path, folder_name), os.path.join(dest_folder, folder_name))
            print(f"Folder {folder_name} copied to {dest_folder}.")
        except FileNotFoundError:
            print("Folder not found.")
            
    def move_file(self):
        file_name = input("Enter file name: ")
        dest_folder = input("Enter destination folder: ")
        try:
            shutil.move(os.path.join(self.current_path, file_name), os.path.join(dest_folder, file_name))
            print(f"File {file_name} moved to {dest_folder}.")
        except FileNotFoundError:
            print("File not found.")

    def move_folder(self):
        folder_name = input("Enter folder name: ")
        dest_folder = input("Enter destination folder: ")
        try:
            shutil.move(os.path.join(self.current_path, folder_name), os.path.join(dest_folder, folder_name))
            print(f"Folder {folder_name} moved to {dest_folder}.")
        except FileNotFoundError:
            print("Folder not found.")
            
    def delete_file(self):
        file_name = input("Enter file name: ")
        try:
            os.remove(os.path.join(self.current_path, file_name))
            print(f"File {file_name} deleted.")
        except FileNotFoundError:
            print("File not found.")

    def delete_folder(self):
        folder_name = input("Enter folder name: ")
        try:
            shutil.rmtree(os.path.join(self.current_path, folder_name))
            print(f"Folder {folder_name} deleted.")
        except FileNotFoundError:
            print("Folder not found.")
            
    def create_random_text_file(self):
        file_name = input("Enter file name: ")
        length = int(input("Enter length of random text: "))
        try:
            with open(os.path.join(self.current_path, file_name), "w") as f:
                f.write(''.join(choices(ascii_lowercase + digits, k=length)))
            print(f"Random text file {file_name} created.")
        except FileNotFoundError:
            print("Directory not found")
            
    def view_file(self):
        file_name = input("Enter file name: ")
        try:
            with open(os.path.join(self.current_path, file_name), "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("File not found.")
            
    def hide_folder(self):
        folder_name = input("Enter folder name: ")
        try:
            os.rename(os.path.join(self.current_path, folder_name), os.path.join(self.current_path, f".{folder_name}"))
        except FileNotFoundError:
            print("Folder not found.")
            
    def toggle_hidden(self):
        self.show_hidden = not self.show_hidden
        files = os.listdir(self.current_path)
        if self.show_hidden:
            files = [f for f in files if f.startswith('.')] 
        for f in files:
            print(f)
            
    def make_file_executable(self):
        file_name = input("Enter file name: ")
        try:
            file_path = os.path.join(os.getcwd(), file_name)
            os.chmod(file_path, 0o755)
            print(f"File {file_name} is now executable.")
        except FileNotFoundError:
            print("File not found.")
            