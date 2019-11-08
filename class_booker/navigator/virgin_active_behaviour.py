from class_booker.navigator.navigator import NavigatorBehaviour


class VirginActiveNavigator(NavigatorBehaviour):

    def __init__(self, navigator):
        self.navigator = navigator

    def login(self, username, password):
        self.navigator.goto('https://www.virginactive.co.uk/login')
        self.navigator.fill_input('UserName', username)
        self.navigator.fill_input('Password', password)
        self.navigator.click_element('Submit')

    def book_class(self, details):
        self.navigator.click_element('View class timetable')
        self.navigator.click_element('Change club')
        self.navigator.click_element(details['club_name'])
        self.navigator.click_element('Time of day')
        self.navigator.click_element(details['time'])
        self.navigator.click_element('Class')
        self.navigator.click_element(details['class_name'])
        self.navigator.click_element(details['day_of_week'])
        self.navigator.click_element('Book')
