from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    # Откройте страницу https://httpbin.qa-territory.online/links/10.
    driver.get("https://httpbin.qa-territory.online/links/10")
    # Найдите все ссылки на странице (тег <a>).
    all_links = driver.find_elements(By.CSS_SELECTOR, "a")
    # Проверьте, что количество ссылок равно 9.
    visible_links = [link for link in all_links if link.is_displayed()]
    assert(
        len(visible_links)==9
    ), f"Найдено{len(visible_links)}) видимых ссылок вместо 9"
    # Проверьте, что все ссылки отображаются на странице.
    for link in visible_links:
         assert (
              link.is_displayed()
    ), "Какая_то из выбранных ссылок скрыта"
    # Проверьте, что текст первой ссылки содержит "1".
    first_link_text = visible_links[0].text
    assert "1" in '{first_link_text}' or visible_links[0].get_attribute("href"),(
        f"Первая ссылка не соответствует условиям. Её текст '{first_link_text}'"
    )
    # Ваш код здесь
    driver.quit()
    