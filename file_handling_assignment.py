def create_and_write_file():
    try:
        # Create a new file in 'w' mode and write initial content
        with open("my_file.txt", "w") as file:
            file.write("Hello, this is the first line.\n")
            file.write("This is the second line, including a number: 12345.\n")
            file.write("The third line is here!\n")
        print("File 'my_file.txt' created and written successfully.")
    
    except (FileNotFoundError, PermissionError) as e:
        print("Error while creating/writing the file: {}".format(e))

def read_file():
    try:
        # Read the content of the file and display it
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("Reading from 'my_file.txt':")
            print(content)
    
    except (FileNotFoundError, PermissionError) as e:
        print("Error while reading the file: {}".format(e))

def append_to_file():
    try:
        #  Open the file in append mode and add more lines
        with open("my_file.txt", "a") as file:
            file.write("Appending a fourth line.\n")
            file.write("Appending a fifth line with a number: 67890.\n")
            file.write("This is the final appended line.\n")
        print("Additional content appended successfully.")

    except (FileNotFoundError, PermissionError) as e:
        print("Error while appending to the file: {}".format(e))

def main():
    try:
        # Call the functions to demonstrate file handling
        create_and_write_file()
        read_file()
        append_to_file()
        read_file()  # Reading again to see the appended content
    
    except Exception as e:
        print("An unexpected error occurred: {}".format(e))

    finally:
        print("File handling operations completed.")

if __name__ == "__main__":
    main()
