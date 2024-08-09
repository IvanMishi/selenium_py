from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Используем контекстный менеджер with для управления экземпляром браузера
with webdriver.Chrome() as webdriver:
    # Открываем веб-страницу по указанному URL
    webdriver.get('https://parsinger.ru/infiniti_scroll_2/')

    # Находим элемент по которому можно выполнить прокрутку колесом мыши, это не интерактивный элемент
    scroll_container = webdriver.find_element(By.CSS_SELECTOR, '#scroll-container > div')

    # Запускаем бесконечный цикл для прокрутки страницы
    while True:
        # Использует ActionChains для прокрутки страницы вниз, перемещая курсор к найденному элементу scroll_container и прокручивая его на 1 пиксель вправо и на 5 пикселей вниз.
        ActionChains(webdriver).move_to_element(scroll_container).scroll_by_amount(1, 5).perform()

        # Перебираем все найденные элементы <p>, если атрибут класса элемента равен 'last-of-list', элемент добавляется в результирующий список.
        last_of_list_elements = [x for x in webdriver.find_elements(By.TAG_NAME, 'p') if x.get_attribute('class') == 'last-of-list']

        # Если найден хотя бы один элемент с классом  'last-of-list'
        if last_of_list_elements:
            break  # Выходит из цикла, так как нужные элементы найдены

    # Добавляет в список значения текстовых элементов <p> на странице, которые содержат числовые значения.
    result = [int(x.text) for x in webdriver.find_elements(By.TAG_NAME, 'p') if x.text]
    # Суммирует все элементы списка result и выводит их на экран.
    print(sum(result))