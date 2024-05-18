# импортирует необходимые библиотеки
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# открывает браузер Chrome
driver = webdriver.Chrome()

# ждет 5 секунд
time.sleep(5)

# переходит по ссылке, метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://suninjuly.github.io/text_input_task.html")

# ждет 5 секунд
time.sleep(5)

# находит поле для ввода текста, метод find_element позволяет найти нужный элемент на сайте, указав путь к нему
textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

# вводим текст "get()" в поле textarea
textarea.send_keys("get()")
# ждет 5 секунд
time.sleep(5)

# находит кнопку отправки формы 
submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")
# кликает на кнопку отправки формы 
submit_button.click()
# ждет 5 секунд
time.sleep(5)

# закрывает окно браузера после выполнения всех действий
driver.quit()