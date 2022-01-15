import math
from tkinter import *
from time import sleep, time

from djitellopy import tello
import movement as move

me = tello.Tello()
# me.connect()
# print(me.get_battery())
#
# me.takeoff()
# sleep(5)
# #me.stream_on()
# #me.send_rc_control(0, 10, 0, 0)
# #me.flip_forward()


x, y = 0, 0
totalMaskCount = 5


def Hover(me):
    print("Hover is called.")
    while me.is_flying:
        moving()


def moving():
    global x, y

    if isMaskCount():
        if x == 0 and y == 0:
            moveForward(y)
            rotateAndDetect()
        elif x == 5 and y == 0:
            rotateClockwise()
            backToBase(x)
        else:
            if y == 4:
                rotateAndDetect()
                rotateClockwise()
                move1Box(x)
                # added extra turn
                rotateClockwise()
                moveBackward(y)
            if y == 0:
                rotateAndDetect()
                rotateCounterClockwise()
                move1Box(x)
                # added extra turn
                rotateCounterClockwise()
                moveForward(y)

    elif not isMaskCount():
        returntoBaseLand(x, y)


def moveForward(y):
    me.send_rc_control(0, 10, 0, 0)
    sleep(4)
    y += 4


def moveBackward(y):
    me.send_rc_control(0, 10, 0, 0)
    sleep(4)
    y -= 4


def move1Box(x):
    me.send_rc_control(0, 10, 0, 0)
    sleep(1)
    x += 1


def rotateClockwise(r=90):
    me.rotate_clockwise(r)


def rotateCounterClockwise(r=90):
    me.rotate_counter_clockwise(r)


def backToBase(x):
    me.send_rc_control(0, 10, 0, 0)
    sleep(5)
    x -= 5
    me.rotate_clockwise(90)
    me.land()


def returntoBaseLand(x, y):
    me.flip_back()
    if y == 4:
        me.send_rc_control(0, -10, 0, 0)
        sleep(y)
        rotateCounterClockwise()
        y -= y
    else:
        rotateClockwise()

    if x > 0:
        me.send_rc_control(0, 10, 0, 0)
        sleep(x)
        x -= x

    me.land()


def isMaskCount():
    if totalMaskCount > 0:
        return True
    else:
        return False


def rotateAndDetect():
    i = 1
    global totalMaskCount
    while i in range(5):
        me.rotate_clockwise(90)
        sur_time = time.time() + 15
        result = move.turnOnDetection(sur_time)
        if result:
            me.send_rc_control(0, 0, -10, 0)
            sleep(2)
            me.send_rc_control(0, 0, 0, 0)
            sleep(10)
            me.send_rc_control(0, 0, 10, 0)
            sleep(2)
            totalMaskCount -= 1

        if (isMaskCount() == False):
            me.rotate_counter_clockwise(i * 90)
            break

        i += 1
    '''
    if detect a person not wearing mask
    me.send_rc_control(0,0,0,0)
    aifan's part here
    '''
    # sleep(5)


