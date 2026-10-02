from selenium import webdriver
from selenium.webdriver.common.by import By


def test_submission():
    driver = webdriver.Chrome()
    # открываем страницу
    driver.get('https://httpbin.qa-territory.online/forms/post')
    #time.sleep(2)
    #Найдите поле ввода с названием custname.
    #Введите в него ваше имя.
    username_field = driver.find_element(By.NAME, "custname")
    username_field.send_keys("Света Лунёва")
    #Найдите кнопку Submit и нажмите на нее.
    order_button = driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
    )
    order_button.click()
    #Проверьте, что после нажатия URL изменился.
    assert '/post' in driver.current_url

    driver.back()
    #time.sleep(2)

    driver.quit()
    