# File Processor

A simple Python script that demonstrates file handling and error management by reading a text file and creating a modified uppercase version.

## What it does

1. **Prompts** the user to enter a filename
2. **Reads** the contents of the specified file
3. **Converts** all text to uppercase
4. **Writes** the modified content to a new file with the prefix "modified\_"

## Features

- **Robust error handling** for common file operations:
  - File not found errors
  - Permission denied errors
  - General exceptions
- **Safe file operations** using context managers
- **Clear user feedback** with descriptive error messages

## Usage

```bash
python file_processor.py
```

When prompted, enter the name of any text file you'd like to process:

```
Enter the name of the file to read: example.txt
Modified file successfully written to 'modified_example.txt'
Everything in modified_example.txt is now all caps
```

## Example

If you have a file called `test.txt` containing:

```
Hello, World!
This is a test file.
```

Running the script will create `modified_test.txt` with:

```
HELLO, WORLD!
THIS IS A TEST FILE.
```
