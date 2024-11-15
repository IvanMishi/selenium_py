import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице


# Ссылка на страницу.
link = 'https://parsinger.ru/selenium/5.8/3/index.html'
# Измеряет время выполнения.
start = time.time()

with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.

    # Находит все поля с значением пин-кода и формирует из них список
    pin_codes = webdriver.find_elements(By.CSS_SELECTOR, ".pin")
    # Находит кнопку для проверки значений пин-кода
    button_check = webdriver.find_element(By.CSS_SELECTOR, ".main #check")
    # Находит подсказку о корректности пин-кода
    result = webdriver.find_element(By.CSS_SELECTOR, "#result")
    # Счетчик для пин-кодов
    count = 0

    # Перебирает все значения в списке pin_codes
    for pin in pin_codes:
        # Извлекатм текст текущего элемента pin, который предполагается как пин-код
        extracted_text = pin.text
        # Кликает на кнопку для проверки пин-кода
        button_check.click()
        # Получает всплывающее сообщение (alert) для ввода пин-кода
        alert = webdriver.switch_to.alert
        # Вводит извлеченный пин-код в всплывающее сообщение
        alert.send_keys(extracted_text)
        # Подтверждает (принимает) введенное значение, что инициирует проверку
        alert.accept()
        # Увеличивает счетчик проверенных пин-кодов на 1
        count+=1
        # Проверяем текст результата проверки пин-кода
        if result.text == 'Неверный пин-код':
            # Если пин-код неверен, то подсказка не поменялась, продолжаем цикл со следующим пин-кодом
           continue
        else:
            # Если пин-код верный, то в подсказке поменялся текст, сохраняем результат в переменной find
            find = result.text
            break
# Выводим сообщение с номером элемента и верным пин-кодом
print(f'Ответ: Элемент № {count} содержит верный пин-код {find}')

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`
