import os

def print_python_file_paths_one_line():
    """Print absolute paths of all .py files in the current directory on one line."""
    current_directory = os.getcwd()  # Get the current working directory
    python_files = [os.path.abspath(f) for f in os.listdir(current_directory) if f.endswith(".py")]
    
    # Join all paths with a space and print
    print(" ".join(python_files))

# Execute the function
print_python_file_paths_one_line()