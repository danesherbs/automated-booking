from selenium import webdriver
from class_booker.virgin_active_navigator import VirginActiveNavigator


# Define navigator
driver = webdriver.Safari()
navigator = VirginActiveNavigator(driver)

# Book class
navigator.login(
    username="my_username",
    password="my_password"
)

navigator.book_class({
    'club_name': 'Chelsea',
    'time': 'Evening',
    'class_name': 'Pilates',
    'day_of_week': 'Tuesday'
})
