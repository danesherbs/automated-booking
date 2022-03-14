from selenium import webdriver
from class_booker.virgin_active_navigator import VirginActiveNavigator


# Define website navigator
driver = webdriver.Safari()
navigator = VirginActiveNavigator(driver)

# Retrieve credentials
username = 'username'
password = 'password'

# Book class
navigator.login(username, password)
navigator.book_class({
    'club_name': 'Chelsea',
    'time': 'Evening',
    'class_name': 'Pilates',
    'day_of_week': 'Tuesday'
})
