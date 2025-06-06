import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами

# Cсылка на страницу
link = "https://parsinger.ru/selenium/3/3.2.2/index.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()


with webdriver.Chrome() as driver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    driver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    # Ошибка будет выведена в консоль в случае если URL не совпадают.
    assert link == driver.current_url, f'\nОжидаемый   URL: {link}, \nФактический URL: {driver.current_url}'

    print('Находит поле для ввода текста на веб-странице и заполняет его пользовательским текстом.')
    textarea = driver.find_element("id", "codeInput").send_keys('Дрогон')
    print('Находит кнопку на веб-странице и выполняет по ней клик.')
    pass_button = driver.find_element("id", "clickButton").click()
    print('Выводит текст из появившегося элемента  в качестве ответа в консоль.')
    print(f'Ответ: {driver.find_element("id", "codeOutput").text}')


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
