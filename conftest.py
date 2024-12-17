import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from Data.urls import Urls
from Data.data import PersonData
from tests.locators import MainPage, AuthLogin


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1300,1200")
    driver = webdriver.Chrome(options=options)
    driver.get(Urls.url_main_paige)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    """ Войти в аккаунт """
    driver.get(Urls.url_login)

    driver.find_element(*AuthLogin.al_email_field).send_keys(PersonData.login)
    driver.find_element(*AuthLogin.al_password_field).send_keys(PersonData.password)
    driver.find_element(*AuthLogin.al_login_button_any_forms).click()

    WebDriverWait(driver, 3).until(EC.presence_of_element_located(MainPage.mn_order_button))
    return driver