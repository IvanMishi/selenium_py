import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver import Keys # Класс Keys из модуля webdriver библиотеки Selenium, который содержит специальные клавиши, такие как ENTER, ESC и TAB, для имитации нажатий в автоматизированных тестах веб-приложений.

# Cсылка на страницу
link = "https://parsinger.ru/selenium/5.7/3/index.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()

with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    list_input = []  # Инициализируем пустой список для хранения обработанных элементов ввода


    while True:  # Начинает бесконечный цикл, который будет продолжаться до тех пор, пока все элементы не станут обработанными, количество элментов не известно
        # Ищет все элементы input на веб-странице и добавляем их в список input_tags
        input_tags = [x for x in webdriver.find_elements(By.TAG_NAME, 'input')]

        # Обходит каждый элемент input в списке
        for tag_input in input_tags:
            # Проверяет, не обрабатывался ли уже этот элемент ранее, чтобы избежать повторной обработки
            if tag_input not in list_input:
                tag_input.send_keys(Keys.DOWN)  # Отправляем клавишу "Вниз"
                tag_input.click()  # Кликаем на элемент
                time.sleep(1)
        if len(input_tags) == 10:
            break



# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`
