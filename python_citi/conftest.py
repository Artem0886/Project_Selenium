import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def set_up():
    print("Start Test")
    url = "https://www.citilink.ru/"
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.maximize_window()
    yield driver
    print("Test Over")

@pytest.fixture(scope="module")
def set_group():
    print("ENTER SYSTEM")
    yield
    print("EXIT SYSTEM")