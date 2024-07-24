# Project Title
Get Motivated - Motivational meme generator
## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

first a quick introduction
Hi im Shawn Neuman from San Antonio Texas in the USA
This is my CS50 python project. at the time im writing this it is 07/24/2024

my accounts are
[text version of url](https://profile.edx.org/u/s-neuman)
[text version of url](https://www.youtube.com/@shawnneuman10)
[text version of url](https://github.com/shawnn10)
please feel free to give me advise or reach out with questions.

This project is meant to help quickly make motivational content. how it does this is by pulling from a folder of images and a file full of categorized quotes. There are 7 default images and 182 quotes. these quotes are divided into 11 catagories based off of the 11 types of motivations. the user is asked to answer 11 questions that help the program better understand the users motivational factors. the users answers and credentials are save in separate text documents. this means the user can come back at any time and not need to answer the questions again, tho they can if the wish to update their answers.

the usage of this program is intended to be for quickly making motivational content for social media. it is also a good tool for self motivation and further understanding what motivates the user. the program supports multiple users or Profiles so that content for different people or different channels can be refined and tailored. one example would be a gym that loads pictures of their facilities and the makes different user profiles with a heavy influence of Physiological Motivation and other. upon requesting content the program would choose a random quote from Physiological Motivation or other and then lay that over their image. then they could quickly send out personalized emails with a splash of motivation.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
  1. install vscode [Download link](https://code.visualstudio.com/Download)
  2. once in the vscode use the terminal to install all the required modules and packages with "pip install -r requirements.txt" command

### Prerequisites

You will need vscode or another python compiler for descriptions and more options see this link https://www.softwaretestinghelp.com/python-compiler/

Visual Studio Code *Recommended*
[Download link](https://code.visualstudio.com/Download)
Programiz
[Download link](https://www.programiz.com/python-programming/online-compiler/)
PyDev
[Download link](https://www.pydev.org/download.html)
PyCharm
[Download link](https://www.jetbrains.com/pycharm/)
Sublime Text
[Download link](https://www.sublimetext.com/)
Thonny
[Download link](https://thonny.org/)
Jupyter Notebook
[Download link](https://jupyter.org/)

### Installing

to get this program up and running its recommended that you start with the Admin user.

First start the program by opening the terminal in your compiler and running "python project.py"
at this point there will be a small paragraph explaining what to do. you can follow the directions there or follow this guide.
now you will be in the Text Menu from here you can type in a command int the terminal as prompted, to navigate the menu.
for now we will use "Login" command and use the Username "Admin" and the Password "Admin"
now you should encounter the second text menu prompt from here we will use the "Make" command
and then choose between 1 - 5 pictures to be made.
at this point its recommended that you use the "Exit" command
now navigate to the root folder of the project file where you will find files name Admin(1-5).jpg
congratulations your motivational images and quotes have been generated.


#### New user Install

to create a new user and start making personalized content use the following commands
"python project.py"
"CreateAccount"
then choose your own Username and Password and verify your password
"Login"
use your new credentials
"Add"
"y"
Then answer the questions that follow to personalize the content
after all the questions have been answered you can then
"Make" your personalized motivation

#### Video Demo:  <URL HERE>
[text version of url](https://youtu.be/VnBPzPiFWcU)

## Usage <a name = "usage"></a>

### main

Main function calling menu, handling user login, and program loop.


### is_username_taken

Check if username exists in the file.

Args:
    username (str): The username to check.
    filename (str): File containing user credentials.

Returns:
    bool: True if username exists, False otherwise.

### remove_motivation

Remove user's motivational data from the file.

Args:
    username (str): The username.
    filename (str): File containing motivational data.

### add_data

Add motivational data for the user.

Args:
    username (str): The current user.

### remove_data

Remove motivational data for the user.

Args:
    username (str): The current user.

### make_data

Generate a number of motivational images for the user.

Args:
    username (str): The current user.

### motivation_questions

Ask the user questions to determine motivational preferences.

Returns:
    tuple: User's responses to motivational questions.


### add_motivation

Add motivational preferences for the user.

Args:
    username (str): The current user.
    filename (str): File to store user data.

### user_preferences

Get user's motivational preferences from the file.

Args:
    username (str): The current user.
    filename (str): File containing user data.

Returns:
    int: User's top motivational preference.

### get_quote

Get a random motivational quote based on user's preferences.

Args:
    username (str): The current user.
    filename (str): File containing user data.

Returns:
    str: A motivational quote.

### make_motivation

Generate and save motivational images for the user.

Args:
    username (str): The current user.
    number_of_pictures (int): Number of images to generate.

### menu

Display login or account creation menu.

Returns:
    str: Verified username.

### menu_two

Display the main menu for user actions.

Args:
    username (str): The current user.

Returns:
    str: Chosen user action.

### authenticate_user

Authenticate user with username and password.

Args:
    username (str): The username.
    password (str): The password.
    filename (str): File containing user credentials.

Returns:
    bool: True if authenticated, False otherwise.

### add_user

Add a new user to the credentials file.

Args:
    username (str): New username.
    password (str): New password.
    filename (str): File to store user credentials.

### remove_user

Remove Admin user for testing purposes.

### help

Provide menu usage instructions to the user.


