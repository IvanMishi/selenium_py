# Ожидания явные и неявные

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
python3 test_(waits)/test_A.py
```
## Для вывода результата в отдельный файл зпускает командой 
```sh
python3 test_(waits)/test_A.py >> test_(waits)/output.txt
```
Где test_A.py -  скрипт с тестом, а output.txt - файл, в который будет записан вывод теста.

## Тестовые данные
- [x] Незарегестированный пользователь переходит по ссылке

- [x] закрывает браузер

##  В test_A
Программа использует Ожидание .element_to_be_clickable и title_is 

##  В test_B
Программа использует title_contains

##  В test_C
Программа использует .presence_of_element_located(locator)

##  В test_D
Программа использует .presence_of_all_elements_located

##  В test_E
Программа использует .visibility_of(element)

##  В test_F
Программа использует .invisibility_of_element_located()

##  В test_G
Программа использует .invisibility_of_element_located()

##  В test_H

##  В test_I

##  В test_J

