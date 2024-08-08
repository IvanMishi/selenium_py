# импортирует необходимые библиотеки
# импортирует модуль time для работы с ожиданием
import time
# импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver
# импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By

# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys

# ссылка на страницу
link = "http://parsinger.ru/infiniti_scroll_1/"

# Менеджер контекста with/as в Python используется для выполнения определенных действий до и после выполнения блока кода.
with webdriver.Chrome() as browser:
    # открывает браузер Chrome
    browser = webdriver.Chrome()
    # переходит по ссылке
    browser.get(link)
    time.sleep(2)

    list_input = []  # Инициализируем пустой список для хранения обработанных элементов ввода
    sum_of_numbers = 0  # Переменная для хранения суммы чисел

    # Флаг для проверки наличия элемента с классом last-of-list
    found_last_of_list = False

    while True:
        # Ищем все элементы input на веб-странице и добавляем их в список input_tags
        input_tags = browser.find_elements(By.CSS_SELECTOR, "#scroll-container span input")
        text_tags = browser.find_elements(By.CSS_SELECTOR, "#scroll-container span")

        # Обходим каждый элемент input в списке
        for tag_input, tag_text in zip(input_tags, text_tags):
            # Проверяем, не обрабатывали ли мы уже этот элемент ранее
            if tag_input not in list_input:
                tag_input.send_keys(Keys.DOWN)  # Отправляем клавишу "Вниз"
                browser.execute_script("return arguments[0].scrollIntoView(true);", tag_input)
                tag_input.click()  # Кликаем на элемент
                text = tag_text.text
                try:
                    number = int(text)
                except ValueError:
                    # Если текст не удалось преобразовать в число, пропускаем этот элемент
                    continue
                sum_of_numbers += number  # Суммируем числа
                list_input.append(tag_input)

        # Проверяем условие для завершения цикла while
        if len(input_tags) == 100:
            break
    print(f"Сумма чисел из элементов: {sum_of_numbers}")





       