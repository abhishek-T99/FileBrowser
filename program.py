# library imports
from filebrowser import FileBrowser

# main function
def main():
    # instanting FileBrowser class
    browser = FileBrowser()
    
    # File Browser menu dictionary
    menu = {
        '1': browser.list_contents, '2': browser.create_empty_file, '3': browser.create_empty_folder, 
        '4': browser.rename_folder, '5': browser.rename_file, '6': browser.copy_file, 
        '7': browser.copy_folder, '8': browser.move_file,  '9': browser.move_folder, 
        '10': browser.delete_file, '11': browser.delete_folder, '12': browser.create_random_text_file,
        '13': browser.view_file, '14': browser.hide_folder, '15': browser.toggle_hidden, 
        '16': browser.make_file_executable
    }
    
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
        
        if choice == 'q':
            break
        if choice in menu:
            menu[choice]()
        else:
            print("Invalid choice. Try again.")
    
        
if __name__ == "__main__":
    main() 