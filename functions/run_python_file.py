import os
import subprocess
import sys

def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    full_path = os.path.join(working_directory, file_path)
    abs_file_path = os.path.abspath(full_path)

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(
                [sys.executable, abs_file_path],
                cwd=abs_working_dir,
                capture_output = True,
                text = True,
                timeout = 30
                )

        output = ""
        if result.stdout:
            output += "STDOUT:" + " " + result.stdout
        if result.stderr:
            output += "STDERR:" + " " + result.stderr
        if result.returncode != 0:
            output += f"\nProcess exited with code {result.returncode}"
    
        return output if output else "No output produced"
    except subprocess.TimeoutExpired:
        return "Error: Script execution timed out after 30 seconds."
    except Exception as e:
        return f"Error: executing Python file: {e}"
