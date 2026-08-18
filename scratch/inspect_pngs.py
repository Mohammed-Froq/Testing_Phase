import os
from PIL import Image

mockups_dir = '/Users/froquser/Desktop/Testing_Phase-main/assets/mockups'

for filename in os.listdir(mockups_dir):
    if filename.endswith('.png') and not filename.startswith('shared_image'):
        full_path = os.path.join(mockups_dir, filename)
        try:
            with Image.open(full_path) as img:
                print(f"{filename}: size={img.size}, mode={img.mode}")
        except Exception as e:
            print(f"Error opening {filename}: {e}")
