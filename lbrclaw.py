from pyautogui import screenshot, press, mouseDown, mouseUp
import numpy as np
from time import sleep


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    r, g, b = (int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
    return r, g, b


def getvariation(*ints):
    if ints <= 11:
        lowint = int
        highint = ints + 21
    elif ints >= 245:
        lowint = ints - 20
        highint = ints
    else:
        lowint = ints - 10
        highint = ints + 11
    result = list(range(lowint, highint))
    return result


def press_space():
    press('space')
    return


def pixel_checksum(left, top, right, bottom):
    im = screenshot(region=(left, top, right, bottom))
    arr = np.array(im)
    checksum = np.sum(arr)
    return checksum


def PixelSearch(left, top, right, bottom, color):
    im = screenshot(region=(left, top, right, bottom))
    image = im.convert('RGB')
    width, height = image.size
    for lr in range(width):
        for tb in range(height):
            r, g, b = image.getpixel((lr, tb))
            if (r, g, b) == color:
                return lr, tb
    return None


mouseDown(500, 370)
sleep(0.25)  # Hold the click for 0.5 seconds
mouseUp(500, 370)


top, left, right, bottom = 510, 500, 900, 250
top2, left2, right2, bottom2 = 500, 500, 50, 50


clawhex = '#5A6988'
hex_colors = ['#F2AF1B', '#FF0044', '#F4B41B', '#FFFFFF'] #hardware accep on # cursed cheese, gem, cheese, anything
#hex_colors = ['#F18D1A', '#FE0043', '#F3B31A', '#FEFEFE'] #hardware accel off # cursed cheese, gem, cheese, anything
succeed = True
while succeed:
    result1 = PixelSearch(left, top, right, bottom, hex_to_rgb(hex_colors[1]))
    if result1 is not None:
        print("Gem found at:", result1)
        x, _ = result1
        x = x + left
        _ = _ + top
        left1, top1, right1, bottom1 = x - 1, 410 - 30, 1, 200
        initialimage1 = pixel_checksum(left1, top1, right1, bottom1)
        print(initialimage1)
        loop2 = True
        while loop2:
            newimage1 = pixel_checksum(left1, top1, right1, bottom1)
            if newimage1 != initialimage1:
                print(newimage1)
                mouseDown(500, 370)
                sleep(0.1)
                mouseUp(500, 370)
                initialimage3 = pixel_checksum(top2, left2, right2, bottom2)
                print("clawcheckini", initialimage3)
                sleep(3)
                newimage3 = pixel_checksum(top2, left2, right2, bottom2)
                if initialimage3 != newimage3:
                    #print("clawchecknew", newimage3)
                    #sleep(0.1)
                    #mouseDown(500, 370)
                    #sleep(0.25)
                    #mouseUp(500, 370)
                    loop2 = False
                    succeed = True
                break
    else:
        for hex_color in hex_colors[0:] + hex_colors[2:] + hex_colors[3:]:
            try:
                color = hex_to_rgb(hex_color)
                result2 = PixelSearch(left, top, right, bottom, color)
                if result2 is not None:
                    print("Pixel found for color:", hex_color, "at:", result2)
                    x, _ = result2
                    x = x + left
                    _ = _ + top
                    left1, top1, right1, bottom1 = x - 1, 410 - 30, 1, 200
                    #im = screenshot(region=(left1, top1, right1, bottom1))
                    #screenshot_path = r"C:\Users\micha\OneDrive\Desktop\screenshot.png"
                    #im.save(screenshot_path)
                    initialimage2 = pixel_checksum(left1, top1, right1, bottom1)
                    print(initialimage2)
                    loop3 = True
                    while loop3:
                        newimage2 = pixel_checksum(left1, top1, right1, bottom1)
                        if newimage2 != initialimage2:
                            print(newimage2)
                            mouseDown(500, 370)
                            sleep(0.1)
                            mouseUp(500, 370)
                            initialimage4 = pixel_checksum(top2, left2, right2, bottom2)
                            print("clawcheck2ini", initialimage4)
                            sleep(3)
                            newimage4 = pixel_checksum(top2, left2, right2, bottom2)
                            if initialimage4 != newimage4:
                                #print("clawcheck2new", newimage4)
                                #sleep(0.1)
                                #mouseDown(500, 370)
                                #sleep(0.25)
                                #mouseUp(500, 370)
                                loop3 = False
                                succeed = True
                            break
                    break
            except Exception as e:

                continue
            else:
                print("Pixel:", hex_color, " not found")
                succeed = True
                continue
                break


