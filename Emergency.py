side = -1
flag = False


def emergency_detect():
    global side
    global flag

    while True:
        x = int(input())
        if x >= 1 and x <= 4:
            side = x
            flag = True
        elif x == 0:
            side = -1
            flag = False
