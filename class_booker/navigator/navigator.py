class Navigator:

    def __init__(self, driver, navigation_behaviour):
        self.driver = driver
        self.navigation_behaviour = navigation_behaviour

    def login(self, username, password):
        self.navigation_behaviour.login(username, password)

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
