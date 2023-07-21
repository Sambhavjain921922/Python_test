import time
import pytest
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.NewAddressPage import Address
from Utilities import config
from tests.test_base import start_browser


def test_new_address():

    choice = "chrome"
    driver = start_browser(choice)
    log = Address(driver)
    log.click_SignUp()
    log.Enter_Email(config.email)
    log.Enter_Password(config.password)
    log.Enter_Submit()
    log.Enter_MyAddress()
    log.Enter_New_Address()
    log.Enter_first(config.firstname)
    log.Enter_last(config.lastname)
    log.Enter_cmpname(config.cmp)
    time.sleep(5)
    log.Enter_adr1(config.adr1)
    log.Enter_adr2(config.adr2)
    log.Enter_cty(config.cty)
    log.Enter_state(config.state)
    log.Enter_code(config.code)
    log.Enter_othr(config.othr)
    log.Enter_phn(config.phn)
    log.Enter_mob(config.mob)
    log.Enter_state1(config.state1)
    log.Enter_Submit2()
    time.sleep(5)
    #driver.close()
    #driver.quit()
