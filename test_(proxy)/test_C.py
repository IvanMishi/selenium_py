import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице


# Список прокси-серверов, которые будут использоваться для соединения
proxy_list = ['8.210.83.33:80', '199.60.103.28:80',
'103.151.246.38:10001', '199.60.103.228:80',
'199.60.103.228:80', '199.60.103.28:80', ]


# Цикл по каждому прокси-серверу из списка
for PROXY in proxy_list:
    try: # Создает объект ChromeOptions для настройки параметров браузера Chrome.
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
        # Ссылка на страницу
        link = 'https://2ip.ru/'
        # Измеряет время выполнения
        start = time.time()


        with webdriver.Chrome(options=chrome_options) as driver:
            # Переходит по ссылке
            driver.get(link)
            time.sleep(1)  # Убеждается что открыта искомая страница
            # Ошибка будет выведена в консоль в случае если URL не совпадают.
            assert link == driver.current_url, f'\nОжидаемый   URL: {link}, \nФактический URL: {driver.current_url}'

            print('Извлекает текст элемента, который содержит IP-адрес пользователя на текущем прокси')
            print(driver.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
            # Устанавливает таймаут загрузки страницы (если страница загружается дольше 5 секунд, будет сгенерирована ошибка
            driver.set_page_load_timeout(5)
            print('Использованный прокси удален из списка, чтобы не использовать его повторно')
            proxy_list.remove(PROXY)

    except Exception as _ex:
        print(f"Превышен timeout ожидания для - {PROXY}")
        print('Продолжает цикл, переходя к следующему прокси')
        continue

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
