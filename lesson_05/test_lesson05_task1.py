import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    # открываем страницу
    driver.get('https://httpbin.qa-territory.online')
    time.sleep(2)
    # найти и кликнуть на ссылку HTML FORM
    click_button = driver.find_element(By.LINK_TEXT, "HTML Form")
    click_button.click()
    time.sleep(2)
    assert 'forms/post' in driver.current_url

    driver.back()
    time.sleep(2)

    assert 'https://httpbin.qa-territory.online' in driver.current_url
    # Ваш код здесь
    driver.quit()




    




