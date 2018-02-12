# This file is only to send the signal to arduino board to set the proper direction
def set(direction):
    if direction == 0:
        print('A')
    elif direction == 1:
        print('B')
    elif direction == 2:
        print('C')
    elif direction == 3:
        print('D')
    else:
        print('Invalid Select')