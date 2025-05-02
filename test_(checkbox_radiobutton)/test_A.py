import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
import math  # Модуль для выполнения математических расчетов
import re  # Модуль для работы с регулярными выражениями


# Ссылка на страницу.
link = 'https://suninjuly.github.io/get_attribute.html'
# Измеряет время выполнения.
start = time.time()
# Функция с математическим выражением вычисляет натуральный логарифм модуля произведения 12 и синуса целочисленного значения x.
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as driver:  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    driver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    assert link == driver.current_url, f'\nОжидаемый   URL: {link}, \nФактический URL: {driver.current_url}'  # Ошибка будет выведена в консоль в случае если URL не совпадают
    print('Url корректный')

    # Находит элемент с идентификатором 'treasure', извлекает его значение из атрибута 'valuex' и вычисляет его с помощью функции calc.
    x = calc(driver.find_element(By.CSS_SELECTOR, "[id='treasure']").get_attribute("valuex"))

    # Находит и заполняет поле ввода текста на веб-странице данными из переменной x.
    input_area = driver.find_element(By.CSS_SELECTOR, "[type='text']").send_keys(x)
    print('Поле ввода дайдено и заполнено')

    # Отмечает чекбокс на веб-странице
    checkbox_button = driver.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    checkbox_button.click()
    if checkbox_button.is_selected():
        print('Чекбокс отмечен')

    # Выбирает радиокнопку на веб-странице
    radio_button = driver.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    radio_button.click()
    if radio_button.is_selected():
        print('Радиокнопка выбрана')

    # Нажимает кнопку отправки формы на веб-странице
    button_submit = driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    time.sleep(1)  # Визуально убеждается, что все действия выполнены

    # Получает alert на веб-странице
    alert = driver.switch_to.alert
    # Сохраняет текст предупреждения (alert) в переменной actual_result
    actual_result = alert.text
    # Выводит числовое значение полученного текста из alert в консоль в качестве ответа
    print(' '.join([f'Ответ {number}' for number in re.findall(r'\d+\.\d+', alert.text)]))
    # Принимает и закрывает alert путем нажатия кнопки "OK" (accept)
    alert.accept()

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")