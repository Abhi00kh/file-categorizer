from setuptools import setup, find_packages

setup(
    name="file_organizer",  # Name of your package
    version="0.1.0",  # Version of your package
    author="Abhijit Khule",  # Replace with your name
    author_email="abhijitkhule0@gmail.com",  # Replace with your email
    description="A Python package to organize files by type.",  # Brief description
    long_description=open('README.md').read(),  # Read the long description from README
    long_description_content_type="text/markdown",  # Set content type for long description
    url="https://github.com/Abhi00kh/file_organizer_pro",  # Replace with your GitHub URL
    packages=find_packages(),  # Automatically find and include packages
    classifiers=[
        "Programming Language :: Python :: 3",  # Supported Python version
        "License :: OSI Approved :: MIT License",  # License type
        "Operating System :: OS Independent",  # Operating system compatibility
    ],
    python_requires='>=3.6',  # Minimum Python version required
)

