def file_read_write():
    
    filename = input("Enter the filename to read: ")

    try:
        # Read the content of the file
        with open(filename, "r") as file:
            content = file.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Create a new output file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"✅ File has been modified and saved as '{new_filename}'")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the function
file_read_write()
