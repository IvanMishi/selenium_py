import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице

# Ссылка на страницу.
link = 'https://parsinger.ru/selenium/5.8/1/index.html'
# Измеряет время выполнения.
start = time.time()


with webdriver.Chrome() as driver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    driver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    assert link == driver.current_url, f'\nОжидаемый   URL: {link}, \nФактический URL: {driver.current_url}' # Ошибка будет выведена в консоль в случае если URL не совпадают

    # Проверяет наличие чекбоксов на странице с помощью find_elements() и отмечает их, если они найдены.
    checkbox_elements = driver.find_elements(By.CSS_SELECTOR, ".buttons")
    # Создает пустой список для найденных элементов.
    checkbox_elements_list = []

    # Перебирает все найденные элементы
    for element in checkbox_elements:
        # Добавляет найденные элементы в список checkbox_elements_list.
        checkbox_elements_list.append(element)

    # Проверяем наличие элементов в checkbox_elements_list
    if checkbox_elements_list:
        # Определяем минимальное количество элементов для обработки из обоих списков.
        for i in range(min(len(checkbox_elements), len(checkbox_elements_list))):
            # Выполняем клик по чекбоксу
            checkbox_elements_list[i].click()

            # После клика переключается и принимает алерт и выводит результат, если он есть.
            try:
                # Переключается на алерт, если он появляется и принимает его.
                alert = driver.switch_to.alert
                alert.accept()

                # Выводит ответ, если он есть.
                result = driver.find_element(By.CSS_SELECTOR, "[id='result']").text; print(f'Ответ: {result}') if result else None

            except NoAlertPresentException:
            # Обрабатывает случай, если алерт не появился
                print("Алерт не появился.")
            except Exception as e:
            # Обрабатывает другие исключений, если необходимо
                print(f'Произошла ошибка: {e}')

    # Убеждается, что все действия выполнены успешно.
    time.sleep(3)

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
