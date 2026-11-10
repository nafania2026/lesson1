from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Edge()
    driver.maximize_window()
    # 1.Откройте страницу https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    # настраиваем задержку калькулятора
    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear() # очистить поле
    delay_input.send_keys("45")
    # нажимаем кнопки на калькуляторе
    button_seven = driver.find_element(By.XPATH, "//span[text()='7']")
    button_seven.click()
    button_plus = driver.find_element(By.XPATH, "//span[text()='+']")
    button_plus.click()
    button_eight = driver.find_element(By.XPATH, "//span[text()='8']")
    button_eight.click()
    button_total = driver.find_element(By.XPATH, "//span[text()='=']")
    button_total.click()
    # используем явное ожидание
    # ждём до 50 секунд, пока калькулятор уляжется в 45 сек.
    WebDriverWait(driver,50).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR,".screen"),"15")
    )
    # Получаем результат
    result_element = driver.find_element(By.CSS_SELECTOR, "#calculator > div.top > div")
    result_text = result_element.text
    # проверяем результат
    assert result_text == "15", f"Ожидалось 15, но калькулятор показал {result_text}"
    # Закрываем  браузер после теста
    driver.quit()
    
