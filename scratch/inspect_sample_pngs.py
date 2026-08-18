import os
from PIL import Image

sample_dir = '/Users/froquser/Desktop/Testing_Phase-main/Sample/Mobile_HomeScreen'

for filename in os.listdir(sample_dir):
    if filename.endswith('.png'):
        full_path = os.path.join(sample_dir, filename)
        try:
            with Image.open(full_path) as img:
                print(f"{filename}: size={img.size}, mode={img.mode}")
        except Exception as e:
            print(f"Error opening {filename}: {e}")
