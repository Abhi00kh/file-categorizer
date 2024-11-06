# File Organizer Pro

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
pip install file-categorizer
```

## Usage
Here is an example of how to use the package:
```python
from file_organizer_pro.organizer import organize_files_by_type, organize_recursively, preview_organization, custom_rules

# Test a directory path (make sure this path exists)
test_path = 'C:/path/to/your/test/folder'

# Organize files by type
organize_files_by_type(test_path)

# Organize files recursively
organize_recursively(test_path)

# Preview how files will be organized
preview_organization(test_path)

# Define custom categorization rules
rules = {
    'Images': ['.jpg', '.jpeg', '.png'],
    'Documents': ['.pdf', '.docx', '.txt']
}

# Organize files based on custom rules
custom_rules(test_path, rules)
```
## Functions
organize_files_by_type(path)
Organize files in the specified directory by type (e.g., images, documents).

organize_recursively(path)
Recursively organize files in the specified directory and all its subdirectories.

preview_organization(path)
Preview the file organization in the specified directory without actually moving files.

custom_rules(path, rules_dict)
Organize files based on custom user-defined rules. The rules_dict should map folder names to lists of file extensions.
