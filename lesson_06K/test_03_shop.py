from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_shops():
    driver = webdriver.Edge()
    driver.maximize_window()
    # 1.Откройте страницу https://www.saucedemo.com/.
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 20)

    cookies = driver.get_cookies()
    for cookie in cookies:
        print(f"{cookie['name']}:{cookie['value']}")
    # Найдите поле ввода с названием имя пользователя
    # Введите в него ваше имя и т.д.
    element_n = driver.find_element(By.XPATH, "//*[@id='user-name']")
    element_n.send_keys("standard_user")
    element_p = driver.find_element(By.XPATH, "//*[@id='password']")
    element_p.send_keys("secret_sauce")
    # нажать на кнопку вход
    button_login = driver.find_element(By.XPATH, "//*[@id='login-button']")
    button_login.click()
    #  добавить в корзину товары
    # Sauce Labs Backpack
    button_add= driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
    button_add.click()
    # Sauce Labs Bolt T-Shirt
    button_add = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
    button_add.click()
    # Sauce Labs fleece jacket
    button_add = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']")
    button_add.click()
    # Перейдите в корзину
    button_entrance = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a")
    button_entrance.click()
    # нажмите кнопку Checkout
    button_Checkout = driver.find_element(By.XPATH, "//*[@id='checkout']")
    button_Checkout.click()
    # заполните форму FIRST NAME
    element_f = driver.find_element(By.XPATH, "//*[@id='first-name']")
    element_f.send_keys("Sveta")
    # заполните форму LAST NAME
    element_l = driver.find_element(By.XPATH, "//*[@id='last-name']")
    element_l.send_keys("Mamina")
    # заполните zip/Postal Code
    element_z = driver.find_element(By.XPATH, "//*[@id='postal-code']")
    element_z.send_keys("101105")
    # нажмите кнопку  Continue
    button_continue = driver.find_element(By.XPATH, "//*[@id='continue']")
    button_continue.click()
    # прочитайте итоговую стоимость(total)
    result_total = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[8]")
    result_total = result_total.text
    # проверяем результат
    assert result_total == "Total: $103.65", f"Ожидалось $103.65, но калькулятор показал {result_total}"
    # Закрываем  браузер после теста
    driver.quit()