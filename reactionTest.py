from time import sleep

import dxcam
import numpy as np
import matplotlib.pyplot as plt

camera = dxcam.create(output_idx=0, output_color="GRAY",max_buffer_len=2)
left, top =200, 200
right, bottom = left + 1, top + 1
region = (left, top, right, bottom)
monitor ={"top": top, "left": left, "width": 1, "height": 1}
#img = camera.grab(region=region)
#print(img[0][0][0])
#
#
#plt.imshow(img)
#plt.show()

import keyboard  # using module keyboardc
import mouse

#camera.start(region=region, target_fps = 120)

mouse.move(350, 350)
mouse.click('left')
import mss


while True:

    #if keyboard.is_pressed("c"):  # if key 'q' is pressed
    #    image = camera.get_latest_frame()  # Will block until new frame available
    #    print(image)

    #image = camera.grab(region=region)
    with mss.mss() as sct:
        image = sct.grab(monitor)
        if image.raw == b'j\xdbK\xff':
            mouse.click('left')
            sleep(1)
            mouse.click('left')
    #if image is not None and image[0][0][0] == 163:
    #    mouse.click('left')
    #    sleep(1)
    #    mouse.click('left')




    #blue 116
    #red 90
    #green 163


    if keyboard.is_pressed("esc"):  # if key 'q' is pressed
        camera.stop()
        print('You Pressed the ESC Key!')
        break  # finishing the loop
