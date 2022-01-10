import math
from time import sleep, time

from djitellopy import tello
import movement as move

me = tello.Tello()
me.connect()
print(me.get_battery())

me.takeoff()
me.send_rc_control(0, 0, 10 ,0)
sleep(2)

x, y = 0, 0


def hover():
    while me.is_flying:
        moving()


def moving():
    global x, y

    if x == 0 and y == 0:
        moveForward(y)
    elif x == 5 and y == 0:
        rotateClockwise()
        backToBase(x)
    else:
        if y == 4:
            rotateAndDetect()

            rotateClockwise()
            move1Box(x)
            moveBackward(y)
        if y == 0:
            rotateAndDetect()
            rotateCounterClockwise()
            move1Box(x)
            moveForward(y)


def moveForward(y):
    me.send_rc_control(0, 50, 0, 0)
    sleep(4)
    y += 4


def moveBackward(y):
    me.send_rc_control(0, 50, 0, 0)
    sleep(4)
    y -= 4


def move1Box(x):
    me.send_rc_control(0, 50, 0, 0)
    sleep(1)
    x += 1


def rotateClockwise():
    me.rotate_clockwise(90)


def rotateCounterClockwise():
    me.rotate_counter_clockwise(90)


def backToBase(x):
    me.send_rc_control(0, 50, 0, 0)
    sleep(5)
    x -= 5


def rotateAndDetect():
    i = 0
    while i in range(4):
        me.rotate_clockwise(90)
        sur_time = time.time() + 15
        move.turnOnDetection(sur_time)
        i += 1
    '''
    if detect a person not wearing mask
    me.send_rc_control(0,0,0,0)
    aifan's part here
    '''
    # sleep(5)
