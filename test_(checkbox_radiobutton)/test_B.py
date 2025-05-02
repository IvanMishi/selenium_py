import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице


# Ссылка на страницу.
link = 'https://parsinger.ru/selenium/4/4.html'
# Измеряет время выполнения.
start = time.time()


with webdriver.Chrome() as driver: # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    driver.get(link) # Переходит по ссылке.
    time.sleep(1) # Убеждается что открыта искомая страница.
    assert link == driver.current_url, f'\nОжидаемый   URL: {link}, \nФактический URL: {driver.current_url}'  # Ошибка будет выведена в консоль в случае если URL не совпадают
    print('Url корректный')

    # Находит чекбокс элементы  на веб странице.
    checkboxs = driver.find_elements(By.CSS_SELECTOR, "[type='checkbox']")
    print(f'Чекбоксы найдены: {len(checkboxs)} шт')
    # Перебирает каждый найденный элемент в списке checkboxs
    for element in checkboxs:
        element.click() # Отмечает каждый найденый чекбокс
    print('Чекбоксы отмечны')
    # Нажимает кнопку отправки формы на веб-странице
    button_submit = driver.find_element(By.CSS_SELECTOR, "[type='button']").click()
    time.sleep(1)  # Визуально убеждается, что все действия выполнены.
    
    # Находит элемент с результатом по его ID и выводит его текст
    print(f"Ответ: {driver.find_element(By.ID, 'result').text}")

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")

