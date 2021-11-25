from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By

class MainPage(BasePage): 
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        #return LoginPage(browser = self.browser, url = self.browser.current_url)
        #login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        #login_link.click()
        