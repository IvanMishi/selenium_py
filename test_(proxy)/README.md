# Основные методы Selenium

## Инженер по тестированию переходит в директорию, предназначенную для хранения файлов с тестами
```
cd selenium_tests
```
## Из директории selenium_tests активирует виртуальное окружение
```sh
source selenium_env/bin/activate
```
## В активированном окружении запускает тест 
```sh
python3  test_(methods)/test_A.py
```
## Для вывода результата в отдельный файл зпускает командой 
```sh
python3 test_(methods)/test_A.py >> test_A2/output.txt
```
Где test_A.py -  скрипт с тестом, а output.txt - файл, в который будет записан вывод теста.




Узнат свой ip через терминал ```curl ifconfig.me```
Узнать свой IP на сайте
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
url = 'https://2ip.ru/'
with webdriver.Chrome() as webdriver:
    webdriver.get(url)
    time.sleep(5)
    print(webdriver.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)

