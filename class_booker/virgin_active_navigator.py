from class_booker.navigator import Navigator


class VirginActiveNavigator(Navigator):

    def login(self, username, password):
        self.goto('https://www.virginactive.co.uk/login')
        self.fill_input('UserName', username)
        self.fill_input('Password', password)
        self.click_element_by_class_name('btn btn-primary va-button')

    def book_class(self, details):
        self.click_element_by_name('View class timetable')
        self.click_element_by_name('Change club')
        self.click_element_by_name(details['club_name'])
        self.click_element_by_name('Time of day')
        self.click_element_by_name(details['time'])
        self.click_element_by_name('Class')
        self.click_element_by_name(details['class_name'])
        self.click_element_by_name(details['day_of_week'])
        self.click_element_by_name('Book')
