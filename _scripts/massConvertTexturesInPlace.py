import os
from PIL import Image
import py3dst

def convert_png_to_3dst(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith('.png'):
                png_path = os.path.join(dirpath, filename)
                base_name = os.path.splitext(filename)[0]
                out_path = os.path.join(dirpath, base_name + ".3dst")
                try:
                    outImage = Image.open(png_path)
                    texture = py3dst.Texture3dst().fromImage(outImage)
                    texture.export(out_path)
                    print(f"Converted: {png_path} -> {out_path}")
                    os.remove(png_path)
                    print(f"Deleted original: {png_path}")

                except Exception as e:
                    print(f"Failed to convert {png_path}: {e}")

if __name__ == "__main__":
    root_directory = ".\\"
    convert_png_to_3dst(root_directory)
