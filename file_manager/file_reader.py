
### File: file_manager/file_reader.py

import os

def get_all_code(directory, extensions):
    collected = []
    filenames = []

    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                path = os.path.join(root, file)
                filenames.append(path)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        code = f.read()
                        collected.append(f"# {file}\n{code}\n")
                except Exception:
                    continue

    file_list_summary = "\n".join(filenames)
    file_contents = "\n".join(collected)
    return file_list_summary, file_contents
