import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.common.keys import Keys # Импортирует класс Keys для эмуляции нажатия клавиш

# Ссылка на страницу.
link = 'https://parsinger.ru/selenium/5.10/6/index.html'
# Измеряет время выполнения.
start = time.time()


with webdriver.Chrome() as webdriver: # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link) # Переходит по ссылке.
    time.sleep(1) # Убеждается что открыта искомая страница.

    # Список слайдеров-конткйренов
    slider_container_list = webdriver.find_elements(By.CLASS_NAME, "slider-container")

    for slider in slider_container_list:
        # Находит слайдер внутри контейнера
        volume_slider = slider.find_element(By.CLASS_NAME, "volume-slider")
        # Получает текущее и целевое значение слайдера
        value = int(volume_slider.get_attribute("value"))
        target_value = int(slider.find_element(By.CLASS_NAME, "target-value").text)

        # Передвигаем слайдер к целевому значению
        while value != target_value:
            if value < target_value:
                # Увеличивает значение
                volume_slider.send_keys(Keys.ARROW_RIGHT)
                value += 1
            else:
                # Уменьшает значение
                volume_slider.send_keys(Keys.ARROW_LEFT)
                value -= 1
    time.sleep(1) # Визуально убеждается, что слайеры были перемещены

    # Находит элемент с результатом по его ID и выводит его текст
    print(f'Ответ: {webdriver.find_element(By.ID, 'message').text}')

    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")
    # Браузер закрывается автоматически после завершения блока `with`
