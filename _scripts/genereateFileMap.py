import os
import json

def generate_file_map(original_dir, output_json="file_map.json"):
    """
    Generates a JSON map of all files in the original directory.
    Maps { filename: relative_path }.
    """
    file_map = {}

    for dirpath, _, filenames in os.walk(original_dir):
        for filename in filenames:
            rel_path = os.path.relpath(os.path.join(dirpath, filename), original_dir)
            file_map[filename] = rel_path.replace("\\", "/")  # normalize slashes

    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(file_map, f, indent=4)

    print(f"✅ File map saved to '{output_json}' with {len(file_map)} entries.")


if __name__ == "__main__":
    original = input("Enter the ORIGINAL directory path: ").strip('"')
    generate_file_map(original)
