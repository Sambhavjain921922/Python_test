import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.SearchPage import search
from Utilities import config
from tests.test_base import start_browser


def test_Search():

    choice = "chrome"
    driver = start_browser(choice)
    log = search(driver)
    log.click_SignUp()
    log.Enter_Email(config.email)
    log.Enter_Password(config.password)
    log.Enter_Submit()
    log.Enter_srch(config.srch)
    log.Enter_Submit2()
    time.sleep(5)
    #driver.close()
    #driver.quit()