def get_file_type(filename):
    """Returns the folder name based on the file extension."""
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.xls', '.xlsx'],
        'Videos': ['.mp4', '.mov', '.avi'],
        'Music': ['.mp3', '.wav'],
        'Archives': ['.zip', '.tar', '.gz', '.rar'],
        'Installation Files': ['.exe', '.msi', '.dmg', '.deb', '.rpm']
    }
    
    file_ext = filename.split('.')[-1].lower()
    for folder_name, extensions in file_types.items():
        if f".{file_ext}" in extensions:
            return folder_name
    return None