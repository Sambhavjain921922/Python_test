from selenium.webdriver.common.by import By
from Utilities import config
from selenium.webdriver.support.select import Select



class SignUp:
    def __init__(self, driver):
        self.driver = driver


    def click_SignUp(self):
        self.driver.find_element(By.CLASS_NAME, "login").click()

    def Enter_Email(self,email):
        self.driver.find_element(By.ID, "email_create").send_keys(email)

    def Enter_Submit(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Create an account']").click()

    def Enter_gender(self):
        self.driver.find_element(By.ID, "id_gender1").click()

    def first_name(self, firstname):
        self.driver.find_element(By.ID, "customer_firstname").send_keys(firstname)

    def Last_Name(self, lastname):
        self.driver.find_element(By.ID, "customer_lastname").send_keys(lastname)

    def EnterPassword(self, password):
        self.driver.find_element(By.ID, "passwd").send_keys(password)

    def Enter_day(self, day):
        day1=self.driver.find_element(By.ID, "days")
        drop = Select(day1)
        drop.select_by_value(day)

    def Enter_month(self, month):
        month1= self.driver.find_element(By.ID, "months")
        drop = Select(month1)
        drop.select_by_value(month)

    def Enter_year(self, year):
        self.driver.find_element(By.ID, "years").send_keys(year)

    def Enter_first(self, firstname):
        self.driver.find_element(By.ID, "firstname").send_keys(firstname)

    def Enter_last(self, lastname):
        self.driver.find_element(By.ID, "customer_lastname").send_keys(lastname)

    def Enter_cmpname(self, cmp):
        self.driver.find_element(By.ID, "company").send_keys(cmp)

    def Enter_adr1(self, adr1):
        self.driver.find_element(By.ID, "address1").send_keys(adr1)

    def Enter_adr2(self, adr2):
        self.  driver.find_element(By.ID, "address2").send_keys(adr2)

    def Enter_cty(self, cty):
        self.   driver.find_element(By.ID, "city").send_keys(cty)

    def Enter_state(self, state):
        state1= self.driver.find_element(By.ID, "id_state")
        drop = Select(state1)
        drop.select_by_value("11")

    def Enter_code(self, code):
        self. driver.find_element(By.NAME, "postcode").send_keys(code)
        get_country = self.driver.find_element(By.XPATH, "//select[@id='id_country']")
        country = Select(get_country)
        country.select_by_value("21")


    def Enter_othr(self, othr):
        self. driver.find_element(By.ID, "other").send_keys(othr)

    def Enter_phn(self, phn):
        self.   driver.find_element(By.ID, "phone").send_keys(phn)

    def Enter_mob(self, mob):
        self. driver.find_element(By.ID, "phone_mobile").send_keys(mob)

    def Enter_state1(self, state1):
        self.driver.find_element(By.ID, "alias").send_keys(state1)


    def Enter_signupsubmit(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Register']").click()

