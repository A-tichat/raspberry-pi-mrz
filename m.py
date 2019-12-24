from PIL import Image
from psMRZ import mrz
from picamera import PiCamera
from time import sleep
import time
import pytesseract

if __name__ == "__main__":
    while True:
        try:
            camera = PiCamera()
            #camera.start_preview()
            #sleep(3)
            camera.capture('/home/pi/Desktop/myFolder/temp.jpg')
            #camera.stop_preview()
            camera.close() 
            img = Image.open('temp.jpg')
            #width, height = img.size
            #area = (0, height*2/3, width, height-10)
            #img = img.crop(area)
            #img.save("crop_pic.jpg")
            f = pytesseract.image_to_string(img)
            code=""
            d=""
            for d in f.splitlines():
                if '<' in d:
                    while ' 'in d:
                        stlen = d.find(' ')
                        d=d[:stlen]+d[stlen+1:]
                    code+=d[:44]
                    code+='\n'
            print(code)
            p1 = mrz(code)
            p1.result()
            print('\n')
            #print(p1.__dict__)
            break
        except ValueError as err:
            print(err)
            f.close()
            pass

        print ("retry")
    f.close()
    print("finish!")
