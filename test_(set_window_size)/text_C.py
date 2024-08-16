from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link ='http://parsinger.ru/blank/3/index.html'
# Измеряет время выполнения определенного участка кода.
start = time.time()


with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    # Убеждается что открыта искомая страница
    time.sleep(1)

    result = []
    input_elements = webdriver.find_elements(By.TAG_NAME, "input")

    # Пребирает каждый найденный элемент в списке input_elements
    for element in input_elements:
        # Вводит текст "Мой ответ" в каждый элемент ввода
        element.click()
        #time.sleep(1)
    #webdriver.switch_to.window(window_handles[0])


    for x in range(len(webdriver.window_handles)):
        webdriver.switch_to.window(webdriver.window_handles[x])
        result.append(webdriver.execute_script("return document.title;"))
        #time.sleep(1)

    # Инициализируем переменную для хранения суммы чисел
    total_sum = 0

    # Проходим по каждому элементу в списке и суммируем числа
    for item in result:
        if str(item).isnumeric():
            total_sum += int(item)

    # Выводим сумму чисел
    print("Сумма чисел в списке:", total_sum)


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")