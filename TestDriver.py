import hover as h


def main():
    h.Hover(me)


me = h.me
me.connect()
print(me.get_battery())

me.takeoff()
if __name__ == '__main__':
    main()
