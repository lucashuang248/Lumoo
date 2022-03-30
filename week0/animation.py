import time

ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
RESET_COLOR = u"\u001B[0m\u001B[2D"

def animation_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(sp + "  _/---\_   ")
    print(sp + " /  . .  \   ")
    print(sp + " |   <   |   ")
    print(sp + " \ |___| / ")
    print(sp + "  \_____/  ")
    print(sp + "    | |  ")
    print(RESET_COLOR)

def animation():
    start = 0
    distance = 60
    step = 2 

    for position in range(start, distance, step):
        animation_print(position)
        time.sleep(.1)