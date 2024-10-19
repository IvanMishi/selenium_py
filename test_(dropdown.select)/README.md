# Поиск элемента в выпадающем списке с помощью метода select_by_value() из библиотеки Selenium

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
python3 test_8(select_by_value)/test_A.py
```
## Для вывода результата в отдельный файл зпускает командой 
```sh
python3 test_8(select_by_value)/test_A.py >> test_8(select_by_value)/output.txt
```
Где test_A.py -  скрипт с тестом, а output.txt - файл, в который будет записан вывод теста.

## Тестовые данные test_A
- [x] Незарегестированный пользователь переходит по ссылке
- [x] Получает текст из элементов с числами на странице.
- [x] Складывает значения и сохраняет результат.
- [x] Выбирает в выпадающем списке элемент, равный сумме чисел.
- [x] Нажимает на кнопку "Submit".
#### В программе использует:
метода select_by_value() из библиотеки Selenium WebDriver который используется для работы с выпадающими списками (dropdown) на веб-странице. \
```from selenium.webdriver.support.ui import Select``` Импортирует модуль Select который позволяет управлять выпадающими списками на веб-страницах
Когда на веб-странице есть элемент <select> (выпадающий список) с дочерними элементами <option>, у каждого из которых есть атрибут value, \
метод select_by_value() позволяет выбрать опцию из выпадающего списка, основываясь на значении value атрибута элемента <option>.

Пример:
```<label for="dropdown">Выберите элемент из выпадающего списка:</label>```
<select id="dropdown" class="custom-select">
 <option selected>--</option>
 <option value="1">Элемент 1</option>
 <option value="2">Элемент 2</option>
 <option value="3">Элемент 3</option>
</select>
Выбирает элемент с значением 1\
```.select_by_value("1")```\
Выбирает элемент с значением 2\
select.select_by_visible_text("Элемент 2")\
Выбирает элемент с значением 3 по индексу, индексация начинается с нуля. \
```.select_by_index(2)```