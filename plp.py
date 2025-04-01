def read_and_modify_file():
    try:
        # Ask user for the filename
        filename = input("Enter the filename to read: ")

        # Open the file and read contents
        with open(filename, 'r') as file:
            content = file.read()

        # Modify content (convert text to uppercase as an example)
        modified_content = content.upper()

        # Define a new filename for the modified file
        new_filename = "modified_" + filename

        # Write the modified content to the new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content saved to {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
