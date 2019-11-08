from selenium import webdriver
import json

# Retrieve credentials
with open('credentials.json', 'r') as f:
    json_file = json.load(f)
    username, password = json_file["username"], json_file["password"]


class Navigator:

    def __init__(self, driver, navigation_behaviour):
        self.driver = driver
        self.navigation_behaviour = navigation_behaviour

    def login(self):
        self.navigation_behaviour.login()

    def book_class(self, details):
        self.navigation_behaviour.book_class(details)

    def fill_input(self, element_name, content, submit=False):
        element_input = self.driver.find_element_by_name(element_name)
        element_input.clear()
        element_input.send_keys(content)
        if submit:
            element_input.submit()

    def click_element(self, element_name):
        element = self.driver.find_element_by_name(element_name)
        element.click()

    def goto(self, url):
        self.driver.get(url)


driver = webdriver.Safari()
virgin_active_navigator = VirginActiveNavigator()
navigator = Navigator(driver)

# Login to Virgin Active account
navigator.goto('https://www.virginactive.co.uk/login')
navigator.fill_input('UserName', username)
navigator.fill_input('Password', password)
navigator.click_element('Submit')


def _book_class(navigator, club_name, time, class_name, day_of_week):
    navigator.click_element('View class timetable')
    navigator.click_element('Change club')
    navigator.click_element(club_name)
    navigator.click_element('Time of day')
    navigator.click_element(time)
    navigator.click_element('Class')
    navigator.click_element(class_name)
    navigator.click_element(day_of_week)
    navigator.click_element('Book')


# Navigate to class and book
_book_class(navigator, 'Islington Angel', 'Morning', 'Pilates', 'Sunday')
