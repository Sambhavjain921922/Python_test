from selenium.webdriver.common.by import By
from Utilities import config

from selenium.webdriver.support.select import Select

class del_Address:
    def __init__(self, driver):
        self.driver = driver

    def click_SignUp(self):
        self.driver.find_element(By.CLASS_NAME, "login").click()

    def Enter_Email(self, email):
        self.driver.find_element(By.ID, "email").send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(By.ID, "passwd").send_keys(password)

    def Enter_Submit(self):
        self.driver.find_element(By.ID, "SubmitLogin").click()

    def Enter_MyAddress(self):
        self.driver.find_element(By.XPATH, "//a[@title='My addresses']").click()

    def delete_MyAddress(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Delete']").click()

    def Pop_up(self):
        alert = self.driver.switch_to.alert
        alert.accept()
