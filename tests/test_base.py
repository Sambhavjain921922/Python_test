import pytest
from selenium import webdriver


def start_browser(choice):
    if choice == "chrome":
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\sambhavjain\\Downloads\\chromedriver.exe")
        driver.get("http://automationpractice.com/index.php")
        driver.maximize_window()
        driver.refresh()
        driver.implicitly_wait(5)
    if choice == "edge":
        driver = webdriver.edge(
            executable_path="C:\\Users\\sambhavjain\\Downloads\\IEDriverServer.exe")
        driver.get("http://automationpractice.com/index.php")
        driver.maximize_window()
        driver.refresh()
        driver.implicitly_wait(5)
    if choice == "firefox":
        driver = webdriver.edge(
            executable_path="C:\\Users\\sambhavjain\\Downloads\\geckodriver.exe")
        driver.get("http://automationpractice.com/index.php")
        driver.maximize_window()
        driver.refresh()
        driver.implicitly_wait(5)
    return driver


@pytest.fixture(autouse=True)
def browser_quit():
    driver = webdriver.Chrome(
        executable_path="C:\\Users\\sambhavjain\\Downloads\\chromedriver.exe")
    driver.quit()
