import os
from PIL import Image

image_path = '/Users/froquser/Desktop/Testing_Phase-main/assets/Logo/WhatsApp Image 2026-08-15 at 18.28.57.jpeg'
output_path = '/Users/froquser/Desktop/Testing_Phase-main/assets/Logo/logo_transparent.png'

try:
    img = Image.open(image_path)
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    # Let's detect background color from top-left corner pixel
    bg_color = datas[0]
    print(f"Top-left pixel color (potential background): {bg_color}")
    
    # We will make pixels close to the background color transparent
    # Typically white or very light grey (thresholding)
    for item in datas:
        # Check if the pixel is near white/light-grey or close to the detected bg_color
        # bg_color is (R, G, B, A)
        r_diff = abs(item[0] - bg_color[0])
        g_diff = abs(item[1] - bg_color[1])
        b_diff = abs(item[2] - bg_color[2])
        
        # Also check if it's generally white/light-grey
        is_white = item[0] > 240 and item[1] > 240 and item[2] > 240
        
        if (r_diff < 30 and g_diff < 30 and b_diff < 30) or is_white:
            # Make transparent
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(output_path, "PNG")
    print(f"Saved transparent logo to {output_path}")

except Exception as e:
    print(f"Error: {e}")
