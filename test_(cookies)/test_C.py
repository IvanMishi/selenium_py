import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице

# Cсылка на страницу
link = "https://parsinger.ru/methods/5/index.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()


with webdriver.Chrome() as driver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    driver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    # Ошибка будет выведена в консоль в случае если URL не совпадают.
    assert link == driver.current_url, f'\nОжидаемый   URL: {link}, \nФактический URL: {driver.current_url}'

    print('Инициализирует пустой словарь для связи значений куки "expiry" с INT из элемента <p id="result">INT</p>')
    expiry_to_int_mapping = {}

    print('Ищет все элементы с классом "urls", которые являются ссылками на другие страницы')
    links = driver.find_elements(By.CSS_SELECTOR, "[class='urls']")
    print('Проходит по каждой найденной ссылке')
    for link in links:
        print('Переходит по ссылке, чтобы открыть соответствующую страницу')
        link.click()
        print('Получает все куки, связанные с текущей страницей')
        cookies = driver.get_cookies()
        print('Извлекает и парсит значение INT из элемента <p id="result">INT</p>')
        int_value = int(driver.find_element(By.ID, "result").text)
        print('Проходит по каждой куки и проверяет наличие ключа "expiry"')
        for cookie in cookies:
            if 'expiry' in cookie:
                print('Преобразует значение "expiry" куки в INT')
                expiry_value = int(cookie['expiry'])
                print('Добавляет связь между значением expiry и INT в словарь')
                expiry_to_int_mapping[expiry_value] = int_value

        print('Возвращается обратно на предыдущую страницу после сбора данных из текущей ссылки')
        driver.back()

    print('Находит самое большое значение куки "expiry" из собранной информации')
    max_expiry_value = max(expiry_to_int_mapping.keys(), default=None)
    print('Проверяет, найдено ли самое большое значение "expiry"')
    if max_expiry_value is not None:
        print('Получает соответсвующее INT значение для найденного максимального expiry')
        max_int_value = expiry_to_int_mapping[max_expiry_value]

        print('Выводит результат на экран в качестве ответа')
        print(f"Самое большое значение куки 'expiry' относится к числу: {max_int_value}")
    else:
        # Выводит сообщение, если куки с ключом 'expiry' не найдены
        print("Куки с ключом 'expiry' не найдены.")

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")

