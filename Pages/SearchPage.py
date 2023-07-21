from selenium.webdriver.common.by import By
from Utilities import config


class search:
    def __init__(self, driver):
        self.driver = driver

    def click_SignUp(self):
        self.driver.find_element(By.CLASS_NAME, "login").click()

    def Enter_Email(self,email):
        self.driver.find_element(By.ID, "email").send_keys(email)

    def Enter_Password(self,password):
        self.driver.find_element(By.ID, "passwd").send_keys(password)

    def Enter_Submit(self):
        self.driver.find_element(By.ID, "SubmitLogin").click()
    def Enter_srch(self,srch):
        self. driver.find_element(By.ID, "search_query_top").send_keys(srch)

    def Enter_Submit2(self):
        self. driver.find_element(By.NAME, "submit_search").click()

