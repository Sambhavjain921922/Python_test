import time

import pytest

from Utilities import config
from selenium import webdriver
from Pages.LoginPage import login
from tests.test_base import start_browser


@pytest.mark.parametrize("Email,Password",
                         [(config.Invalidemail, config.InvalidPassword), (config.email, config.InvalidPassword),
                          (config.Invalidemail, config.password)])
def test_Invalid_Login(Email, Password):
    choice = "chrome"
    driver = start_browser(choice)
    log = login(driver)
    log.click_SignUp()
    log.Enter_Email(Email)
    log.Enter_Password(Password)
    log.Enter_Submit()
    time.sleep(5)
    # driver.close()
    # driver.quit()
