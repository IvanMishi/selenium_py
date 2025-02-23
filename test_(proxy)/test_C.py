import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице

# Список прокси-серверов, которые будут использоваться для соединения
proxy_list = ['8.210.83.33:80', '199.60.103.28:80',
'103.151.246.38:10001', '199.60.103.228:80',
'199.60.103.228:80', '199.60.103.28:80', ]

# Цикл по каждому прокси-серверу из списка
for PROXY in proxy_list:
    try: # Создает объект для указания опций работы Chrome
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % PROXY)  # Устанавливает текущий прокси-сервер
        link = 'https://2ip.ru/' # Cсылка на страницу

        with webdriver.Chrome(options=chrome_options) as webdriver: # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
            webdriver.get(link) # Переходит по ссылке.
            print(webdriver.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text) # Извлекает текст элемента, который содержит IP-адрес пользователя на текущем прокси
            # Устанавливает таймаут загрузки страницы (если страница загружается дольше 5 секунд, будет сгенерирована ошибка)
            webdriver.set_page_load_timeout(5)
            # Удаляет использованный прокси из списка, чтобы не использовать его повторно
            proxy_list.remove(PROXY)
    except Exception as _ex:
        print(f"Превышен timeout ожидания для - {PROXY}")
        continue # Продолжаем цикл, переходя к следующему прокси