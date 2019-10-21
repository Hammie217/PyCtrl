import pytest
from main import *


@pytest.mark.parametrize("test_input,expected",
                         [(0, -1), (-1, -1), (-100, -1),
                          (0.1, -1), ("N", -1), ('f', -1), ([1, 2], -1), (1, 0), (5, 0)])
def test_Cursor_up_down_left_right(test_input, expected):
    assert cursorUp(test_input) == expected
    assert cursorDown(test_input) == expected
    assert cursorRight(test_input) == expected
    assert cursorLeft(test_input) == expected


def test_Cursor_methods_print_output(capfd):
    test_input = 1
    cursorUp(test_input)
    cursorDown(test_input)
    cursorRight(test_input)
    cursorLeft(test_input)

    out, err = capfd.readouterr()
    assert get_print_cursor_value(1, "A") in out
    assert get_print_cursor_value(1, "B") in out
    assert get_print_cursor_value(1, "C") in out
    assert get_print_cursor_value(1, "D") in out


def test_print_cursor_value_prints_cursor_log(capfd):
    print_cursor_value("hello", "A")
    out, err = capfd.readouterr()
    assert out == "\x1b[helloA"


def get_print_cursor_value(val, letter):
    unicode_prefix = u"\u001b["
    return f'{unicode_prefix}{val}{letter}'


@pytest.mark.parametrize("test_input,expected",
                         [("Red", 0), ("black", 0), ("WhItE", 0), ("Green", 0), ("RESET", 0), ("Gren", -1),
                          ("unknown", -1), (6, -1), ("R", -1), (["Hi", "Bye"], -1), (0.1, -1), ('f', -1),
                          ])
def test_SetColor(test_input, expected):
    assert setColor(test_input) == expected
    print(test_input)


def test_printList_prints_words_to_std_out(capfd):
    arr = ["Choice1", "Choice2", "Choice3"]
    printList(arr)
    out, err = capfd.readouterr()
    assert out == "  Choice1\n\r  Choice2\n\r  Choice3\n\r"


def test_Single(capfd):
    valArray = ["Choice1", "Choice2", "Choice3"]
    assert multiChoice(valArray, "Red", "Text", "fx", "Magenta") == -1


def test_hideCursor(capfd):
    hideCursor()
    out, err = capfd.readouterr()
    assert "\u001b[?25l" in out


def test_resetCursor(capfd):
    resetCursor()
    out, err = capfd.readouterr()
    assert "\u001b[?0l" in out
