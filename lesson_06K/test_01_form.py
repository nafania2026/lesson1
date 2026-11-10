from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Edge()
    driver.maximize_window()
    # 1.Откройте страницу https://bonigarcia.dev/selenium-webdriver-java/data-types.html .
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html ")

    wait = WebDriverWait(driver, 10)

    cookies = driver.get_cookies()
    for cookie in cookies:
        print(f"{cookie['name']}:{cookie['value']}")
    # Найдите поле ввода с названием First Name.
    # Введите в него ваше имя и т.д.
    element_n = driver.find_element(By.NAME, "first-name")
    element_n.send_keys("Sveta")
    element_n = driver.find_element(By.NAME, "last-name")
    element_n.send_keys("Mamina")
    element_n = driver.find_element(By.NAME, "address")
    element_n.send_keys("Proekt,65-1")
    element_n = driver.find_element(By.NAME, "e-mail")
    element_n.send_keys("Svet_mam@kozly123456")
    element_n = driver.find_element(By.NAME, "phone")
    element_n.send_keys("+7985985885")
    element_n = driver.find_element(By.NAME, "city")
    element_n.send_keys("Moscow")
    element_n = driver.find_element(By.NAME, "country")
    element_n.send_keys("Russua")
    element_n = driver.find_element(By.NAME, "job-position")
    element_n.send_keys("QA")
    element_n = driver.find_element(By.NAME, "company")
    element_n.send_keys("Prosky")

    # находим и кликаем по кнопке submit
    button_submit = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    )
    button_submit.click()
    # обновление кода
    element_n = (WebDriverWait(driver, 10).until
                 (EC.presence_of_element_located((By.ID, "zip-code"))
    ))

    # driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

    # Проверяем (assert) Zip code  на красный цвет
    zip_field = driver.find_element(By.ID, "zip-code")
    # Кликаем по элементу в обход графического интерфейса
    driver.execute_script("arguments[0].click();", zip_field)
    # забираем цвет
    zip_border_color = zip_field.value_of_css_property("border-color")
    # Браузеры возвращают цвет в формате rgba  или rgb
    assert "245, 194, 199" in zip_border_color or "red" in zip_border_color, f"Zip code не красный! Получен цвет:rgb(245, 194, 199)"
    # assert ('255, 0, 0' in 'rgb(245, 194, 199)' or 'red' in 'rgb(245, 194, 199)')
    # Проверяем (assert), что остальные поля зелёные
    first_name_field = driver.find_element(By.ID, "first-name")
    first_name_color = first_name_field.value_of_css_property("border-color")
    assert "186, 219, 204" in first_name_color or "green" in first_name_color, f"FirstName не зеленое!Получен цвет:(186, 219, 204)"

    driver.quit()

