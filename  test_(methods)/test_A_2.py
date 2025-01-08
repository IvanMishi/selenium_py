import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице


# Cсылка на страницу
link = "https://suninjuly.github.io/text_input_task.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()

with webdriver.Chrome() as webdriver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    webdriver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    # Переменная  содержит текст, который участник тестового сценария ожидает увидеть после успешного завершения теста.
    expected_result = "Thank you for submitting the form!"

    # Находит поле для ввода текста на веб-странице
    textarea = webdriver.find_element("class name", "textarea")
    # Заполняет поле данными
    textarea.send_keys("пользовательский текст")
    # Ждет 2 секунды
    time.sleep(2)

    # Находит кнопку отправки формы на веб-странице, используя уникальный идентификатор "submit_button"
    submit_button = webdriver.find_element("id", "submit_button")
    # Нажимает на кнопку отправки формы
    submit_button.click()

    # Убеждается, что текст всплывающего окна (alert) соответствует ожидаемому результату. Если текст в алерте не совпадает с ожидаемым текстом, будет выведено сообщение об ошибке.
    # Получает alert на веб-странице
    alert = webdriver.switch_to.alert
    # Сохраняет текст предупреждения (alert) в переменной actual_result
    actual_result = alert.text
    # Ждет 1 секунду
    time.sleep(1)
    # Принимает и закрывает alert путем нажатия кнопки "OK" (accept)
    alert.accept()

    # Если alert_text верен, дополнительные сообщения в консоли не должны выводиться.
    # При вызове assert можно добавить дополнительное сообщение через запятую для вывода в случае ошибки
    assert actual_result == expected_result, f"Текст алерта не соответствует ожидаемому. Полученный текст: {actual_result}, Ожидаемый текст: {expected_result}"
    print(f'Полученный текст алерта "{actual_result}" соответствует ожидаемому результату.')


# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`