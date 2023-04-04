import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

class Smart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""

    price = "(//div[@role='slider'])[3]"
    check_box_1 = "//div[@data-meta-value='Бренд']"
    check_box_2 = "//div[@data-meta-value='APPLE']"
    check_box_3 = "//div[@data-meta-value='Серия']"
    check_box_4 = "//div[@data-meta-value='Apple iPhone 14 Pro']"
    check_box_5 = "//div[@data-meta-value='Встроенная память']"
    check_box_6 = "//div[@data-meta-value='256 ГБ']"
    list_apple = "//h1[@class='e1e4gwta0 eml1k9j0 app-catalog-yhwyfr e1gjr6xo0']"
    smart_apple = "(//a[@title='Смартфон Apple iPhone 14 Pro 256Gb,  A2889,  золотой'])[1]"
    add_to_cart = "//button[@data-meta-name='BasketDesktopButton']"
    cart = "//button[@class='e4uhfkv0 css-10je9jt e4mggex0']"
    checkout = "//button[@title='Перейти к оформлению']"
    main_word = "//h1[@class='e1ubbx7u0 eml1k9j0 app-catalog-tn2wxd e1gjr6xo0']"
    main_word_2 = "//span[@class='e1ys5m360 e106ikdt0 css-175fskm e1gjr6xo0']"

    """Getters"""

    def get_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price)))

    def get_check_box_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.check_box_1)))

    def get_check_box_2(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.check_box_2)))

    def get_check_box_3(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.check_box_3)))

    def get_check_box_4(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.check_box_4)))

    def get_check_box_5(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.check_box_5)))

    def get_check_box_6(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.check_box_6)))

    def get_list_apple(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.list_apple)))

    def get_smart_apple(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.smart_apple)))

    def get_add_to_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart)))

    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_checkout(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkout)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_main_word_2(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.main_word_2)))

    """Actions"""

    def click_check_box_2(self):
        self.get_check_box_2().click()
        print("Check box Apple")

    def click_check_box_4(self):
        self.get_check_box_4().click()
        print("Check box Серия")

    def click_check_box_6(self):
        self.get_check_box_6().click()
        print("Check box - 256 ГБ")

    def click_smart_apple(self):
        self.get_smart_apple().click()
        print("Select iPhone 14 Pro")

    def click_add_to_cart(self):
        self.get_add_to_cart().click()
        print("Add to cart")

    def click_cart(self):
        self.get_cart().click()
        print("Enter to cart")

    def click_checkout(self):
        self.get_checkout().click()
        print("Enter to checkout")

    """Кликает и тянет slider цены"""
    def click_and_hold_price(self, element):
        action = ActionChains(self.driver)
        action.click_and_hold(element).move_by_offset(30, 0).release().perform()
        print("Click and hold price")

    """Наводиться на элемент, за приделами видимости экрана"""
    def move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        if element == self.get_list_apple():
            print("List Apple")
        else:
            pass

    """Наводиться и кликает на элемент(чек-боксы), за приделами видимости экрана"""
    def move_click_to_element(self, element, element_2):
        action = ActionChains(self.driver)
        action.move_to_element(element).click(element_2).perform()
        if element_2 == self.get_check_box_2():
            print("Check box Apple")
        elif element_2 == self.get_check_box_4():
            print("Check box Серия")
        elif element_2 == self.get_check_box_6():
            print("Check box - 256 ГБ")
        else:
            pass

    """Methods"""

    def select_check_box(self):
        with allure.step("Select check box"):
            Logger.add_start_step(method="select_check_box")
            self.get_current_url()
            self.assert_url("https://www.citilink.ru/catalog/smartfony/")
            self.screenshot()
            self.click_and_hold_price(self.get_price())
            self.move_click_to_element(self.get_check_box_1(), self.get_check_box_2())
            self.move_click_to_element(self.get_check_box_3(), self.get_check_box_4())
            self.move_click_to_element(self.get_check_box_5(), self.get_check_box_6())
            self.move_to_element(self.get_list_apple())
            self.click_smart_apple()
            self.assert_word(self.get_main_word(), "Смартфон Apple iPhone 14 Pro 256Gb, A2889, золотой")
            self.get_current_url()
            self.assert_url("https://www.citilink.ru/product/smartfon-apple-iphone-14-pro-a2889-256gb-zolotistyi-3g-4g-6-1-iphone-i-1863809/")
            self.screenshot()
            self.click_add_to_cart()
            self.click_cart()
            self.assert_word(self.get_main_word_2(), "Смартфон Apple iPhone 14 Pro 256Gb, A2889, золотой")
            self.get_current_url()
            self.assert_url("https://www.citilink.ru/order/")
            self.screenshot()
            self.click_checkout()
            self.get_current_url()
            self.assert_url("https://www.citilink.ru/order/checkout/")
            Logger.add_end_step(url=self.driver.current_url, method="select_check_box")