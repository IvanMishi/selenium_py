import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице


# Ссылка на страницу.
link = 'https://parsinger.ru/selenium/5.8/2/index.html'
# Измеряет время выполнения.
start = time.time()


with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Проверка существования элементов: находит все элементы на странице, которые являются элементами типа копка.
    button_elements = webdriver.find_elements(By.CSS_SELECTOR, ".buttons")
    # Cоздает пустой список для хранения найденных элементов.
    button_elements_list = []
    # Перебираем все найденные элементы
    for element in button_elements:
        # Добавляет каждый найденный элемент в список button_elements_list.
        button_elements_list.append(element)

    # Проверяет наличие найденных элементов
    # Если были найдены элементы
    if button_elements_list:
        # Определяет количество элементов, которые нужно обработать (минимум из длин обоих списков)
        for i in range(min(len(button_elements), len(button_elements_list))):
            # Кликает по кнопке
            button_elements_list[i].click()
            time.sleep(.01) # Пауза для корректной работы

            # После клика переключается на алерт.
            try:
                # Переключается на алерт, если он появляется, сохраняет его текст в переменную и принимает его.
                alert = webdriver.switch_to.alert
                alert_text = alert.text
                alert.accept()
            # Заполняет поле проверки валидности пин-кода и нажимает кнопку проверить, если в элменте result значение меняется с дефолтного на иное, выводит текст в консоль в качестве ответа.
                input_check = webdriver.find_element(By.CSS_SELECTOR, "#input").send_keys(alert_text)
                button_check = webdriver.find_element(By.CSS_SELECTOR, "#check").click()
                result = webdriver.find_element(By.CSS_SELECTOR, "[id='result']").text
                if result == 'Неверный пин-код':
                    continue
                else:
                    print(f'Ответ: {result}')
            except NoAlertPresentException:
                # Обрабатывает случай, если алерт не появился
                print("Алерт не появился.")
            except Exception as e:
                # Обрабатывает другие исключений, если необходимо
                print(f'Произошла ошибка: {e}')

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`