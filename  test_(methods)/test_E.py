import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице

# Cсылка на страницу
link = "https://parsinger.ru/methods/1/index.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()


with webdriver.Chrome() as driver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    driver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    # Ошибка будет выведена в консоль в случае если URL не совпадают.
    assert link == driver.current_url, f'\nОжидаемый   URL: {link}, \nФактический URL: {driver.current_url}'
    print('Инициализирует переменную refresh_count как 0, чтобы начать с нулевой суммы')
    refresh_count = 0

    print('Обновляет страницу пока в элементе не появится числовое значение.')
    while True:
        try:
            actual_result = driver.find_element(By.CSS_SELECTOR, "[id='result']").text
            if actual_result.isdigit():  # Проверка на число
                break  # Выход из цикла, если текст найден в элементе
        except NoSuchElementException:
            pass
        driver.refresh()
        refresh_count += 1
    time.sleep(2)

    print('Выводит значение переменной actual_result в консоль в качестве ответа')
    print('Ответ', actual_result)
    print(f'Страница обновдена {refresh_count} раз')


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
