import os
import base64

mockups_dir = '/Users/froquser/Desktop/Testing_Phase-main/assets/mockups'

for filename in os.listdir(mockups_dir):
    if filename.endswith('.base64.txt'):
        full_path = os.path.join(mockups_dir, filename)
        with open(full_path, 'r') as f:
            data = f.read().strip()
        
        # Split prefix if exists (e.g. data:image/png;base64,...)
        if ',' in data:
            header, base64_data = data.split(',', 1)
        else:
            base64_data = data
            
        decoded_data = base64.b64decode(base64_data)
        
        # Output filename: replace .base64.txt with .png
        out_name = filename.replace('.base64.txt', '.png')
        out_path = os.path.join(mockups_dir, out_name)
        
        with open(out_path, 'wb') as f_out:
            f_out.write(decoded_data)
        print(f"Decoded {filename} to {out_name}")
