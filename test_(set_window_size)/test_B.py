from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options_chrome = webdriver.ChromeOptions()
#options_chrome.add_argument('--headless')
# Ссылка на страницу
link = "http://parsinger.ru/window_size/2/index.html"

# Измерение времени выполнения кода
start = time.time()

#Задание значений ширины и высоты окна браузера
window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

with webdriver.Chrome(options=options_chrome) as driver:
    driver.get(link)

    for x in window_size_x:
        for y in window_size_y:
            # Для получения данных о разрешений с размером раб области можно задать значение 500x500 и вычесть разниу
            driver.set_window_size(x,139+y)
            window_size = driver.get_window_size()

            #print(f'{x}x{y} --- {window_size["width"]}x{window_size["height"]}')
            result = driver.find_element('xpath', '//span[@id="result"]').text
            if result:
                print(f'Ответ: {result} в разрешении {{\'width\': {x}, \'height\': {y}}}')

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")