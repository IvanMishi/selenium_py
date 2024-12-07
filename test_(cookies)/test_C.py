import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице

# Cсылка на страницу
link = "https://parsinger.ru/methods/5/index.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Инициализирует пустой словарь для связи значений куки 'expiry' с INT из элемента <p id="result">INT</p>
    expiry_to_int_mapping = {}

    # Ищет все элементы с классом 'urls', которые являются ссылками на другие страницы
    links = webdriver.find_elements(By.CSS_SELECTOR, "[class='urls']")
    # Проходит по каждой найденной ссылке
    for link in links:
        # Переходит по ссылке, чтобы открыть соответствующую страницу
        link.click()
        # Получает все куки, связанные с текущей страницей
        cookies = webdriver.get_cookies()
        # Извлекает и парсит значение INT из элемента <p id="result">INT</p>
        int_value = int(webdriver.find_element(By.ID, "result").text)
        # Проходит по каждой куки и проверяет наличие ключа 'expiry'
        for cookie in cookies:
            if 'expiry' in cookie:
                # Преобразует значение 'expiry' куки в INT
                expiry_value = int(cookie['expiry'])
                # Добавляет связь между значением expiry и INT в словарь
                expiry_to_int_mapping[expiry_value] = int_value

        # Возвращается обратно на предыдущую страницу после сбора данных из текущей ссылки
        webdriver.back()

    # Находит самое большое значение куки 'expiry' из собранной информации
    max_expiry_value = max(expiry_to_int_mapping.keys(), default=None)
    # Проверяет, найдено ли самое большое значение 'expiry'
    if max_expiry_value is not None:
        # Получает соответсвующее INT значение для найденного максимального expiry
        max_int_value = expiry_to_int_mapping[max_expiry_value]

        # Выводит результат на экран в качестве ответа
        print(f"Самое большое значение куки 'expiry' относится к числу: {max_int_value}")
    else:
        # Выводит сообщение, если куки с ключом 'expiry' не найдены
        print("Куки с ключом 'expiry' не найдены.")

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`
