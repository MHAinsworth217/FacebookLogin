# Matthew Ainsworth
# Automated Facebook Login Project using Selenium and Chromedriver
# 24/07/2020

# Import time and selenium modules
import time
from selenium import webdriver

# Access Chromedriver
driver = webdriver.Chrome()

# Set the acceptable options that the user can input
# These will need to be changed if more users are added/removed
options = [1, 2, 3, 4, 5]

# Add the users and passwords to a list of dictionaries
users = [
    {"email": "ehmeffdoom@gmail.com", "password": "wordpass23"},
    {"email": "viccaughn345@gmail.com", "password": "doomguy23"},
    {"email": "kddumile@gmail.com", "password": "doritos54"},
    {"email": "metalfingers97@gmail.com", "password": "fritos89"},
    {"email": "dangerdoomio@gmail.com", "password": "cheetos67"},
         ]

print("Welcome!")
time.sleep(2)

# Initialise loop for program to run until user completes login process or exits
while True:
    print("""
Please select a user from the list:
(1) Harrold Smith
(2) Victor Vaughn
(3) Kevin Dumile
(4) Michael Fingers
(5) Daniel Dhoom
(0) Exit Program
    """)
    # Get selection from user (integer)
    selection = int(input())
    # If the selection is in the list of options we created earlier, run this block of code
    if selection in options:
        # Set index to the selection - 1. This is because the index will start at 0 instead of 1
        index = int(selection) - 1
        # Set the username and password values to the place in the list, corresponding to the index number
        username = users[index]["email"]
        password = users[index]["password"]
        # Go to facebook
        driver.get("https://facebook.com")
        time.sleep(1)
        # Find the login and password boxes and fill them with the values of username and password
        loginBox = driver.find_element_by_id("email")
        loginBox.send_keys(username)
        passBox = driver.find_element_by_id("pass")
        passBox.send_keys(password)
        time.sleep(1)
        # Submit the values, therefore logging in
        passBox.submit()
        # Exit program
        print("Thank you for using my program!")
        break
    # If the user selects 0, run this block of code
    elif selection == 0:
        # Exit the program
        print("Goodbye!")
        break
    # If any other selection is made, it is out of range. Therefore, run this block of code and start again.
    else:
        print("Please enter a valid selection.")
