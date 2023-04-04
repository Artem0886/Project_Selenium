import allure
import pytest
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.smart_page import Smart_page
from pages.tv_page import Tv_page

@pytest.mark.order(2)
@allure.description("Test buy Apple")
def test_buy_product(set_up):

    print("Test buy Apple")

    login = Login_page(set_up)
    login.authorization()

    mp = Main_page(set_up)
    mp.select_smart()

    sp = Smart_page(set_up)
    sp.select_check_box()

    print("Finish test buy Apple")

@pytest.mark.order(1)
@allure.description("Test buy TV")
def test_buy_tv(set_up, set_group):

    print("Test buy TV")

    login = Login_page(set_up)
    login.authorization()

    mp = Main_page(set_up)
    mp.select_tv()

    tv = Tv_page(set_up)
    tv.select_tv_check_box()

    print("Finish test buy TV")