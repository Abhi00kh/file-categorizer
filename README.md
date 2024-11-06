# file-categorizer

## Overview
File Organizer Pro is a Python package designed to organize files in a specified directory by their types, such as images, documents, videos, and more.

## Features
- Organizes files by type into subfolders.
- Supports custom rules for file categorization.
- Preview mode to show how files will be organized.
- Recursive organization for subdirectories.

## Installation

You can install the package using pip:

```bash
pip install file_organizer_pro
```
## Usage
Here is an example of how to use the package:
```bash
from file_organizer_pro.utils import get_file_type

print(get_file_type('example.jpg'))  # Outputs: Images
```
To organize files in a directory:
```bash
from file_organizer_pro.organizer import organize_files

organize_files('/path/to/directory')
```
## Custom Rules
You can define custom rules for file categorization by modifying the file_types dictionary in utils.py.

## organize files in subdirectories as well:
```bash
from file_organizer_pro.organizer import organize_files

organize_files('/path/to/directory', recursive=True)
```

