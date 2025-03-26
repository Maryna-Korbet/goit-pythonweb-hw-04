# Async Folder Sorter

## Description
This Python script asynchronously sorts files from a specified source folder into subfolders based on their extensions in a destination folder. It efficiently handles large numbers of files using asynchronous operations.

## Features
- Recursively reads all files in the source directory.
- Sorts files into subdirectories based on their extensions.
- Uses asynchronous operations for better performance.
- Logs all actions and errors.

## Requirements
- Python 3.8+
- Install dependencies using:
  ```bash
  pip install aiopath aioshutil
  ```

## Usage
Run the script with the following command:

```bash
python main.py --source <source_folder> --output <output_folder>
```

### Example
```bash
python main.py --source test_source --output test_output
```
This will copy files from `test_source` and sort them into `test_output` based on their extensions.

## License
This project is licensed under the MIT License.

