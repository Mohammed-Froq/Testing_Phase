import os
from PIL import Image

mockups_dir = '/Users/froquser/Desktop/Testing_Phase-main/assets/mockups'

for name in ['hero_composition.png', 'slide1_opt.png', 'slide1_clean.png', 'hero_composition_solution.png']:
    path = os.path.join(mockups_dir, name)
    if not os.path.exists(path):
        print(f"{name} does not exist")
        continue
    try:
        with Image.open(path) as img:
            img = img.convert('RGB')
            pixels = list(img.getdata())
            red_count = 0
            green_count = 0
            other_count = 0
            for r, g, b in pixels:
                if r > 240 and g > 240 and b > 240:
                    continue
                if r > g * 1.3 and r > b * 1.3:
                    red_count += 1
                elif g > r * 1.2 and g > b * 1.2:
                    green_count += 1
                else:
                    other_count += 1
            total = red_count + green_count + other_count
            if total == 0:
                print(f"{name}: blank or all white")
            else:
                print(f"{name}: red={red_count/total:.1%}, green={green_count/total:.1%}, other={other_count/total:.1%}")
    except Exception as e:
        print(f"Error reading {name}: {e}")
