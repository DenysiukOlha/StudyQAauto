from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # створення обєкту сторінки
    sign_in_page = SignInPage()

    # відкриваємо сторінку https://github.com/login
    sign_in_page.go_to()

    # виконуємо спробу увійти в систему github
    sign_in_page.try_login('page_object@gmail.com', 'wrong password')

    # перевіряємо, що назва сторінки така, як ми очікуємо
    assert sign_in_page.check_title('Sign in to GitHub · GitHub')

    # закриваємо браузер
    sign_in_page.close()