from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from Data.urls import Urls
from Data.data import PersonData


class TestStellarBurgersLoginLogoutForm:

    def test_login_correct_email_and_password_show_main_page(self, login):
        """ При вводе корректных данных отображается главная страница """
        driver = login

        order_button = driver.find_element(*MainPage.mn_order_button)
        assert driver.current_url == Urls.url_main_paige and order_button.text == 'Оформить заказ'


    def test_login_sign_in_button_show_login_page(self, driver):
        """ Проверка входа по кноке 'Войти в аккаунт' """

        driver.find_element(*MainPage.mn_auth).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(AuthLogin.al_login_text))

        driver.find_element(*AuthLogin.al_email_field).send_keys(PersonData.login)
        driver.find_element(*AuthLogin.al_password_field).send_keys(PersonData.password)

        driver.find_element(*AuthLogin.al_login_button_any_forms).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPage.mn_order_button))

        order_button = driver.find_element(*MainPage.mn_order_button)
        assert driver.current_url == Urls.url_main_paige and order_button.text == 'Оформить заказ'


    def test_login_personal_account_button_show_login_page(self, driver):
        """ Проверка входа через кнопку 'Личный Кабинет' """

        driver.find_element(*MainPage.mn_profile_button).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(AuthLogin.al_login_text))

        driver.find_element(*AuthLogin.al_email_field).send_keys(PersonData.login)
        driver.find_element(*AuthLogin.al_password_field).send_keys(PersonData.password)

        driver.find_element(*AuthLogin.al_login_button_any_forms).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(MainPage.mn_order_button))

        order_button = driver.find_element(*MainPage.mn_order_button)
        assert driver.current_url == Urls.url_main_paige and order_button.text == 'Оформить заказ'


    def test_login_registration_form_sign_in_button(self, driver):
        """ Проверка входа через кнопку 'Войти' в форме регистрации """
        driver.get(Urls.url_register)

        driver.find_element(*AuthLogin.al_login_text_with_href).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(AuthLogin.al_login_text))

        driver.find_element(*AuthLogin.al_email_field).send_keys(PersonData.login)
        driver.find_element(*AuthLogin.al_password_field).send_keys(PersonData.password)

        driver.find_element(*AuthLogin.al_login_button_any_forms).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(MainPage.mn_order_button))

        order_button = driver.find_element(*MainPage.mn_order_button)
        assert driver.current_url == Urls.url_main_paige and order_button.text == 'Оформить заказ'


    def test_login_forgot_password_form_sign_in_button(self, driver):
        """ Проверка входа через кнопку 'Войти' в форме 'Восстановление пароля' """
        driver.get(Urls.url_forgot_password)

        driver.find_element(*AuthPassword.ap_login_text_with_href).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(AuthLogin.al_login_text))

        driver.find_element(*AuthLogin.al_email_field).send_keys(PersonData.login)
        driver.find_element(*AuthLogin.al_password_field).send_keys(PersonData.password)

        driver.find_element(*AuthLogin.al_login_button_any_forms).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(MainPage.mn_order_button))

        order_button = driver.find_element(*MainPage.mn_order_button)
        assert driver.current_url == Urls.url_main_paige and order_button.text == 'Оформить заказ'
