from passporteye import read_mrz
from picamera import PiCamera
from time import sleep

while True:
    camera = PiCamera()
    camera.start_preview()
    sleep(3)
    camera.capture('/home/pi/Desktop/myFolder/a.jpg')
    camera.stop_preview()
    camera.close() 

    mrz = read_mrz('a.jpg')
    print(mrz)
    print('\n')
    if not (mrz=='none'): 
        print("Done")
        break
