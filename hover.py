import math
from tkinter import *
from time import sleep
import time
from djitellopy import tello
import movement as move

me = tello.Tello()

x, y = 0, 0
totalMaskCount = 1


def Hover(me):
    print("Hover is called.")
    while me.is_flying:
        moving()


def moving():
    global x, y
    print(x, y)
    print(totalMaskCount)
    if isMaskCount():
        if x == 0 and y == 0:
            moveForward()
            # rotateAndDetect()
        elif x == 5 and y == 0:
            rotateClockwise()
            backToBase()
        else:
            if y == 4:
                rotateAndDetect()
                rotateClockwise()
                move1Box()
                # added extra turn
                rotateClockwise()
                moveBackward()

            elif y == 0:
                rotateAndDetect()
                if not isMaskCount():
                    returntoBaseLand()
                rotateCounterClockwise()
                move1Box()
                # added extra turn
                rotateCounterClockwise()
                moveForward()

    elif not isMaskCount():
        returntoBaseLand()


def moveForward():
    global y
    me.send_rc_control(0, 50, 0, 0)
    sleep(4)
    y += 4
    print(y)


def moveBackward():
    global y
    print(
        'reverse'
    )
    me.send_rc_control(0, 50, 0, 0)
    sleep(4)
    y -= 4
    print(y)


def move1Box():
    global x
    me.send_rc_control(0, 30, 0, 0)
    sleep(3)
    x += 1
    print(x)


def rotateClockwise(r=90):
    me.rotate_clockwise(r)
    sleep(3)
    print("rotating CW 90")


def rotateCounterClockwise(r=90):
    me.rotate_counter_clockwise(r)
    sleep(3)
    print("rotating CCW 90")


def backToBase():
    global x
    print("Back to base")
    me.send_rc_control(0, 30, 0, 0)
    sleep(5)
    x -= 5
    print(x)
    me.rotate_clockwise(90)
    me.land()


def returntoBaseLand():
    print("returning to base")
    global y, x
    print(x, y)
    # me.flip_back()
    if y == 4:
        me.rotate_clockwise(180)
        me.send_rc_control(0, 50, 0, 0)
        sleep(4)
        rotateCounterClockwise()
        y -= 4
        print(y)
    else:
        rotateClockwise()

    if x > 0:
        me.send_rc_control(0, 30, 0, 0)
        sleep(x)
        x -= x
        print(x)
    me.send_rc_control(0, 0, 0, 0)
    sleep(3)
    me.land()


def isMaskCount():
    if totalMaskCount > 0:
        return True
    else:
        return False


def rotateAndDetect():
    i = 1
    print("detecting")
    global totalMaskCount
    while i in range(5):
        me.rotate_clockwise(90)
        sleep(3)
        sur_time = time.time() + 5

        result = move.turnOnDetection(sur_time, me)
        print("rotation .{}".format(i))
        if result:
            me.send_rc_control(0, 0, -30, 0)
            sleep(2)
            me.send_rc_control(0, 0, 0, 0)
            sleep(5)
            me.send_rc_control(0, 0, 30, 0)
            sleep(2)
            totalMaskCount -= 1

        if (isMaskCount() == False):
            me.rotate_counter_clockwise(i * 90)
            break

        i += 1
