import time
import pytest
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.DeleteAddressPage import del_Address
from Utilities import config
from tests.test_base import start_browser


def test_delete_address():

    choice = "chrome"
    driver = start_browser(choice)
    log = del_Address(driver)
    log.click_SignUp()
    log.Enter_Email(config.email)
    log.Enter_Password(config.password)
    log.Enter_Submit()
    log.Enter_MyAddress()
    log.delete_MyAddress()
    log.Pop_up()
    time.sleep(5)
    #driver.close()
    #driver.quit()
