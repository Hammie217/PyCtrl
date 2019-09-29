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
    assert cursorLeft(0) == -1
    assert cursorLeft(-1) == -1
    assert cursorLeft(-100) == -1
    assert cursorLeft(0.1) == -1
    assert cursorLeft("N") == -1
    assert cursorLeft('f') == -1
    assert cursorLeft([1,2]) == -1
    assert cursorLeft(1) == 0
    assert cursorLeft(5) == 0
def testCursorRight():
    assert cursorUp(0) == -1
    assert cursorUp(-1) == -1
    assert cursorUp(-100) == -1
    assert cursorUp(0.1) == -1
    assert cursorUp("N") == -1
    assert cursorUp('f') == -1
    assert cursorUp([1,2]) == -1
    assert cursorUp(1) == 0
    assert cursorUp(5) == 0
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
    print("Gren")
    assert setColor("unknown")==-1
    print("UNKNOWN")
    assert setColor(6)==-1
    print("6")
    assert setColor("R")==-1
    print("!\"red!\"")

print("Initiating test \n\n\n\n\n\n")
testCursorUp()
testCursorLeft()
testSetColor()

print("Completed Test")