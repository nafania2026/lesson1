from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.maximize_window()
# 1.Откройте страницу https://gitflic.ru/.
    driver.get("https://gitflic.ru/")
    wait = WebDriverWait(driver, 10)
# 2.Установите cookie пользователя 1.
    driver.add_cookie({
        "name": "SESSION",
        "value": "NzEzZmFkNzctOTdhMy00MTBkLTgxYTEtYWM2MDg1ZGE3ZDE3",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })
# 3.Обновите страницу.
    driver.refresh()
# 4.Перейдите на страницу пользователя 1.
    driver.get("https://gitflic.ru/user/kozly123456")
    wait = WebDriverWait(driver, 10)
# 5.Сохраните текущий URL.
    url_user1 = driver.current_url
    with open("saved_urls.txt", "w", encoding="utf-8") as file:
        file.write(f"Текущий URL 1: {url_user1}\n")
# 6.Разлогиньтесь (очистите куки).
    driver.delete_all_cookies()
    driver.refresh()
    #yield driver
    #driver.quit()

# 1.Откройте страницу заново https://gitflic.ru/.
    driver.get("https://gitflic.ru/")
# 7.Установите cookie пользователя 2.
    driver.add_cookie({
        "name": "SESSION",
        "value": "ZTFhMTQ0OTEtMTQ4OS00ZGZlLTg2YjYtZDZhYTU5ZmM4NGZj",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })
# 8.Обновите страницу.
    driver.refresh()
# 9.Перейдите на страницу пользователя 2.
    driver.get("https://gitflic.ru/user/pipa1234")
# 10.Сохраните текущий URL.
    url_user2 = driver.current_url
    with open("saved_urls.txt", "a", encoding="utf-8") as file:
        file.write(f"Текущий URL 2: {url_user2}\n")
# 11.Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
    assert url_user1 != url_user2,"URL пользователей одинаковые, авторизация не сменилась!"

    driver.quit()