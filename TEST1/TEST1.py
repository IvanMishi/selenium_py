
#импортирует модуль time для работы с ожиданием
import time 
# импортирует модуль webdriver из библиотеки selenium для взаимодействия с веб-браузером
from selenium import webdriver 
# импортирует модуль By из библиотеки selenium.webdriver.common для использования способа поиска элементов на странице
from selenium.webdriver.common.by import By


# Переменная expected_result содержит ожидаемый текст результата, который участник тестового сценария ожидает увидеть после успешного завершения
expected_result = "Thank you for submitting the form!"


# открывает браузер Chrome
driver = webdriver.Chrome()

# ждет 2 секунды
time.sleep(2)

# переходит по ссылке, метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://suninjuly.github.io/text_input_task.html")

# ждет 2 секунды
time.sleep(2)

# Находит поле для ввода текста на веб-странице
# Метод find_element находит элемент на сайте по заданным параметрам, "class name" и "textarea" параметры для поиска конкретного элемента на странице.
# Когда этот метод будет выполнен, будет возвращен объект, который представляет найденный элемент на веб-странице.
textarea = driver.find_element("class name", "textarea")

# вводит текст в поле textarea
textarea.send_keys("пользовательский текст")
# ждет 2 секунды
time.sleep(2)

# находит кнопку отправки формы на веб-странице, используя уникальный идентификатор "submit_button"
submit_button = driver.find_element("id", "submit_button") 
# нажимает на кнопку отправки формы 
submit_button.click()


# Убеждается, что текст всплывающего окна (alert) соответствует ожидаемому результату. Если текст в алерте не совпадает с ожидаемым текстом, будет выведено сообщение об ошибке.
# получает alert на веб-странице
alert = driver.switch_to.alert
# сохраняет текст предупреждения (alert) в переменной actual_result
actual_result = alert.text
# ждет 2 секунды
time.sleep(2)
# принимает и закрывает alert путем нажатия кнопки "OK" (accept)
alert.accept()


# Если alert_text верен, дополнительные сообщения в консоли не должны выводиться.
# При вызове assert можно добавить дополнительное сообщение через запятую для вывода в случае ошибки
assert actual_result == expected_result, f"Текст алерта не соответствует ожидаемому. Полученный текст: {actual_result}, Ожидаемый текст: {expected_result}" 
print(f'Полученный текст алерта "{actual_result}" соответствует ожидаемому результату.')

# закрывает браузер
driver.quit()