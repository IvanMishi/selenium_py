import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице

# Незарегестированный пользователь переходит по ссылке
# Собирает данные о жизни куки в каждой найденной ссылке переходя по ней
# Ищет куки с самым долгим сроком жизни и выводит в качестве ответа число из тега <p id="result">INT</p> на странице этого куки


# Cсылка на страницу
link = "https://parsinger.ru/methods/5/index.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()
# Переменная для хранения количества найденных элементов.
count = 0


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Инициализирует пустой словарь для связи значений куки 'expiry' с INT из элемента <p id="result">INT</p>
    expiry_to_int_mapping = {}

    #
    links = webdriver.find_elements(By.CSS_SELECTOR, "[class='urls']")
    # проходит по каждой ссылке
    for link in links:
        # переходит на найденную ссылку
        link.click()
        # получает все куки из этой ссылки
        cookies = webdriver.get_cookies()
        # Парсит значение INT из элемента <p id="result">INT</p> из ссылки
        int_value = int(webdriver.find_element(By.ID, "result").text)
        # Проходит по каждой куки и проверяем наличие ключа 'expiry'
        for cookie in cookies:
            if 'expiry' in cookie:
                expiry_value = int(cookie['expiry'])
                expiry_to_int_mapping[expiry_value] = int_value
        # Возвращается назад после сбора данных из ссылки
        webdriver.back()

    # Находим самое большое значение куки 'expiry'
    max_expiry_value = max(expiry_to_int_mapping.keys(), default=None)
    if max_expiry_value is not None:
        max_int_value = expiry_to_int_mapping[max_expiry_value]
        print(f"Самое большое значение куки 'expiry' относится к числу: {max_int_value}")
    else:
        print("Куки с ключом 'expiry' не найдены.")

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`
