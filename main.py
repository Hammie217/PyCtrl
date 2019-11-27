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

    val -one integer greater than zero

    RETURNS

    0 for success and -1 for error
    """
    if isinstance(val, int) and val > 0:
        print_cursor_value(val, "A")
        return 0
    return -1


def cursorDown(val):
    """
    PURPOSE
 
    Moves console cursor down by defined value

    INPUT

    val -one integer greater than zero

    RETURNS

    0 for success and -1 for error
    """
    if isinstance(val, int) and val > 0:
        print_cursor_value(val, "B")
        return 0
    return -1


def cursorRight(val):
    """
    PURPOSE
 
    Moves console cursor right by defined value

    INPUT

    val -one integer greater than zero

    RETURNS

    0 for success and -1 for error
    """
    if isinstance(val, int) and val > 0:
        print_cursor_value(val, "C")
        return 0
    return -1


def cursorLeft(val):
    """
    PURPOSE
 
    Moves console cursor left by defined value

    INPUT

    val -one integer greater than zero

    RETURNS

    0 for success and -1 for error
    """
    if isinstance(val, int) and val > 0:
        print_cursor_value(val, "D")
        return 0
    return -1


def print_cursor_value(val, letter):
    """
    PURPOSE
 
    Function designed for printing special [ANSI Escape Codes](https://en.wikipedia.org/wiki/ANSI_escape_code#Terminal_input_sequences). The value and letter are concatenated to the escape character before being printed to the console.

    INPUT

    val - no verification and validation
    letter - no verification and validation

    RETURNS

    None
    """
    unicode_prefix = u"\u001b["
    print(f'{unicode_prefix}{val}{letter}', end='')


def setColor(val):
    """
    PURPOSE
 
    Defines the console cursor color

    INPUT

    val - one string from list (Black, Red, Green, Yellow, Blue, Magenta, Cyan, White, Reset)

    RETURNS

    0 for success and -1 for error
    """
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
    """
    PURPOSE
 
    Prints array passed with one element on each line before returning.

    INPUT

    arr - array of strings to be printed

    RETURNS

    None
    """
    for word in arr:
        print(f"  {word}", end="\n\r")


def hideCursor():
    """
    PURPOSE
 
    Hide the console cursor.

    INPUT

    None

    RETURNS

    None
    """
    print("\u001b[?25l", end='')


def resetCursor():
    """
    PURPOSE
 
    Resets the console cursor to on.

    INPUT

    None

    RETURNS

    None
    """
    print("\u001b[?0l", end='')



def onCharUp(cursorColor, position):
    """
    PURPOSE
 
    \warning {This function is designed to be private, it may be used elswhere if useful hence the lack of attempt to hide}

    This function sets the curson color as defined on input as well as moving the cursor up as long as the passed position is not currently greater than zero.

    INPUT

    cursorColor - Colors defined in setColor
    position - current cursor position

    RETURNS
    
    position - new position after movement
    """
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
    """
    PURPOSE
 
    \warning {This function is designed to be private, it may be used elswhere if useful hence the lack of attempt to hide}

    This function sets the curson color as defined on input as well as moving the cursor down as long as the passed position is not currently at the length of the passed array length.

    INPUT

    arrL - Length of array printed
    cursorColor - Colors defined in setColor
    position - current cursor position

    RETURNS
    
    position - new position after movement
    """
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
    """
    PURPOSE
 
    Gets single key input from the user

    INPUT

    None

    RETURNS

    key buffer after press
    """
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
    cursorUp(len(arr))

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


# valArray=["Choice1","Choice2","Choice3"]
# print(*multiChoice(valArray,"Red","Text","f","Magenta"), sep='\n')
# valArray=["Choice1","Choice2","Choice3"]
# print(singleChoice(valArray,"Magenta","Text"),)
