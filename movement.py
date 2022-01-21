import cv2
from djitellopy import tello
from time import sleep
import time
import detect_mask_video as detect


i = 0

#cap = cv2.VideoCapture(0)

# Travel to/from starting checkpoint 0 from/to the charging base
frombase = ["forward", 50]
tobase = ["forward", 50]

# Flight path to Checkpoint 1 to 5 and back to Checkpoint 0 sequentially
checkpoint = [[1, "cw", 0, "forward", 100], [2, "cw", 180, "forward", 100]]


def turnOnDetection(t_end, me):
    global i
    while time.time() < t_end:

        #_, frame = cap.read()
        frame = me.get_frame_read().frame

        frame = cv2.resize(frame, (360, 240))

        newframe = detect.start_detect(frame, i)

        if (newframe == True):
            # do landing procedure
            return True
            break
        elif (newframe == "Mask"):
            i = 0
        elif (newframe == "NoMask"):
            i += 1

        cv2.imshow("Output", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # me.land()
            break
    return False

'''
def main():
    me.move_up(100)
    me.move(frombase[0], frombase[1])

    for i in range (len(checkpoint)):

        if(checkpoint[i][1] == "cw"):
            me.rotate_clockwise(checkpoint[i][2])
        elif(checkpoint[i][1] == "ccw"):
            me.rotate_counterclockwise(checkpoint[i][2])
        else:
            print("Wrong command")
            print("Landing")
            me.land()

        if(checkpoint[i][3] == "forward"):
            me.move_forward(checkpoint[i][4])
        elif(checkpoint[i][3] == "backward"):
            me.move_back(checkpoint[i][4])
        elif(checkpoint[i][3] == "left"):
            me.move_left(checkpoint[i][4])
        elif(checkpoint[i][3] == "right"):
            me.move_right(checkpoint[i][4])

        sur_time = time.time() + 15
        turnOnDetection(sur_time)


    me.move(tobase[0], tobase[1])
    me.land()


main()
'''





