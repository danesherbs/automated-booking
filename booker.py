from selenium import webdriver
import json


# Retrieve credentials
with open('credentials.json', 'r') as f:
    json_file = json.load(f)
    username, password = json_file["username"], json_file["password"]

# Login to Virgin Active portal
driver = webdriver.Safari()
url = 'https://www.virginactive.co.uk/login'
driver.get(url)

username_input = driver.find_element_by_name('UserName')
username_input.clear()
username_input.send_keys(username)

password_input = driver.find_element_by_name('Password')
password_input.clear()
password_input.send_keys(password)
password_input.submit()

# Retrieve timetable for your club
class_timetable = driver.find_element_by_name('View class timetable')
class_timetable.click()

change_club_button = driver.find_element_by_name('Change club')
change_club_button.click()
