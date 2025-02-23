import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице

# Определяет адрес прокси-сервера, который будет использоваться для интернет-соединения.
#proxy = '8.210.83.33:80'
# Cсылка на страницу
link = 'https://2ip.ru/'
# Создает объект ChromeOptions для настройки параметров браузера Chrome.
chrome_options = webdriver.ChromeOptions()
# Добавляет аргумент с прокси-сервером в настройки браузера.
#chrome_options.add_argument('--proxy-server=%s' % proxy)


with webdriver.Chrome(
        options=chrome_options) as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    # Находит элемент на странице с ID 'd_clip_button' и затем в нем находим тег 'span'.
    # Извлекает текст из найденного элемента и выводит его в консоль.
    print(webdriver.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
    # Ждет 5 секунд
    time.sleep(5)