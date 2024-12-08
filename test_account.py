from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from Data.urls import Urls


class TestStellarBurgersProfileForm:

    def test_click_profile_button_open_profile_form(self, login):
        """ Открыть личный кабинет """
        driver = login

        driver.find_element(*MainPage.mn_profile_button).click()

        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Account.acc_info_message))
        profile = driver.find_element(*Account.acc_history_shop_button)
        assert Urls.url_profile == driver.current_url and profile.text == 'История заказов'


    def test_click_constructor_button_show_constructor_form(self, login):
        """ Переход из личного кабинета в конструктор при нажатии кнопки 'Конструктор' """
        driver = login

        driver.find_element(*MainPage.mn_profile_button).click()

        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Account.acc_info_message))
        driver.find_element(*MainPage.mn_constructor_button).click()

        h1_tag = driver.find_elements(By.XPATH, ".//h1")
        assert len(h1_tag) > 0 and h1_tag[0].text == 'Соберите бургер'


    def test_click_logo_button_show_constructor_form(self, login):
        """ Переход из личного кабинета в конструктор при нажатии на логотип """
        driver = login

        driver.find_element(*MainPage.mn_profile_button).click()

        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Account.acc_info_message))
        driver.find_element(*MainPage.mn_logo).click()

        h1_tag = driver.find_elements(By.XPATH, ".//h1")
        assert len(h1_tag) > 0 and h1_tag[0].text == 'Соберите бургер'


    def test_click_logout_button_in_lk_open_login_form(self, login):
        """ Выйти из аккаунта """
        driver = login

        driver.find_element(*MainPage.mn_profile_button).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(Account.acc_info_message))

        driver.find_element(*Account.acc_logout_button).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(AuthLogin.al_login_button_any_forms))

        login_button = driver.find_element(*AuthLogin.al_element_with_login_text)
        assert driver.current_url == Urls.url_login and login_button.text == 'Вход'
