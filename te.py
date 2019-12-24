try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

img = Image.open('image.jpg')
width, height = img.size
print(img.size)
area = (0,height*2/3, width, height) 
img = img.crop(area)
img.save("crop_pic.jpg")

