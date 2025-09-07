
from PIL import Image, ImageOps

img = Image.open(r'C:\Users\Lenovo\Downloads\MU.photo.jpg')
padded = ImageOps.expand(img, border=20, fill='black')
padded.show()