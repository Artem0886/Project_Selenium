import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""

    catalog = "//button[@data-meta-name='DesktopHeaderFixed__catalog-menu']"
    smart_and_gadget = "(//span[contains(text(),'Смартфоны и гаджеты')])[2]"
    smart = "//span[contains(text(),'Смартфоны')]"
    main_word = "//h1[@class='e1e4gwta0 eml1k9j0 app-catalog-yhwyfr e1gjr6xo0']"
    cart = "(//a[@href='/order/'])[1]"
    cart_2 = "(//div[@data-meta-value='1'])[1]"
    clear_cart = "(//button[@class='etd7ecp0 css-11xrwzj e8hswel0'])[2]"
    word_cart = "//span[@class='e1ys5m360 e106ikdt0 css-175fskm e1gjr6xo0']"
    price = "(//div[@class='rc-slider'])[2]"
    tv = "//a[@data-meta-category='cardId-3']"
    logo = "//div[@data-meta-name='Logo']"

    """Getters"""

    def get_catalog(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_smart_and_gadget(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.smart_and_gadget)))

    def get_smart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.smart)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_cart_2(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart_2)))

    def get_clear_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.clear_cart)))

    def get_word_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.word_cart)))

    def get_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price)))

    def get_tv(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.tv)))

    def get_logo(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.logo)))

    """Actions"""

    def click_catalog(self):
        self.get_catalog().click()
        print("Click catalog")

    def click_smart_and_gadget(self):
        self.get_smart_and_gadget().click()
        print("Click smart and gadget")

    def click_smart(self):
        self.get_smart().click()
        print("Click smart")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    def click_logo(self):
        self.get_logo().click()

    def click_tv(self):
        self.get_tv().click()
        print("Click TV")

    def click_clear_cart(self):
        self.get_clear_cart().click()
        print("Cart empty")

    """Очищает корзину перед покупкой сартфона,  т.к. вместо шага(кнопки) "добавить в корзину" будет сразу "оформить заказ"(получится не весь полный путь, покупки товара)"""
    def clear_cart_smart(self):
        try:
            number_cart = WebDriverWait(self.driver, 1).until(
                EC.element_to_be_clickable((By.XPATH, "(//div[@data-meta-value='1'])[1]")))
            value_word_cart = number_cart.text
            assert value_word_cart == "1"
            self.click_cart()
            self.click_clear_cart()
            self.click_catalog()
        except TimeoutException:
            print("Exception: ""TimeoutException")
            self.click_catalog()

    """Очищает корзину перед покупкой TV, т.к. вместо шага(кнопки) "добавить в корзину" будет сразу "оформить заказ"(получится не весь полный путь, покупки товара)"""
    def clear_cart_tv(self):
        try:
            number_cart = WebDriverWait(self.driver, 1).until(
                EC.element_to_be_clickable((By.XPATH, "(//div[@data-meta-value='1'])[1]")))
            value_word_cart = number_cart.text
            assert value_word_cart == "1"
            self.click_cart()
            self.click_clear_cart()
            self.click_logo()
            self.click_tv()
        except TimeoutException:
            print("Exception: ""TimeoutException")
            self.click_tv()

    """Methods"""

    def select_smart(self):
        with allure.step("Select smart"):
            Logger.add_start_step(method="select_smart")
            self.clear_cart_smart()
            self.click_smart_and_gadget()
            self.click_smart()
            self.assert_word(self.get_main_word(), "Смартфоны")
            Logger.add_end_step(url=self.driver.current_url, method="select_smart")

    def select_tv(self):
        with allure.step("Select TV"):
            Logger.add_start_step(method="select_smart")
            # self.clear_cart_tv()
            self.click_tv()
            self.assert_word(self.get_main_word(), "Телевизоры")
            Logger.add_end_step(url=self.driver.current_url, method="select_smart")