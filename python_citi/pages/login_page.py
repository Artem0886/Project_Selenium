from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger
import allure

class Login_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""

    login = "(//span[@class='en3k2720 e106ikdt0 css-1rzz8dw e1gjr6xo0'])[1]"
    email = "//input[@name='login']"
    password = "//input[@name='pass']"
    submit = "//button[@class='e4uhfkv0 css-1yh1imp e4mggex0']"
    main_word = "//span[text()='Артем']"
    i_agree = "//button[@class='e4uhfkv0 css-1jfe691 e4mggex0']"

    """Getters"""

    def get_login(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login)))

    def get_email(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_submit(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.submit)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_i_agree(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.i_agree)))

    """Actions"""

    def click_login(self):
        self.get_login().click()
        print("Click login")

    def input_email(self, login):
        self.get_email().send_keys(login)
        print("Input email")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_submit(self):
        self.get_submit().click()
        print("Click submit")

    def click_i_agree(self):
        self.get_i_agree().click()
        print("Click i agree")

    """Methods"""

    def authorization(self):
        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            self.click_i_agree()
            self.click_login()
            self.input_email("Почта")   ### Личные данные скрыты
            self.input_password("Пароль")   ### Личные данные скрыты
            self.click_submit()
            self.assert_word(self.get_main_word(), "Артем")
            Logger.add_end_step(url=self.driver.current_url, method="authorization")