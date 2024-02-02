from PIL import Image, ImageEnhance, ImageFilter
import os

from PIL.Image import Image

path = './img'
pathOut = '/editedImg'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit: Image = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)
     
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
   
    clean_name: str = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')
