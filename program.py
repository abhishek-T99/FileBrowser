# library imports
import os
from filebrowser import FileBrowser

# main function
def main():
    browser = FileBrowser()
    
    # program loop
    while True:
        print(f"\nCurrent directory: {browser.current_path}")
        print("1. List directory contents")
        print("2. Create a file")
        print("3. Create a folder")
        print("4. Rename folder")
        print("5. Rename file")
        print("q: Quit")
        
        choice = input("Enter your choice: ")
    
        if choice == "1":
            browser.list_contents()
            
        elif choice == "2":
            browser.create_empty_file()
            
        elif choice == "3":
            browser.create_empty_folder()
            
        elif choice == "4":
            browser.rename_folder()
            
        elif choice == "5":
            browser.rename_file()
            
        elif choice == "q":
            break
        
        else:
            print("Invalid choice. Try again.")
        

if __name__ == "__main__":
    main()
    