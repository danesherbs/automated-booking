class Navigator:

    def __init__(self, driver):
        self.driver = driver

    def fill_input(self, element_name, content):
        element_input = self.driver.find_element_by_name(element_name)
        element_input.clear()
        element_input.send_keys(content)

    def click_element_by_name(self, element_name):
        element = self.driver.find_element_by_name(element_name)
        element.click()

    def click_element_by_class_name(self, class_name):
        element = self.driver.find_element_by_class_name(class_name)
        element.click()

    def goto(self, url):
        self.driver.get(url)
