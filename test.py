import pytest
from main import *

def testCursorUp():
    assert cursorUp(0) == -1
    assert cursorUp(-1) == -1
    assert cursorUp(-100) == -1
    assert cursorUp(0.1) == -1
    assert cursorUp("N") == -1
    assert cursorUp('f') == -1
    assert cursorUp([1,2]) == -1
    assert cursorUp(1) == 0
    assert cursorUp(5) == 0
def testCursorDown():
    assert cursorDown(0) == -1
    assert cursorDown(-100) == -1
    assert cursorDown(-1) == -1
    assert cursorDown(0.1) == -1
    assert cursorDown("N") == -1
    assert cursorDown('f') == -1
    assert cursorDown([1,2]) == -1
    assert cursorDown(1) == 0
    assert cursorDown(5) == 0
def testCursorRight():
    assert cursorRight(0) == -1
    assert cursorRight(-1) == -1
    assert cursorRight(-100) == -1
    assert cursorRight(0.1) == -1
    assert cursorRight("N") == -1
    assert cursorRight('f') == -1
    assert cursorRight([1,2]) == -1
    assert cursorRight(1) == 0
    assert cursorRight(5) == 0
def testCursorLeft():
    assert cursorLeft(0) == -1
    assert cursorLeft(-1) == -1
    assert cursorLeft(-100) == -1
    assert cursorLeft(0.1) == -1
    assert cursorLeft("N") == -1
    assert cursorLeft('f') == -1
    assert cursorLeft([1,2]) == -1
    assert cursorLeft(1) == 0
    assert cursorLeft(5) == 0
def testSetColor():
    assert setColor("Red")==0
    print("Red")
    assert setColor("black")==0
    print("black")
    assert setColor("WhItE")==0
    print("WhItE")
    assert setColor("Green")==0
    print("Green")
    assert setColor("RESET")==0
    print("RESET")
    assert setColor("Gren")==-1
    assert setColor("unknown")==-1
    assert setColor(6)==-1
    assert setColor("R")==-1
    assert setColor(["Hi","Bye"])==-1
    assert setColor(0.1)==-1
    assert setColor('f')==-1



print("Initiating test")
testCursorUp()
testCursorDown()
testCursorRight()
testCursorLeft()
testSetColor()


print("Completed Test")