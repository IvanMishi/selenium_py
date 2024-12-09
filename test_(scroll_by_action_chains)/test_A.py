import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.common.action_chains import ActionChains # Модуль Selenium для выполнения комплексных действий с веб-элементами, включая наведение курсора, нажатие клавиш и перетаскивание.



# Cсылка на страницу
link = "https://parsinger.ru/infiniti_scroll_2/"
# Измеряет время выполнения определенного участка кода.
start = time.time()


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.



    # Находит элемент по которому можно выполнить прокрутку колесом мыши, это не интерактивный элемент
    scroll_container = webdriver.find_element(By.CSS_SELECTOR, '#scroll-container > div')

    # Запускаем бесконечный цикл для прокрутки страницы
    while True:
        # Использует ActionChains для прокрутки страницы вниз, перемещая курсор к найденному элементу scroll_container и прокручивая его на 1 пиксель вправо и на 5 пикселей вниз.
        ActionChains(webdriver).move_to_element(scroll_container).scroll_by_amount(1, 5).perform()

        # Перебираемт все найденные элементы <p>, если атрибут класса элемента равен 'last-of-list', элемент добавляется в результирующий список.
        last_of_list_elements = [x for x in webdriver.find_elements(By.TAG_NAME, 'p') if
                                 x.get_attribute('class') == 'last-of-list']

        # Если найден хотя бы один элемент с классом  'last-of-list'
        if last_of_list_elements:
            break  # Выходит из цикла, так как нужные элементы найдены

    # Добавляет в список значения текстовых элементов <p> на странице, которые содержат числовые значения.
    result = [int(x.text) for x in webdriver.find_elements(By.TAG_NAME, 'p') if x.text]
    # Суммирует все элементы списка result и выводит их на экран.
    print(sum(result))



# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`
