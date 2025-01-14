import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице


# Cсылка на страницу
link = "https://parsinger.ru/methods/1/index.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    
    # Обновляет страницу пока в элементе не появится числовое значение.
    while True:
        try:
            actual_result = webdriver.find_element(By.CSS_SELECTOR, "[id='result']").text
            if actual_result.isdigit():  # Проверка на число
                break  # Выход из цикла, если текст найден в элементе
        except NoSuchElementException:
            pass
        webdriver.refresh()
    time.sleep(2)

    # Выводит значение переменной actual_result в консоль в качестве ответа
    print('Ответ', actual_result)


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
