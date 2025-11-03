import os
import json
import shutil

def rearrange_from_map(modified_dir, map_file="file_map.json", output_root="rearranged_output", missing_log="missing_files.txt", move_files=False):
    """
    Uses a file map (filename → relative path) to rearrange modified files into the original structure.
    """
    with open(map_file, "r", encoding="utf-8") as f:
        file_map = json.load(f)

    os.makedirs(output_root, exist_ok=True)
    missing = []

    # Index all modified files (searchable by name)
    modified_lookup = {}
    for dirpath, _, filenames in os.walk(modified_dir):
        for filename in filenames:
            modified_lookup[filename] = os.path.join(dirpath, filename)

    print(f"🔍 Found {len(modified_lookup)} modified files.")

    for filename, rel_path in file_map.items():
        dest_path = os.path.join(output_root, rel_path)
        dest_dir = os.path.dirname(dest_path)
        os.makedirs(dest_dir, exist_ok=True)

        # Already aligned? Skip
        if os.path.exists(dest_path):
            continue

        # Found matching file in modified directory?
        if filename in modified_lookup:
            src = modified_lookup[filename]
            if move_files:
                shutil.move(src, dest_path)
            else:
                shutil.copy2(src, dest_path)
        else:
            missing.append(rel_path)

    # Log missing files
    if missing:
        with open(missing_log, "w", encoding="utf-8") as f:
            f.write("\n".join(missing))
        print(f"⚠️ Missing {len(missing)} files. See '{missing_log}'.")
    else:
        print("✅ All files successfully matched.")

    print(f"📦 Output directory: {os.path.abspath(output_root)}")


if __name__ == "__main__":
    modified = input("Enter the MODIFIED directory path: ").strip('"')
    rearrange_from_map(modified)
