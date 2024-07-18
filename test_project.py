#main file necessities imported as precaution
import sys
from PIL import Image, ImageDraw, ImageFont
import os
import random
import textwrap

import pytest
import unittest
from unittest.mock import patch, mock_open
from project import is_username_taken, remove_motivation, add_motivation, add_user, remove_user, authenticate_user, make_data, add_data, remove_data, motivation_questions, user_preferences, get_quote, make_motivation, menu, menu_two, help

username = "Admin" #do not change(current bug in remove_motivation deletes all file content)
password = "Admin"


def test_is_username_taken():
    assert is_username_taken(username, "user_credentials.txt")


def test_authenticate_user():
    assert authenticate_user(username, password, "user_credentials.txt")


def test_remove_user():
    assert remove_user()


def test_add_user():
    assert add_user(username, password, "user_credentials.txt")


def test_remove_motivation():
    assert remove_motivation(username, "user_data.txt")


def test_help():
    assert help(username)


@patch('builtins.input', side_effect=['y', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10'])
def test_motivation_questions(mock_input):
    expected_results = (10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)
    results = motivation_questions()
    assert results == expected_results


@patch('project.is_username_taken')
@patch('project.motivation_questions')
@patch('builtins.open', new_callable=mock_open)
def test_add_motivation_success(mock_open, mock_motivation_questions, mock_is_username_taken):
    mock_is_username_taken.return_value = False
    mock_motivation_questions.return_value = (10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)

    result = add_motivation(username, "user_data.txt")

    mock_is_username_taken.assert_called_once_with(username, "user_data.txt")
    mock_motivation_questions.assert_called_once()
    mock_open.assert_called_once_with("user_data.txt", 'a')
    mock_open().write.assert_called_once_with(f"{username}, (10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)\n")
    assert result is True


@patch('project.make_motivation')
@patch('builtins.input', side_effect=['1'])
def test_make_data(mock_input, mock_make_motivation):
    mock_make_motivation.return_value = 0
    assert make_data(username)


@patch('project.add_motivation')
def test_add_data(mock_add_motivation):
    mock_add_motivation.return_value = True
    assert add_data(username) == 0


@patch('project.remove_motivation')
def test_remove_data(mock_remove_motivation):
    mock_remove_motivation.return_value = True
    assert remove_data(username) == 0


@patch('builtins.open', new_callable=mock_open, read_data="Admin, (1,2,3)")
def test_user_preferences(mock_open):
    with patch('random.choice', return_value=(0, 3)):
        result = user_preferences(username, "user_data.txt")
        assert result == 1
        mock_open.assert_called_once_with("user_data.txt", 'r')

@patch('project.user_preferences')
@patch('builtins.open', new_callable=mock_open, read_data='12# "Hello World, this is a test quote" - Shawn')
def test_get_quote(mock_open, mock_user_preferences):
    mock_user_preferences.return_value = 12
    result = get_quote("Admin", "user_data.txt")
    assert result == '"Hello World, this is a test quote" - Shawn'
    mock_open.assert_called_once_with("motivational_quotes.txt", 'r')


#running this test as is will randomize the Admin1.jpg file which acts as an example of make_motivation
#this doesn't actually test the functionality it only checks that it runs to completion with out error
def test_make_motivation():
    assert make_motivation(username, 1) == 0


@patch('builtins.input', side_effect=['Exit'])
def test_menu(mock_input):
    with pytest.raises(SystemExit):
        menu()


@patch('builtins.input', side_effect=['Exit'])
def test_menu_two(mock_input):
    assert menu_two(username) == 'exit'


