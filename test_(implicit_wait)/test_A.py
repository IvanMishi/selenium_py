import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице




# Ссылка на страницу
link = 'https://demoqa.com/dynamic-properties'
# Измеряет время выполнения
start = time.time()

with webdriver.Chrome() as driver:
    # Переходит по ссылке
    driver.get(link)
    time.sleep(1) # Убеждается что открыта искомая страница

    # Неявное ожидание для каждого найденого элемента
    driver.implicitly_wait(10)

    #Находит кнопку на странице и нажимает на нее 
    driver.find_element(By.ID, 'enableAfter').click()
    print('Кнопка была нажата успешно') 

    # Завершение отсчета времени
    end = time.time()
    print(f"Время выполнения: {end - start} секунд.")


    

