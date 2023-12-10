#!/usr/bin/env python3
import os
import subprocess
import sys

def find_venv(project_dir):
    # Common virtual environment directory names
    venv_names = ['venv', '.venv']

    # Search for a virtual environment in the project directory
    for name in venv_names:
        venv_path = os.path.join(project_dir, name)
        if os.path.exists(venv_path):
            return venv_path

    # Return None if no virtual environment is found
    return None

def generate_requirements(project_dir, venv_path):
    # Activate the virtual environment
    activate_script = os.path.join(venv_path, 'bin', 'activate')
    command = f'source "{activate_script}" && pip freeze > "{os.path.join(project_dir, "requirements.txt")}"'

    # Run the command in a subshell
    subprocess.run(command, shell=True, executable='/bin/bash')

    print(f'requirements.txt generated in {project_dir}')

if __name__ == "__main__":
    # Check if the project directory is provided
    if len(sys.argv) != 2:
        print("Usage: python generate_requirements_file.py <project_directory>")
        sys.exit(1)

    project_dir = sys.argv[1]

    # Find the virtual environment
    venv_path = find_venv(project_dir)
    if venv_path is None:
        print("No virtual environment found in the project directory.")
    else:
        generate_requirements(project_dir, venv_path)
