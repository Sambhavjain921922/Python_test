import time
from Utilities import config
from selenium import webdriver
from Pages.LoginPage import login
from tests.test_base import start_browser


def test_Login():

    choice = "chrome"
    driver = start_browser(choice)
    log = login(driver)
    log.click_SignUp()
    log.Enter_Email(config.email)
    log.Enter_Password(config.password)
    log.Enter_Submit()
    time.sleep(5)
    #driver.close()
    #driver.quit()
