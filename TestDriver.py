from time import sleep

import hover as h


def main():
    h.Hover(me)


me = h.me
me.connect()
print(me.get_battery())

me.takeoff()
me.send_rc_control(0, 0, 0, 0)
sleep(3)
me.streamon()
if __name__ == '__main__':
    main()
