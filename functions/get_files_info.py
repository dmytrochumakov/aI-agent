import os

def get_files_info(working_directory, directory=None):
    if directory is None:
        target_dir = working_directory
    else:
        target_dir = os.path.join(working_directory, directory)

    if directory is not None:
        try:
            abs_working_dir = os.path.abspath(working_directory)
            abs_target_dir = os.path.abspath(target_dir)

            if not abs_target_dir.startswith(abs_working_dir) and abs_target_dir != abs_working_dir:
                return f"Error: Directory {directory} is outside the working directory"
        except Exception:
            return f"Error: Invalid directory path {directory}"

    if not os.path.exists(target_dir):
        return f"Error: Directory does not exists {target_dir}"
    if not os.path.isdir(target_dir):
        return f"Error: {target_dir} is not a directory"
    
    result = []

    try:
        items = os.listdir(target_dir)

        if not items:
            result.append("(empty directory)")
        else:
            for item in items:
                try:
                    item_path = os.path.join(target_dir, item)
                    if os.path.isdir(item_path):
                        size = os.path.getsize(item_path) if os.path.exists(item_path) else 0
                        result.append(f"- {item}: file_size={size} bytes, is_dir=True")
                    else:
                        size = os.path.getsize(item_path)
                        result.append(f"- {item}: file_size={size} bytes, is_dir=False")
                except (OSError, PermissionError):
                    is_dir = os.path.isdir(item_path)
                    result.append(f"- {item}: file_size=0 bytes, is_dir={is_dir}")
    except PermissionError:
        result.append("Permission denied - cannot read directory contents")
    except Exception as e:
        result.append(f"Error reading directory: {str(e)}")
    return "\n".join(result)
