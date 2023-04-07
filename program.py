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
        print("6. Copy file")
        print("7. Copy folder")
        print("8. Move file")
        print("9. Move folder")
        print("10. Delete file")
        print("11. Delete folder")
        print("12. Create random text file")
        print("13. Read file content")
        print("14. Hide folder")
        print("15. Show hidden folders")
        print("16. Make a file executable")
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
            
        elif choice == "6":
            browser.copy_file()
            
        elif choice == "7":
            browser.copy_folder()
            
        elif choice == "8":
            browser.move_file()
            
        elif choice == "9":
            browser.move_folder()
            
        elif choice == "10":
            browser.delete_file()
            
        elif choice == "11":
            browser.delete_folder()
            
        elif choice == "12":
            browser.create_random_text_file()
            
        elif choice == "13":
            browser.view_file()
            
        elif choice == "14":
            browser.hide_folder()
            
        elif choice == "15":
            browser.toggle_hidden()
            
        elif choice == "16":
            browser.make_file_executable()
            
        elif choice == "q":
            break
        
        else:
            print("Invalid choice. Try again.")
        

if __name__ == "__main__":
    main()
    