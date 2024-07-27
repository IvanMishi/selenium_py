import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get(r"https://parsinger.ru/selenium/5.7/3/index.html")

    list_input = []      # Инициализируем пустой список для хранения обработанных элементов ввода

    flag = True
    while flag:          # Начинаем бесконечный цикл
        # Ищем все элементы input на веб-странице и добавляем их в список input_tags
        input_tags = [x for x in browser.find_elements(By.TAG_NAME, 'input')]

        # Обходим каждый элемент input в списке
        for tag_input in input_tags:
            # Проверяем, не обрабатывали ли мы уже этот элемент ранее
            if tag_input not in list_input:
                browser.execute_script("return arguments[0].scrollIntoView(true);", tag_input)
                tag_input.click()                  # Кликаем на элемент
                time.sleep(.3)
                list_input.append(tag_input)       # Добавляем элемент в список обработанных элементов

                print(len(list_input), len(input_tags))

                if len(list_input) == 40:
                    flag = False