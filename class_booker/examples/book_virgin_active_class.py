import json
from selenium import webdriver

from class_booker.navigator.navigator import Navigator
from class_booker.navigator.virgin_active_behaviour import VirginActiveNavigator

driver = webdriver.Safari()
navigator_behaviour = VirginActiveNavigator()
navigator = Navigator(driver, navigator_behaviour)

# Retrieve credentials
with open('credentials.json', 'r') as f:
    json_file = json.load(f)
    username, password = json_file["username"], json_file["password"]

# Define class details
class_details = {
    'club_name': 'Islington Angel',
    'time': 'Morning',
    'class_name': 'Pilates',
    'day_of_week': 'Sunday'
}

navigator.login(username, password)
navigator.book_class(class_details)
