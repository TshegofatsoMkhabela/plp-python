def main():
    # 🧪 Error Handling Lab
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, "r") as infile:
            contents = infile.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return
    except PermissionError:
        print(f"Error: You don’t have permission to read '{filename}'.")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return

    # 🖋️ File Read & Write Challenge
    # Example modification: convert text to uppercase
    modified_contents = contents.upper()

    # Write to a new file
    new_filename = "modified_" + filename
    try:
        with open(new_filename, "w") as outfile:
            outfile.write(modified_contents)
        print(f"Modified file successfully written to '{new_filename}'\n Everything in {new_filename} is now all caps")
    except Exception as e:
        print(f"Error writing to file: {e}")


if __name__ == "__main__":
    main()
