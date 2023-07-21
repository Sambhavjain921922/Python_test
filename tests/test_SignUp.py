import time
import pytest
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.SignUpPage import SignUp
from Utilities import config
from tests.test_base import start_browser


def test_SignUp():
    choice = "chrome"
    driver = start_browser(choice)
    log = SignUp(driver)
    log.click_SignUp()
    log.Enter_Email(config.email)
    log.Enter_Submit()
    time.sleep(5)
    log.Enter_gender()
    log.first_name(config.firstname)
    log.Last_Name(config.lastname)
    log.EnterPassword(config.password)
    log.Enter_day(config.day)
    log.Enter_month(config.month)
    log.Enter_year(config.year)
    log.Enter_first(config.firstname)
    log.Enter_last(config.lastname)
    log.Enter_cmpname(config.cmp)
    log.Enter_adr1(config.adr1)
    log.Enter_adr2(config.adr2)
    log.Enter_cty(config.cty)
    log.Enter_state(config.state)
    log.Enter_code(config.code)
    log.Enter_othr(config.othr)
    log.Enter_phn(config.phn)
    log.Enter_mob(config.mob)
    log.Enter_state1(config.state1)
    log.Enter_signupsubmit()
    time.sleep(5)
    # driver.close()
    # driver.quit()
