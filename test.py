import pyautogui
import sys
import time
from PIL import Image
import numpy
def getStatus(s):
    p = Image.open(s)
    php = p.crop((9,13,100,14))
    phpdata = numpy.asarray(php)
    phplength = 0
    phpblue = 0
    phpempty = 0
    for i in phpdata:
        phplength = len(i)
        for y in i:
            basic = 189
            if y[2] <= 190:
                phpblue = phpblue + 1
            else:
                phpempty = phpempty + 1
    phppercent = phpblue/phplength*100

    pmp = p.crop((9,25,100,26))
    pmpdata = numpy.asarray(pmp)
    pmplength = 0
    pmpblue = 0
    pmpempty = 0
    for i in pmpdata:
        pmplength = len(i)
        for y in i:
            basic = 189
            if y[2] <= 190:
                pmpblue = pmpblue + 1
            else:
                pmpempty = pmpempty + 1
    pmppercent = pmpblue/pmplength*100

    return int(phppercent), int(pmppercent)

def checkBattle():
    battle = pyautogui.locateCenterOnScreen("battle2.png")
    if battle == None:
        return True
    else:
        return False
def checkBattlemaru():
    battle = pyautogui.locateCenterOnScreen("battlemaru.jpg")
    if battle == None:
        return True
    else:
        return battle
vnc = pyautogui.getWindowsWithTitle("WIN-BB")[0]
while True:
    status = pyautogui.screenshot(region=(vnc.left+40,vnc.top+90, 110, 50))
    status.save("test.png")
    while checkBattle():
        pyautogui.keyDown('f6') #prayy
        pyautogui.keyUp('f6') #prayy

        time.sleep(0.1)
        if checkBattle():
            pyautogui.mouseDown()
            pyautogui.mouseUp()
        # else:
        #     break
        # time.sleep(0.3)
        # pyautogui.keyDown('f6') #prayy
        # pyautogui.keyUp('f6') #prayy

    hp, mp = getStatus("test.png")
    recovery = False
    print(hp, mp)
    if mp < 80 or hp < 80:
        recovery = True
    while recovery:
        status = pyautogui.screenshot(region=(vnc.left+40,vnc.top+90, 110, 50))
        status.save("test.png")
        hp, mp = getStatus("test.png")
        if mp < 80:
            pyautogui.keyDown('f7') #prayy
            pyautogui.keyUp('f7') #prayy
            time.sleep(0.3)

        if hp < 80:
            pyautogui.keyDown('f8') #prayy
            pyautogui.keyUp('f8') #prayy
            time.sleep(0.3)     
        
        print(hp,mp)
        if mp > 90 and hp > 90:
            recovery = False

        # hp = 8,12 100,13 #189,21,3
        # mp = 8,15 100,15 #2,86,189
        # empty = 227,234,235

    # finally:
    #     notEnd = True
    #     while notEnd:
    #         pass



    # 30,31 #49A3FE
