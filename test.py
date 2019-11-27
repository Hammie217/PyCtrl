from unittest import mock

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
                         [("Red", 0), ("black", 0), ("YELLOW", 0), ("MAGENTA", 0), ("CYAN", 0), ("WhItE", 0),
                          ("Green", 0), ("RESET", 0), ("Gren", -1),
                          ("unknown", -1), (6, -1), ("R", -1), (["Hi", "Bye"], -1), (0.1, -1), ('f', -1),
                          ])
def test_SetColor(test_input, expected):
    assert setColor(test_input) == expected
    print(test_input)


def test_hideCursor(capfd):
    hideCursor()
    out, err = capfd.readouterr()
    assert "\u001b[?25l" in out


def test_resetCursor(capfd):
    resetCursor()
    out, err = capfd.readouterr()
    assert "\u001b[?0l" in out


def test_printList_prints_words_to_std_out(capfd):
    arr = ["Choice1", "Choice2", "Choice3"]
    printList(arr)
    out, err = capfd.readouterr()
    assert out == "  Choice1\n\r  Choice2\n\r  Choice3\n\r"


#--------------------------------MultiChoice--------------------------------#
@mock.patch("sys.stdin.fileno")
@mock.patch("sys.stdin.read")
@mock.patch("termios.tcgetattr")
@mock.patch("termios.tcsetattr")
@mock.patch("tty.setraw")
def test_multiChoice(mock_set_raw: mock.Mock,
                     mock_tc_get_attr: mock.Mock,
                     mock_tc_set_attr: mock.Mock,
                     mock_sys_read: mock.Mock,
                     mock_file_no: mock.Mock, capfd):
    valArray = ["Choice1", "Choice2", "Choice3"]
    char_down_sequence = [chr(27), chr(91), chr(66)] * 3
    mock_sys_read.side_effect = char_down_sequence + [chr(13)]

    result = multiChoice(valArray, "Red", "Text", "f", "Magenta")

    out, err = capfd.readouterr()
    assert get_print_cursor_value(3, "A") in out
    assert result == []


@mock.patch("sys.stdin.fileno")
@mock.patch("sys.stdin.read")
@mock.patch("termios.tcgetattr")
@mock.patch("termios.tcsetattr")
@mock.patch("tty.setraw")
def test_multichoice_symbol_in(mock_set_raw: mock.Mock,
                               mock_tc_get_attr: mock.Mock,
                               mock_tc_set_attr: mock.Mock,
                               mock_sys_read: mock.Mock,
                               mock_file_no: mock.Mock, capfd):
    test_cases = [
        {
            "sequence": [chr(27), chr(91), chr(66)] + [chr(13)] + ([chr(27), chr(91), chr(66)]*2),
            "values": ("Red", "Text", "X", "Magenta"),
            "symbol": "✗",
            "result": "Choice2"
        },
        {
            "sequence": ([chr(27), chr(91), chr(66)] *2) + [chr(13)] + ([chr(27), chr(91), chr(66)]*2),
            "values": ("Red", "Text", "T", "Magenta"),
            "symbol": "✓",
            "result": "Choice3"
        },
        {
            "sequence": ([chr(27), chr(91), chr(66)] *2) + [chr(13)] + ([chr(27), chr(91), chr(66)]*2),
            "values": ("Red", "Text", "©", "Magenta"),
            "symbol": "©",
            "result": "Choice3"
        },
        {
            "sequence": ([chr(27), chr(91), chr(66)] *2) + [chr(13)] + [chr(13)] +  [chr(13)] + ([chr(27), chr(91), chr(66)]*2),
            "values": ("Red", "Text", "©", "Magenta"),
            "symbol": "©",
            "result": "Choice3"
        },
        {
            "sequence": ([chr(27), chr(91), chr(66)] *2) + [chr(13)] + ([chr(27), chr(91), chr(65)] *2) + ([chr(27), chr(91), chr(66)]*4),
            "values": ("Red", "VAL", "©", "Magenta"),
            "symbol": "©",
            "result": 2
        },
        {
            "sequence": ([chr(27), chr(91), chr(66)] *2) + [chr(13)] + ([chr(27), chr(91), chr(65)] *2) + ([chr(27), chr(91), chr(66)]*4),
            "values": ("Red", "Text", "©", "Magenta"),
            "symbol": "©",
            "result": "Choice3"
        }
    ]
    valArray = ["Choice1", "Choice2", "Choice3"]
    for test_case in test_cases:
        mock_sys_read.side_effect = test_case["sequence"] + [chr(13)]

        result = multiChoice(valArray, *test_case["values"])

        out, err = capfd.readouterr()
        assert test_case["symbol"] in out
        assert result == [test_case["result"]]


def test_multiChoice_given_tick_or_cross_is_less_than_one():
    valArray = ["Choice1", "Choice2", "Choice3"]
    assert multiChoice(valArray, "Red", "Text", "fx", "Magenta") == -1

#--------------------------------SingleChoice--------------------------------#

@mock.patch("sys.stdin.fileno")
@mock.patch("sys.stdin.read")
@mock.patch("termios.tcgetattr")
@mock.patch("termios.tcsetattr")
@mock.patch("tty.setraw")
def test_singleChoice_given_choices_chooses_choice_three1(mock_set_raw: mock.Mock,
                                                         mock_tc_get_attr: mock.Mock,
                                                         mock_tc_set_attr: mock.Mock,
                                                         mock_sys_read: mock.Mock,
                                                         mock_file_no: mock.Mock, capfd):
    valArray = ["Choice1", "Choice2", "Choice3"]
    char_down_sequence = [chr(27), chr(91), chr(66)] * 3 + [chr(27), chr(91), chr(65)] + [chr(27), chr(91), chr(66)]
    mock_sys_read.side_effect = char_down_sequence + [chr(13)]

    result = singleChoice(valArray, "Red", "Text")

    out, err = capfd.readouterr()
    assert get_print_cursor_value(3, "A") in out
    assert result == "Choice3"

@mock.patch("sys.stdin.fileno")
@mock.patch("sys.stdin.read")
@mock.patch("termios.tcgetattr")
@mock.patch("termios.tcsetattr")
@mock.patch("tty.setraw")
def test_singleChoice_given_choices_chooses_choice_three2(mock_set_raw: mock.Mock,
                                                         mock_tc_get_attr: mock.Mock,
                                                         mock_tc_set_attr: mock.Mock,
                                                         mock_sys_read: mock.Mock,
                                                         mock_file_no: mock.Mock, capfd):
    valArray = ["Choice1", "Choice2", "Choice3"]
    char_down_sequence = [chr(27), chr(91), chr(66)] 
    mock_sys_read.side_effect = char_down_sequence + [chr(13)]

    result = singleChoice(valArray, "Red", "Val")

    out, err = capfd.readouterr()
    assert get_print_cursor_value(3, "A") in out
    assert result == 1
