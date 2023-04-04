import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

class Tv_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""

    price_min = "(//input[@name='input-min'])[2]"
    price_max = "(//input[@name='input-max'])[2]"
    check_box_1 = "//div[@data-meta-value='Бренд']"
    check_box_2 = "//div[@data-meta-value='SAMSUNG']"
    check_box_3 = "//div[@data-meta-value='Диагональ']"
    check_box_4 = "(//span[contains(text(),'65')])[1]"
    check_box_5 = "//div[@data-meta-value='Технология экрана']"
    check_box_6 = "//div[@data-meta-value='Neo QLED']"
    list_tv = "//h1[@class='e1e4gwta0 eml1k9j0 app-catalog-yhwyfr e1gjr6xo0']"
    tv_samsung = "//a[contains(text(),'Samsung QE65QN900AUXRU, Neo QLED, 8K Ultra HD, нержавеющая сталь, СМАРТ ТВ, Tizen OS')]"
    main_word = "//h1[@class='e1ubbx7u0 eml1k9j0 app-catalog-tn2wxd e1gjr6xo0']"
    main_word_2 = "//span[@class='e1ys5m360 e106ikdt0 css-175fskm e1gjr6xo0']"
    add_to_cart = "//button[@data-meta-name='BasketDesktopButton']"
    cart = "//button[@class='e4uhfkv0 css-10je9jt e4mggex0']"
    checkout = "//button[@title='Перейти к оформлению']"

    """Getters"""

    def get_price_min(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_min)))

    def get_price_max(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_max)))

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

    def get_list_tv(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.list_tv)))

    def get_tv_samsung(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.tv_samsung)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_main_word_2(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.main_word_2)))

    def get_add_to_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart)))

    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_checkout(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkout)))

    """Actions"""

    def click_check_box_2(self):
        self.get_check_box_2().click()
        print("Check box SAMSUNG")

    def click_check_box_4(self):
        self.get_check_box_4().click()
        print("Check box 65 дюймов")

    def click_check_box_6(self):
        self.get_check_box_6().click()
        print("Check box Neo QLED")

    def click_tv_samsung(self):
        self.get_tv_samsung().click()
        print("Select TV Samsung")

    def click_add_to_cart(self):
        self.get_add_to_cart().click()
        print("Add to cart")

    def click_cart(self):
        self.get_cart().click()
        print("Enter to cart")

    def click_checkout(self):
        self.get_checkout().click()
        print("Enter to checkout")

    """Очищает поле с минимальной ценой и вводит свою"""
    def clear_price_min(self):
        self.get_price_min().clear()
        self.get_price_min().send_keys("100000")
        print("Price min 100000")

    """Очищает поле с максимальной ценой и вводит свою"""
    def clear_price_max(self):
        self.get_price_max().clear()
        self.get_price_max().send_keys("400000")
        print("Price max 400000")

    """Наводиться на элемент, за приделами видимости экрана"""
    def move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        if element == self.get_list_tv():
            print("List TV Samsung")
        else:
            pass

    """Наводиться и кликает на элемент(чек-боксы), за приделами видимости экрана"""
    def move_click_to_element(self, element, element_2):
        action = ActionChains(self.driver)
        action.move_to_element(element).click(element_2).perform()
        if element_2 == self.get_check_box_2():
            print("Check box Samsung")
        elif element_2 == self.get_check_box_4():
            print("Check box 65 дюймов")
        elif element_2 == self.get_check_box_6():
            print("Check box Neo QLED")
        else:
            pass

    """Methods"""

    def select_tv_check_box(self):
        with allure.step("Select TV check box"):
            Logger.add_start_step(method="select_tv_check_box")
            self.get_current_url()
            self.assert_url("https://www.citilink.ru/catalog/televizory/")
            self.screenshot()
            self.clear_price_min()
            self.clear_price_max()
            self.move_click_to_element(self.get_check_box_1(), self.get_check_box_2())
            self.move_click_to_element(self.get_check_box_3(), self.get_check_box_4())
            self.move_click_to_element(self.get_check_box_5(), self.get_check_box_6())
            self.move_to_element(self.get_list_tv())
            self.click_tv_samsung()
            self.assert_word(self.get_main_word(), '65" Телевизор Samsung QE65QN900AUXRU, Neo QLED, 8K Ultra HD, нержавеющая сталь, СМАРТ ТВ, Tizen OS')
            self.get_current_url()
            self.assert_url("https://www.citilink.ru/product/televizor-qled-samsung-65-qe65qn900auxru-smart-q-serebristyi-4k-ultra-1833886/")
            self.screenshot()
            self.click_add_to_cart()
            self.click_cart()
            self.assert_word(self.get_main_word_2(), '65" Телевизор Samsung QE65QN900AUXRU, Neo QLED, 8K Ultra HD, нержавеющая сталь, СМАРТ ТВ, Tizen OS')
            self.get_current_url()
            self.assert_url("https://www.citilink.ru/order/")
            self.screenshot()
            self.click_checkout()
            self.get_current_url()
            self.assert_url("https://www.citilink.ru/order/checkout/")
            Logger.add_end_step(url=self.driver.current_url, method="select_tv_check_box")