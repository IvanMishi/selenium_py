import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.common.action_chains import ActionChains


# Ссылка на страницу.
link = "https://parsinger.ru/selenium/5.7/5/index.html"
# Измеряет время выполнения.
start = time.time()


with webdriver.Chrome() as driver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    driver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    assert link == driver.current_url, f'\nОжидаемый   URL: {link}, \nФактический URL: {driver.current_url}' # Ошибка будет выведена в консоль в случае если URL не совпадают

    # Находит контейнер с кнопками .
    container_parrent = driver.find_elements(By.CSS_SELECTOR, "[id='main_container'] button")
    # Перебирает найденные кнопки.
    for element in container_parrent:
        timer = element.get_attribute('value') # Поучает время удержания кнопки из атрибута.
        # Удерживает кнопку на заданное время.
        ActionChains(driver).click_and_hold(element).pause(float(timer)).release(element).perform()


    # Получает alert на веб-странице и переключается на него.
    alert = driver.switch_to.alert
    # Выводит значение полученного текста из alert в консоль в качестве ответа.
    print(f'Ответ {alert.text}')
    # Принимает и закрывает alert путем нажатия кнопки "OK" (accept).
    alert.accept()
    # Убеждается, что все действия выполнены успешно.
    time.sleep(3)

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
