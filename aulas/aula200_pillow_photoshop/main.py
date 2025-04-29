# Pillow: https://pillow.readthedocs.io/en/stable/
# Pillow is a Python Imaging Library that adds image processing capabilities to your Python interpreter.

from PIL import Image, ImageFilter, ImageDraw, ImageFont
from pathlib import Path

root_folder = Path(__file__).parent
img_path = root_folder / 'RBEME1462.JPG'
NEW_IMAGE = root_folder / 'RBEME1462_edited.jpg'

# Open an image file
pil_img = Image.open(img_path)
width, height = pil_img.size
exif = pil_img.info['exif']


# print(f'Original image size: {width} x {height}')

# width -> new width
# height -> x

new_width = int(width * 0.5)
new_height = int(height * 0.5)

print(f'New image size: {new_width} x {new_height}')
print(f'Original image size: {width} x {height}')

new_img = pil_img.resize((new_width, new_height))
new_img.save(NEW_IMAGE,
               exif=exif,
               optimize=True,
               quality=85,
               )