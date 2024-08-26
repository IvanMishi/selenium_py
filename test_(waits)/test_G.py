import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями


# Ссылка на страницу
link = 'https://parsinger.ru/selenium/5.9/5/index.html'
# Измеряет время выполнения
start = time.time()

with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    time.sleep(1) # Убеждается что открыта искомая страница

    # Список для хранения кнопок, которые были нажаты
    catch_buttons = []
    answer = []

    while True:
        # Находит все элементы на веб-странице, у которых есть класс 'box_button', и создает список этих элементов.
        button_list = [x for x in webdriver.find_elements(By.CLASS_NAME, 'box_button')]

        # Проходит по списку кнопок
        for button in button_list:
            if button not in catch_buttons: # Если кнопка еще не нажата
                button.click()  # Нажимает на кнопку
                # Закрываем рекламное окно, если оно существует
                try:
                    close_ad = WebDriverWait(webdriver, 10).until(
                        EC.element_to_be_clickable((By.ID, 'close_ad'))).click()
                    WebDriverWait(webdriver, 10).until(EC.invisibility_of_element_located((By.ID, 'ad_window')))
                except Exception as e:
                    print("Ошибка при закрытии рекламы:", e)

                # Ждет, пока текст кнопки не станет ненулевым (не пустым).
                WebDriverWait(webdriver, 10).until(lambda d: button.text != "") # Лямбда-функция, которая проверяет, что текст кнопки (button.text) не является пустой строкой.
                # Получает текст кнопки
                text = button.text
                answer.append(text)
                # Добавляет кнопку в уже нажатые
                catch_buttons.append(button)

                # Если количество нажатых кнопок стало равно количеству найденых кнопок, задача выполнена.
                if len(catch_buttons) == len(button_list):
                    break
        if len(catch_buttons) == len(button_list):
            break
    # Выводит в консоль в качестве ответа текст из каждой найденой кнопки если он есть, объединяет все элементы в списке answer в одну строку, разделяя их символом "-"
    print(f'Ответ: {"-".join(answer)}')

    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")
    # Браузер закрывается автоматически после завершения блока `with`
