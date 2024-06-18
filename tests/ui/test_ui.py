import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.mark.ui
def test_check_incorrect_username():
    # Створення обєкту для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # відкриваємо сторінку https://github.com/login
    driver.get('https://github.com/login')

    # знаходимо поле, в яке будемо вводити неправильне імя та пароль
    login_elem = driver.find_element(By.ID, 'login_field')
    pass_elem = driver.find_element(By.ID, 'password')

    # вводимо неправильне імя користувача та пароль
    login_elem.send_keys('olha@gemail.com')
    pass_elem.send_keys('wrong password')

    # знаходимо кнопку sign in
    btn_elem = driver.find_element(By.NAME, 'commit')

    # емулюємо клік ЛКМ
    btn_elem.click()

    # Перевіряємо, що назва сторінки така ,як ми очікуємо
    assert driver.title == 'Sign in to GitHub · GitHub'
    time.sleep(3)

    # закриваємо браузер
    driver.close()