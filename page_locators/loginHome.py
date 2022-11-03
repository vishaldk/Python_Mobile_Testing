from appium.webdriver.common.mobileby import MobileBy
from owl_eyes.general_utilities.basePage import basePage


class loginHome(basePage):
    def __init__(self, driver):
        self.driver = driver
        a=5
    skip = (MobileBy.ID, "com.application.zomato:id/skip_button")

    def skip_login(self):
        self.click(self.skip)

