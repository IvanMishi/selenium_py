import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице


# Ссылки на страницы в виде списка.
sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html', 'http://parsinger.ru/blank/1/3.html', 'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html',]
# Измеряет время выполнения.
start = time.time()
# Инициализирует переменную для сбора результатов
total_resut = 0

with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    # Переходит по каждому сайту в списке sites
    for site in sites:
        webdriver.get(site) # Открывает сайт
        # Находит элемент с типом "checkbox" и устанавливает его в состояние "checked"
        checkbox_element = webdriver.find_element(By.CSS_SELECTOR, '[type="checkbox"]').click()
        # Извлекает текст из элемента с id "result"
        result = webdriver.find_element(By.CSS_SELECTOR, '[id="result"]').text
        # Обновляет общую сумму, добавляя квадратный корень из извлеченного результата
        total_resut = total_resut + (int(result) ** 0.5)
        time.sleep(1)  # Убеждается что открыта искомая страница.
    # Выводит итоговую сумму, округленную до 9 знаков после запятой
    print(f'Ответ: {round(total_resut, 9)}')

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`