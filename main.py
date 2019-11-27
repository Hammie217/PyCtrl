"""@package docstring
Documentation for this module.
 
More details.
"""
import sys, tty, termios


def cursorUp(val):
    """
    PURPOSE
 
    Moves console cursor up by defined value

    INPUT

    one integer greater than zero

    RETURNS

    0 for success and -1 for error
    """
    if isinstance(val, int) and val > 0:
        print_cursor_value(val, "A")
        return 0
    return -1


def cursorDown(val):
    if isinstance(val, int) and val > 0:
        print_cursor_value(val, "B")
        return 0
    return -1


def cursorRight(val):
    if isinstance(val, int) and val > 0:
        print_cursor_value(val, "C")
        return 0
    return -1


def cursorLeft(val):
    if isinstance(val, int) and val > 0:
        print_cursor_value(val, "D")
        return 0
    return -1


def print_cursor_value(val, letter):
    unicode_prefix = u"\u001b["
    print(f'{unicode_prefix}{val}{letter}', end='')


def setColor(val):
    if isinstance(val, str):
        val = val.upper()
        colors = {"BLACK": "\u001b[30m",
                  "RED": "\u001b[31m",
                  "GREEN": "\u001b[32m",
                  "YELLOW": "\u001b[33m",
                  "BLUE": "\u001b[34m",
                  "MAGENTA": "\u001b[35m",
                  "CYAN": "\u001b[36m",
                  "WHITE": "\u001b[37m",
                  "RESET": "\u001b[0m"}
        if val in colors.keys():
            print(colors[val], end="")
            return 0
    return -1


def printList(arr):
    for word in arr:
        print(f"  {word}", end="\n\r")
    cursorUp(len(arr))


def hideCursor():
    print("\u001b[?25l", end='')


def resetCursor():
    print("\u001b[?0l", end='')


def onCharUp(cursorColor, position):
    if position > 0:
        print(" ", end="")
        cursorLeft(1)
        cursorUp(1)
        setColor(cursorColor)
        print(">", end="")
        setColor("Reset")
        cursorLeft(1)
        position -= 1
    return position



def onDownChar(arrL, cursorColor, position):
    if position < arrL:
        print(" ", end="")
        cursorLeft(1)
        cursorDown(1)
        setColor(cursorColor)
        print(">", end="")
        setColor("Reset")
        cursorLeft(1)
        position += 1
    return position


def get_input_char():
    return ord(sys.stdin.read(1))


def singleChoice(arr, cursorColor="Blue", textOrVal="Val"):
    # save terminal settings
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    # set terminal to raw mode
    tty.setraw(sys.stdin)
    # read output
    charIn = 0
    printList(arr)
    hideCursor()
    position = 0
    setColor(cursorColor)
    print(">", end="")
    setColor("Reset")
    cursorLeft(1)
    enter_not_pressed = charIn != 13
    while enter_not_pressed:
        sys.stdout.flush()
        charIn = get_input_char()  # Get input
        if charIn == 27:  # ESC pressed
            charIn = get_input_char()
            if charIn == 91:  # [ pressed
                charIn = get_input_char()  # Get input
                if charIn == 65:  # Up
                    position = onCharUp(cursorColor, position)
                elif charIn == 66:  # Down
                    position = onDownChar(len(arr)-1, cursorColor, position)
        enter_not_pressed = charIn != 13
    cursorDown(len(arr) - position)
    # Set terminal style back to normal
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    resetCursor()
    if textOrVal.upper() == "TEXT":
        return arr[position]
    else:
        return position


def multiChoice(arr, cursorColor="Blue", textOrVal="Val", tickOrCross="T", otherColor="Green"):
    if (len(tickOrCross) > 1):
        print("Error: character " + tickOrCross + " Too long")
        return -1
    # save terminal settings
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    # set terminal to raw mode
    tty.setraw(sys.stdin)
    # read output
    charIn = 0
    printList(arr)
    print("  Done", end="\n\r")
    hideCursor()
    cursorUp(len(arr) + 1)
    position = 0
    setColor(cursorColor)
    print(">", end="")
    setColor("Reset")
    cursorLeft(1)
    positionList = []
    ended = False
    while ended != True:  # whilst enter not pressed
        # draw arrows at selected positions
        currpos = position
        cursorUp(position)
        for i in range(0, len(arr)):
            if i in positionList:
                cursorRight(1)
                if tickOrCross == 'X':
                    setColor("Red")
                    print("✗", end="\r\n")
                elif tickOrCross == 'T':
                    setColor("Green")
                    print("✓", end="\r\n")
                else:
                    setColor(otherColor)
                    print(tickOrCross, end="\r\n")
                setColor("Reset")
            else:
                cursorRight(1)
                print(" ", end="\r\n")
        cursorUp(len(arr) - currpos)

        sys.stdout.flush()
        charIn = ord(sys.stdin.read(1))  # Get input
        
        if charIn == 13:#Enter
            if position == len(arr):
                ended = True
                break
            if position not in positionList:
                positionList.append(position)
            else:
                positionList.remove(position)

        elif charIn == 27:  # ESC pressed
            charIn = ord(sys.stdin.read(1))
            if charIn == 91:  # [ pressed
                charIn = ord(sys.stdin.read(1))  # Get input
                if charIn == 65:  # Up
                    position = onCharUp(cursorColor, position)
                elif charIn == 66:  # Down
                    position = onDownChar(len(arr), cursorColor, position)
    cursorDown(len(arr) - position)
    print("", end='\n\r')
    # Set terminal style back to normal
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if textOrVal.upper() == "TEXT":
        posListText = []
        for i in positionList:
            posListText.append(arr[i])
        return posListText
    else:
        return positionList


#valArray=["Choice1","Choice2","Choice3"]
#print(*multiChoice(valArray,"Red","Text","f","Magenta"), sep='\n')
#valArray=["Choice1","Choice2","Choice3"]
#print(singleChoice(valArray,"Magenta","Text"),)#
