
import os

def print_directory_tree(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip hidden files and folders
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        filenames = [f for f in filenames if not f.startswith('.')]
        # Print the directory path
        print(f"{dirpath}/")

        # Print the filenames in the directory
        for filename in filenames:
            print(f"{filename}")

# Call the function with the current directory
print_directory_tree('C:\\Users\\VZCS6X\\Documents\\PythonProjects\\Nback\\')
