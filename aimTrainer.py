import dxcam
import keyboard  # using module keyboardc
import mouse
from matplotlib import pyplot as plt

camera = dxcam.create(output_idx=0, output_color="GRAY",max_buffer_len=2)
left, top =850, 190
right, bottom = 2560-850, 660
region = (left, top, right, bottom)
mouse.move(1280, 400)
mouse.click('left')
while True:

    #if keyboard.is_pressed("c"):  # if key 'q' is pressed
    #    image = camera.get_latest_frame()  # Will block until new frame available
    #    print(image)

    image = camera.grab(region=region)
    if image is not None:
        must_break = False
        for x in range(0,470,65):
            if must_break:
                break
            for y in range(0, 860, 65):
                if image[x][y][0] >= 120:
                    mouse.move(y+850, x+190)

                    mouse.click('left')

                    must_break = True
                    break


    #gray value <120 -> Target
    #target size >=65x65 pixel


    if keyboard.is_pressed("esc"):  # if key 'q' is pressed
        camera.stop()
        print('You Pressed the ESC Key!')
        break  # finishing the loop