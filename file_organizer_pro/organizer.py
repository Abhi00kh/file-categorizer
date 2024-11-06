# import os
# import shutil
# from .utils import get_file_type

# def organize_files_by_type(path):
#     """Organize files in the given directory by type."""
#     if not os.path.exists(path):
#         print(f"Path '{path}' does not exist.")
#         return

#     for filename in os.listdir(path):
#         file_path = os.path.join(path, filename)
#         if os.path.isfile(file_path):
#             folder_name = get_file_type(filename)
#             if folder_name:
#                 folder_path = os.path.join(path, folder_name)
#                 if not os.path.exists(folder_path):
#                     os.makedirs(folder_path)
#                 shutil.move(file_path, os.path.join(folder_path, filename))
#                 print(f"Moved '{filename}' to '{folder_name}/'")

# def organize_recursively(path):
#     """Organize files in the given directory and its subdirectories by type."""
#     for root, _, files in os.walk(path):
#         for filename in files:
#             file_path = os.path.join(root, filename)
#             folder_name = get_file_type(filename)
#             if folder_name:
#                 folder_path = os.path.join(root, folder_name)
#                 if not os.path.exists(folder_path):
#                     os.makedirs(folder_path)
#                 shutil.move(file_path, os.path.join(folder_path, filename))
#                 print(f"Moved '{filename}' to '{folder_name}/'")

# def preview_organization(path):
#     """Preview how files will be organized in the given directory."""
#     if not os.path.exists(path):
#         print(f"Path '{path}' does not exist.")
#         return

#     print("Preview of file organization:")
#     for filename in os.listdir(path):
#         file_path = os.path.join(path, filename)
#         if os.path.isfile(file_path):
#             folder_name = get_file_type(filename)
#             if folder_name:
#                 print(f"{filename} -> {folder_name}/")

# def custom_rules(path, rules_dict):
#     """Organize files based on custom user-defined rules."""
#     if not os.path.exists(path):
#         print(f"Path '{path}' does not exist.")
#         return

#     for filename in os.listdir(path):
#         file_path = os.path.join(path, filename)
#         if os.path.isfile(file_path):
#             file_ext = os.path.splitext(filename)[1].lower()
#             for folder_name, extensions in rules_dict.items():
#                 if file_ext in extensions:
#                     folder_path = os.path.join(path, folder_name)
#                     if not os.path.exists(folder_path):
#                         os.makedirs(folder_path)
#                     shutil.move(file_path, os.path.join(folder_path, filename))
#                     print(f"Moved '{filename}' to '{folder_name}/'")
#                     break
import os
import shutil
from .utils import get_file_type

def is_valid_folder_name(folder_name):
    """Check if the folder name is valid (not empty or containing invalid characters)."""
    invalid_chars = '<>:"/\\|?*'  # Windows invalid characters
    return folder_name and not any(char in invalid_chars for char in folder_name)

def organize_files_by_type(path):
    """Organize files in the given directory by type."""
    if not os.path.exists(path):
        print(f"Path '{path}' does not exist.")
        return

    # Create a set to keep track of folder names we need to create
    folder_names = set()

    # Identify all file types
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            folder_name = get_file_type(filename)
            if is_valid_folder_name(folder_name):
                folder_names.add(folder_name)

    # Create the folders based on identified file types
    for folder_name in folder_names:
        folder_path = os.path.join(path, folder_name)  # No normalization needed
        print(f"Creating folder: {folder_path}")  # Debug print
        os.makedirs(folder_path, exist_ok=True)  # Create the folder if it doesn't exist

    # Move the files into their respective folders
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            folder_name = get_file_type(filename)
            if is_valid_folder_name(folder_name):
                destination_path = os.path.join(path, folder_name, filename)  # No normalization needed
                print(f"Moving '{filename}' to '{destination_path}'")  # Debug print
                shutil.move(file_path, destination_path)
                print(f"Moved '{filename}' to '{folder_name}/'")

def organize_recursively(path):
    """Organize files in the given directory and its subdirectories by type."""
    for root, _, files in os.walk(path):
        for filename in files:
            file_path = os.path.join(root, filename)
            folder_name = get_file_type(filename)
            if is_valid_folder_name(folder_name):
                folder_path = os.path.join(root, folder_name)  # No normalization needed
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                shutil.move(file_path, os.path.join(folder_path, filename))
                print(f"Moved '{filename}' to '{folder_name}/'")

def preview_organization(path):
    """Preview how files will be organized in the given directory."""
    if not os.path.exists(path):
        print(f"Path '{path}' does not exist.")
        return

    print("Preview of file organization:")
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            folder_name = get_file_type(filename)
            if folder_name:
                print(f"{filename} -> {folder_name}/")

def custom_rules(path, rules_dict):
    """Organize files based on custom user-defined rules."""
    if not os.path.exists(path):
        print(f"Path '{path}' does not exist.")
        return

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            for folder_name, extensions in rules_dict.items():
                if file_ext in extensions:
                    folder_path = os.path.join(path, folder_name)  # No normalization needed
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    shutil.move(file_path, os.path.join(folder_path, filename))
                    print(f"Moved '{filename}' to '{folder_name}/'")
                    break
