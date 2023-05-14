# https://www.silvergames.com/en/piano-tiles-2
from pynput.mouse import Button, Controller
from PIL import ImageGrab
import keyboard
import time

mouse = Controller()
x1, y1 = (880, 790)
x2, y2 = (736, 791)
x3, y3 = (1028, 790)
x4, y4 = (1170, 790)
black = (0,0,0)
blue = (54,159,198)
add=236.97

time.sleep(5)

def start():
    screen = ImageGrab.grab()
    if screen.getpixel((x1, y1)) == blue:
        mouse.position = ((x1,y1))
        mouse.press(Button.left)
        mouse.release(Button.left)

    elif screen.getpixel((x2, y2)) == blue:
        mouse.position = ((x2,y2))
        mouse.press(Button.left)
        mouse.release(Button.left)

    elif screen.getpixel((x3, y3)) == blue:
        mouse.position = ((x3,y3))
        mouse.press(Button.left)
        mouse.release(Button.left)

    elif screen.getpixel((x4, y4)) == blue:
        mouse.position = ((x4,y4))
        mouse.press(Button.left)
        mouse.release(Button.left)

def play():
    screen = ImageGrab.grab()
    if screen.getpixel((x1, y1)) == black:
        mouse.position = ((x1,(y1+add)))
        mouse.press(Button.left)
        mouse.release(Button.left)

    elif screen.getpixel((x2, y2)) == black:
        mouse.position = ((x2,(y2+add)))
        mouse.press(Button.left)
        mouse.release(Button.left)

    elif screen.getpixel((x3, y3)) == black:
        mouse.position = ((x3,(y3+add)))
        mouse.press(Button.left)
        mouse.release(Button.left)

    elif screen.getpixel((x4, y4)) == black:
        mouse.position = ((x4,(y4+add)))
        mouse.press(Button.left)
        mouse.release(Button.left)

start()
while True:  
    play()
    if keyboard.is_pressed("q"):
        break
