try:
    from PIL import Image
except ImportError:
    import Image
from picamera import PiCamera
from time import sleep
from passporteye import read_mrz
from scanText import readFile
import subprocess
import time
import pytesseract

def main():
    while True:
        camera = PiCamera()

        camera.start_preview()
        sleep(3)
        camera.capture('/home/pi/Desktop/myFolder/a.jpg')
        camera.stop_preview()
        camera.close() 

        img = Image.open('a.jpg')
        width, height = img.size
        area = (0, height*2/3, width, height-10)
        img = img.crop(area)
        img.save("crop_pic.jpg")
        f = pytesseract.image_to_string(img)
        code =""
        z=""
        print(f)
        for z in f.splitlines():
            if('<' in z):
                code += z.replace(" ", "")
                code += '\n'
        print(code)
        result = readFile(code)
        print(result)
        if result=="Done": break
        print("\n")
if __name__ == "__main__":
    main()
