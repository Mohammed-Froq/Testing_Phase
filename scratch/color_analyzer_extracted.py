import os
from PIL import Image

extracted_dir = '/Users/froquser/Desktop/Testing_Phase-main/assets/extracted'

if not os.path.exists(extracted_dir):
    print("Extracted directory does not exist")
    exit()

for filename in os.listdir(extracted_dir):
    if filename.endswith('.png'):
        path = os.path.join(extracted_dir, filename)
        try:
            with Image.open(path) as img:
                img = img.convert('RGB')
                pixels = list(img.getdata())
                red_count = 0
                green_count = 0
                other_count = 0
                for r, g, b in pixels:
                    # Ignore transparent/white pixels
                    if r > 240 and g > 240 and b > 240:
                        continue
                    if r > g * 1.5 and r > b * 1.5:
                        red_count += 1
                    elif g > r * 1.5 and g > b * 1.5:
                        green_count += 1
                    else:
                        other_count += 1
                total = red_count + green_count + other_count
                if total > 100:  # only look at non-empty images
                    red_pct = red_count / total
                    green_pct = green_count / total
                    if red_pct > 0.1 or green_pct > 0.1:
                        print(f"{filename}: size={img.size}, red={red_pct:.1%}, green={green_pct:.1%}")
        except Exception as e:
            pass
