# Поиск элемента в выпадающем списке с помощью метода send_keys() библиотеки Selenium

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
python3 TEST9/TEST9.py
```
## Для вывода результата в отдельный файл зпускает командой 
```sh
python3 TEST9/TEST9.py >> TEST9/output.txt
```
Где TEST9.py -  скрипт с тестом, а output.txt - файл, в который будет записан вывод теста.


## Тестовые данные
- [x] Незарегестированный пользователь переходит по ссылке http://parsinger.ru/selenium/6/6.html
- [x] Ищет элемент с математическим выражением и получает текст из элемента
- [x] Выбирает в выпадающем списке элемент с текстовым значением, вычисленным из переменной с помощью функции eval()
- [x] Нажимает на кнопку "Submit"
- [x] Закрывает браузер


##  В этой задаче

Программа использует метод text для получения математического выражения из элемента, преобразует его в числа и вычисляет с помощью eval(), которая выполняет строковое выражение как код.
eval() выполняет строку Python-кода как выражение, инструкцию или вызов функции, что обеспечивает гибкость в интерпретации и выполнении кода, представленного в виде строки.

Метод send_keys() позволяет программе взаимодействовать с выпадающим списком на веб-странице, имитируя ввод текста в соответствующее поле. \
Этот метод можно использовать при работе с выпадающим списком для ввода текста в поле поиска или скроллинга по элементам списка выпадающего меню. \
Например, используя send_keys(), можно легче находить и выбирать необходимый элемент из выпадающего списка путем ввода соответствующего текста.
