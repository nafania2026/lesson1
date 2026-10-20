from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # 1. Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2
    driver.get ("https://the-internet.herokuapp.com/dynamic_loading/2")
    wait = WebDriverWait(driver, 10)
    # 2. нажмите кнопку start
    first_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[text()='Start']")
    ))
    first_button.click()
    # 3. Дождитесь появления текста "Hello World!"
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='Hello World!']")))
    # 4. Сделайте скриншот страницы
    driver.save_screenshot("full_screen_l6.png")
    # 5. Проверьте, что появившийся текст равен "Hello World!"
    hello_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Hello World!']")))

    driver.quit()
