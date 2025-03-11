from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Открытие браузера
with webdriver.Chrome() as browser:
    # Переход на указанную страницу
    browser.get("https://parsinger.ru/selenium/8/8.1.2/index.html")
    main_page = browser.current_window_handle
    time.sleep(1)

    # Поиск всех ссылок на странице
    links = browser.find_elements(By.CSS_SELECTOR, 'a')
    urls = [link.get_attribute('href') for link in links]
    # Открытие всех ссылок одновременно
    for url in urls:
        # Использование execute_script для открытия новой вкладки
        browser.execute_script(f"window.open('{url}', '_blank');")

    # Ждем, пока все вкладки откроются
    time.sleep(3)

    # Получаем все вкладки
    handles = browser.window_handles
    result = []

    # Переключаемся между всеми вкладками
    for handle in handles:
        browser.switch_to.window(handle)
        #time.sleep(3)  # Задержка для загрузки страницы
        n = browser.find_elements(By.CLASS_NAME, 'number')
        for k in n:
            result.append(k.text)

    # Вывод суммы чисел

    browser.switch_to.window(main_page)
    browser.find_element(By.ID, 'sumInput').send_keys(str(sum(int(i) for i in result)))
    time.sleep(6)
    browser.find_element(By.ID, 'checkButton').click()
    print(browser.find_element(By.ID, 'passwordDisplay').text)