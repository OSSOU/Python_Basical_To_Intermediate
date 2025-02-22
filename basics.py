import time
import pyautogui

def screenshot():
    name = int(round(time.time()*1000))
    name = "D:/Formation Dosjos/Udemy/Python/20_Python_Projects/{}.png".format(name)
    time.sleep(5)
    img = pyautogui.screenshot("test.png")
    img.show()

screenshot()
