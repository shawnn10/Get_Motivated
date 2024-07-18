"""
this is the main project file for what im calling Get Motivated

"""

import sys
from PIL import Image, ImageDraw, ImageFont
import os
import random
import textwrap

def main():
    """
    main function used to call menu and receive verified username
    also contains the main program loop for accessing user data and editing
    as well as the greeting and explanation  for how the program works
    """

    # greeting and program explanation
    print("")
    print("Hi And Welcome To my CS50 Python Course project.")
    print("in a moment you will be asked to make an account or log in.")
    print("the default username is Admin and the Password is Admin.")
    print("be aware that the default account is already set up.")
    print("this means you wont have a tailored experience,")
    print("but you can quickly start testing the project.")
    print("this project is designed to generate motivational quotes,")
    print("on top of and image. these quotes and images are randomly")
    print("selected from the images folder and motivational_quotes.txt file")
    print("adding images or quotes is supported but please match file")
    print("types and quote catagories found in the README.md file.")
    print("Enjoy the project and, Get Motivated!")
    print("")
    username = menu()
    print("welcome", username)

    while True:
        operation = menu_two(username)
        if operation == "add":
            operation = add_data(username)
        elif operation == "remove":
            operation = remove_data(username)
        elif operation == "make":
            operation = make_data(username)
        elif operation == "exit":
            sys.exit("Bye Bye")

def is_username_taken(username, filename):
    """
    Checks if the provided username already exists in the given file.

    Args:
        username (str): The username to check.
        filename (str): The path to the file containing user credentials.

    Returns:
        bool: True if the username is already taken, False otherwise.
    """
    try:
        with open(filename, 'r') as file:
            for line in file:
                stored_username, _ = line.strip().split(',')
                if username == stored_username:
                    return True
        return False
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return False

def remove_motivation(username, filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        with open(filename, 'w') as file:
            for line in lines:
                line_parts = line.split(', ')
                if line_parts[0] == username and line_parts[0] != "Admin":
                    continue  # Skip writing this line
                file.write(line)
        return True
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. User not added.")
        return False


def add_data(username):
    """
    Adds motivational data for the given user.

    Args:
        username (str): The username of the current user.

    The function attempts to add motivational data for the user by calling
    the add_motivation function. If an error occurs or the data already
    exists, an error message is displayed.

    Returns:
        int: 0 after attempting to add data.
    """
    try:
        add_motivation(username, "user_data.txt")
        return 0
    except:
        print("Procedure interrupted before user data added or data exists already ")
        print("")
        return 1


def remove_data(username):
    """
    Removes motivational data for the given user.

    Args:
        username (str): The username of the current user.

    The function attempts to remove motivational data for the user by calling
    the remove_motivation function. If an error occurs or the data does not
    exist, an error message is displayed.

    Returns:
        int: 0 after attempting to remove data.
    """
    try:
        remove_motivation(username, "user_data.txt")
        return 0
    except:
        print("Procedure interrupted before user data removed or data never existed ")
        print("")
        return 1


def make_data(username):
    """
    Generates a specified number of motivational images for the given user.

    Args:
        username (str): The username of the current user.

    The function prompts the user to specify how many motivational images
    to generate (between 1 and 5). It then attempts to generate the images
    by calling the make_motivation function. If an error occurs, an error
    message is displayed. If the number of images is not between 1 and 5,
    the user is prompted again.

    Returns:
        int: 0 after attempting to generate images.
    """
    number_of_pictures = 0
    while number_of_pictures == 0:
        number_of_pictures = int(input("How many would you like to make 1 - 5 "))
        if number_of_pictures <= 5 and number_of_pictures >= 1:
            try:
                make_motivation(username, number_of_pictures)
                return True
            except:
                print("Procedure interrupted check files and folders")
                print("")
                return 1
        else:
            number_of_pictures = 0
            print("number was not between 1 - 5")



"""
this code determines a persons preferences of motivational material by asking a series of questions based on this list of motivations.

List of motivations
    Prime Motivations
1. Intrinsic Motivation
2. Extrinsic Motivation
    Internal/Intrinsic Motivations
3. Competence & Learning Motivation
4. Attitude Motivation
5. Achievement Motivation
6. Creative Motivation
7. Physiological Motivation
    External/Extrinsic Motivations
8. Incentive Motivation
9. Fear Motivation
10. Power Motivation
11. Affiliation & Social Motivation
"""


def motivation_questions():
    explanation = input(
        "the next few prompts will ask you 1-10. 1 being the worst and 10 the best. how likely you are to be motivated by whats said. do you want to proceed y/n: ")

    if explanation == "y":

        intrinsic = input("1-10 I engage in activities purely for the pleasure and satisfaction: ")
        extrinsic = input(
            "1-10 I engage in activities for the prizes, trophy's, or acknowledgement of others: ")
        learning = input("1-10 I engage in activities for the pursuit of knowledge: ")
        attitude = input(
            "1-10 I engage in activities for the betterment of the world regardless of what people think: ")
        achievement = input(
            "1-10 I engage in activities for the completion of a task. example collecting all pieces of a set or growing the perfect orchid: ")
        creative = input(
            "1-10 I engage in activities for the chance to express myself or discover things: ")
        physiological = input(
            "1-10 I engage in activities because i have to. examples: Im hungry so i eat same can be said for thirst, lust, or sleep: ")
        incentive = input(
            "1-10 I engage in activities for the benefits i can receive. example: I work hard for more time off or a better bonus: ")
        fear = input(
            "1-10 I engage in activities for the fear of negative consequences. example: I study hard to avoid failing a test: ")
        power = input(
            "1-10 I engage in activities for the power and control derived from my advancement: ")
        social = input(
            "1-10 I engage in activities for the social growth, meeting new people, and making friends: ")
        results = (int(intrinsic), int(extrinsic), int(learning), int(attitude), int(achievement), int(
            creative), int(physiological), int(incentive), int(fear), int(power), int(social))
        return (results)

    else:
        return 0


def add_motivation(username, filename):
    if not is_username_taken(username, filename):
        results = motivation_questions()
        if results == 0:
            raise ValueError("no answers given")
        elif results != 0:
            try:
                with open(filename, 'a') as file:
                    file.write(f"{username}, {results}\n")
                return True
            except FileNotFoundError:
                print(f"Error: File '{filename}' not found. User not added.")
                return False
    else:
        raise ValueError("User already added question data")




def user_preferences(username, filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                # Split the line into username and preferences
                parts = line.strip().split(',', 1)
                if username == parts[0]:
                    preferences = parts[1].strip().strip("()")
                    preferences = preferences.split(',')

                count = 0
                for preference in preferences:
                    preference = preferences[count].strip()
                    preferences[count] = count, int(preference)
                    count = count + 1

                sorted_preferences = sorted(preferences, key=lambda x: x[1], reverse=True)

                top_3_preferences = sorted_preferences[:3]

                random_preference = random.choice(top_3_preferences)

                return random_preference[0] + 1
            # If username not found in the file
            print(f"Error: User '{username}' not found.")
            return None
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. User not added.")
        return None

def get_quote(username, filename):
    preference = user_preferences(username, filename)
    # set a new number if users default is 1 or 2 which are the prime catagories
    if int(preference) == 1:
        random_number = [3,4,5,6,7]
        preference = random.choice(random_number)
    elif int(preference) == 2:
        random_number = [8,9,10,11]
        preference = random.choice(random_number)

    try:
        with open("motivational_quotes.txt", 'r') as file:
            lines = file.readlines()
            new_lines = []
            for line in lines:
                number, quote = line.split("#")
                if int(number.strip()) == preference:
                    new_lines.append(quote.strip())
        return(random.choice(new_lines))


    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. User not added.")
        return None





def make_motivation(username, number_of_pictures):
    while number_of_pictures != 0:
        # Define the folder path where the images are located
        image_folder = "/workspaces/105595387/project/images"
        files = os.listdir(image_folder)

        # Pick a random image
        random_image = random.choice(files)

        # Open the image
        image_path = os.path.join(image_folder, random_image)
        image = Image.open(image_path)

        # Resize the image
        new_img = image.resize((500, 500))

        # Add text to the image
        draw = ImageDraw.Draw(new_img)
        font = ImageFont.truetype("arial.ttf", 35)  # Adjust font size as needed
        ... #this section is still under construction. add a random pick from the users top 3 motivation factors

        text = get_quote(username, "user_data.txt")
        # Set margin and offset
        margin = offset = 30
        # Wrap the text
        # shadow layer
        for line in textwrap.wrap(text, width=25):
            draw.text((margin, offset), line, font=font, fill="Black")
            offset += 45

        # ReSet margin and offset
        margin = offset = 28
        # Light Layer
        for line in textwrap.wrap(text, width=25):
            draw.text((margin, offset), line, font=font, fill="White")
            offset += 45

        # Save the modified image
        new_img.save(f"{username}{number_of_pictures}.jpg", format="JPEG", optimize=True)
        print("")
        print(f"Image resized and text added. Saved as {username}{number_of_pictures}.jpg")

        number_of_pictures = number_of_pictures - 1
    return 0

def menu():
    logged = False
    """
    Takes user input and matches it to available menu options.
    it loops endlessly until menu = 'Exit' or ctrl c pressed

    Args:
        logged (bool): this stops the loop after verification
        menu (str): The menu option for function request.

    returns username for security

    """
    while not logged:
        menu = input("Text Menu: Login, CreateAccount, or Exit: ")

        if menu.strip().lower().title() == "Login":
            user_input_username = input("Enter your Username: ")
            user_input_password = input("Enter your Password: ")

            if authenticate_user(user_input_username, user_input_password, "user_credentials.txt"):
                print("Authentication successful!")
                logged = True
            else:
                print("Authentication failed. Invalid username or password.")

        elif menu.strip() == "CreateAccount":
            made = False
            while not made:
                user_input_username = input("Choose your Username: ")
                user_input_password = input("Choose your Password: ")
                user_input_password2 = input("Verify your Password: ")
                if user_input_password == user_input_password2:
                    try:
                        add_user(user_input_username, user_input_password, "user_credentials.txt")
                        print(f"User '{user_input_username}' added successfully!")
                    except ValueError:
                        print("Username already taken")
                    except:
                        print("User not added due to error.")
                    made = True
                else:
                    print("Error passwords must match ")

        elif menu.strip().lower().title() == "Exit":
            sys.exit("Bye Bye")

        else:
            print("Invalid menu option.")
    return user_input_username


def menu_two(username):
    """
    Displays a menu to the user and processes their chosen action.

    Args:
        username (str): The username of the current user.

    The function calls the help function to provide assistance to the user,
    then prompts the user to choose an action from a list of valid actions:
    ["add", "remove", "make", "exit"]. If the user enters a valid action,
    it is returned. Otherwise, the menu is displayed again.

    Returns:
        str: The action chosen by the user, which is one of the valid actions.
    """
    help(username)
    valid_actions = ["add", "remove", "make", "exit"]
    user_action = input("what Would you like to do: ").strip().lower()
    if user_action in valid_actions:
        return user_action
    else:
        menu_two(username)


def authenticate_user(username, password, filename):
    """
    Authenticates a user by checking if the provided username and password match any entry in the given file.

    Args:
        username (str): The username to check.
        password (str): The password to check.
        filename (str): The path to the file containing user credentials.

    Returns:
        bool: True if the user is authenticated, False otherwise.
    """
    try:
        with open(filename, 'r') as file:
            for line in file:
                stored_username, stored_password = line.strip().split(',')
                if username == stored_username and password == stored_password:
                    return True
        return False
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return False


def add_user(username, password, filename):
    """
    Adds a new user (username and password) to the given file.

    Args:
        username (str): The new username to add.
        password (str): The new password to add.
        filename (str): The path to the file where user credentials are stored.

    Returns:
        bool: True if the user was successfully added, False otherwise.
    """
    if not is_username_taken(username, filename):
        try:
            with open(filename, 'a') as file:
                file.write(f"{username},{password}\n")
            return True
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found. User not added.")
            return False
    else:
        raise ValueError("Username already taken")

def remove_user():
    """
    Removes Admin (username and password).
    For testing only
    """
    if is_username_taken("Admin", "user_credentials.txt"):
        try:
            with open("user_credentials.txt", 'w') as file:
                file.write(f"")
            return True
        except FileNotFoundError:
            print(f"Error: File 'user_credentials.txt' not found. User not added.")
            return False


def help(username):
    """
    Provides instructions to the user on how to use the menu options.

    Args:
        username (str): The username of the current user.

    The function prints a message to the user for troubleshooting
    """
    print("")
    print(f"Hi {username}, if would you like to Add or Remove data, type (Add or Remove) respectively")
    print("If adding is unsuccessful try to remove then add again")
    print("If you would like Make an image or Exit the the program, type (Make or Exit) ")
    print("after using make the image will be saved in the root folder")
    print("")

    return True


if __name__ == "__main__":
    main()
