import pytest
from main import *

def test_Tester(capfd):
    print("Hello World!")
    out, err = capfd.readouterr()
    assert out == "Hello World!\n"
def test_CursorUp():
    assert cursorUp(0) == -1
    assert cursorUp(-1) == -1
    assert cursorUp(-100) == -1
    assert cursorUp(0.1) == -1
    assert cursorUp("N") == -1
    assert cursorUp('f') == -1
    assert cursorUp([1,2]) == -1
    assert cursorUp(1) == 0
    assert cursorUp(5) == 0
def test_CursorDown():
    assert cursorDown(0) == -1
    assert cursorDown(-100) == -1
    assert cursorDown(-1) == -1
    assert cursorDown(0.1) == -1
    assert cursorDown("N") == -1
    assert cursorDown('f') == -1
    assert cursorDown([1,2]) == -1
    assert cursorDown(1) == 0
    assert cursorDown(5) == 0
def test_CursorRight():
    assert cursorRight(0) == -1
    assert cursorRight(-1) == -1
    assert cursorRight(-100) == -1
    assert cursorRight(0.1) == -1
    assert cursorRight("N") == -1
    assert cursorRight('f') == -1
    assert cursorRight([1,2]) == -1
    assert cursorRight(1) == 0
    assert cursorRight(5) == 0
def test_CursorLeft():
    assert cursorLeft(0) == -1
    assert cursorLeft(-1) == -1
    assert cursorLeft(-100) == -1
    assert cursorLeft(0.1) == -1
    assert cursorLeft("N") == -1
    assert cursorLeft('f') == -1
    assert cursorLeft([1,2]) == -1
    assert cursorLeft(1) == 0
    assert cursorLeft(5) == 0
def test_SetColor():
    assert setColor("Red")==0
    print("Red")
    assert setColor("black")==0
    print("black")
    assert setColor("WhItE")==0
    print("WhItE")
    assert setColor("Green")==0
    print("Green")
    assert setColor("Yellow")==0
    print("Yellow")
    assert setColor("Blue")==0
    print("Blue")
    assert setColor("Magenta")==0
    print("Magenta")
    assert setColor("Cyan")==0
    print("Cyan")
    assert setColor("RESET")==0
    print("RESET")
    assert setColor("Gren")==-1
    assert setColor("unknown")==-1
    assert setColor(6)==-1
    assert setColor("R")==-1
    assert setColor(["Hi","Bye"])==-1
    assert setColor(0.1)==-1
    assert setColor('f')==-1
def test_printList(capfd):
    arr =["Choice1","Choice2","Choice3"]
    printList(arr)
    out, err = capfd.readouterr()
    assert out == "  Choice1\n\r  Choice2\n\r  Choice3\n\r"
def test_Single(capfd):
    valArray=["Choice1","Choice2","Choice3"]
    assert multiChoice(valArray,"Red","Text","fx","Magenta")== -1
def test_hideCursor(capfd):
    hideCursor()
    out, err = capfd.readouterr()
    assert out == '\x1b[?25l'

def test_resetCursor(capfd):
    resetCursor()
    out, err = capfd.readouterr()
    assert out == "\x1b[?0l"

