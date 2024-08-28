import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями
import math # Модуль для выполнения математических расчетов
import re # Модуль для работы с регулярными выражениями

# Ссылка на страницу
link = "http://suninjuly.github.io/explicit_wait2.html"
# Измеряет время выполнения
start = time.time()
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as webdriver:
    # Переходит по ссылке
    webdriver.get(link)
    time.sleep(1)  # Убеждается что открыта искомая страница

    # Ждет появления элемента содержащего текст "$100"
    WebDriverWait(webdriver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))  # Ожидаемый текст
    button_book = webdriver.find_element(By.CSS_SELECTOR, "[id='book']").click()
    # Находит элемент с данными для вычисления в уравнении
    x = calc(webdriver.find_element(By.CSS_SELECTOR, "[id='input_value']").text)

    # Вводит полученый результат с поле ответа и нажимает отправить
    input_area = webdriver.find_element(By.CSS_SELECTOR, "[id='answer']").send_keys(x)
    button_submit = webdriver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    # Ожидает, что модальное окно появится, переключается на него и выводит число из текста в консоль в качестве ответа
    print(' '.join([f'Ответ {number}' for number in re.findall(r'\d+\.\d+', WebDriverWait(webdriver, 60).until(EC.alert_is_present()).text)]))
    webdriver.switch_to.alert.accept()

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")
# Браузер закрывается автоматически после завершения блока `with`
