# Поиск элементов с помощью Selenium, использование x-path локаторов

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
python3 test_5(by_xpath)/test_A.py
```
## Для вывода результата в отдельный файл зпускает командой 
```sh
python3 test_5(by_xpath)/test_A.py >> test_5(by_xpath)/output.txt
```
Где TEST_A.py -  скрипт с тестом, а output.txt - файл, в который будет записан вывод теста.

## Тестовые данные test_A
- [x] Незарегестированный пользователь переходит по ссылке .
- [x] Ищет текстовые поля на странице по x-path локатору и  заполняет данными.
- [x] Ищет кнопку 'Submit' по x-path локатору и нажимает на нее.

#### В программе использует x-path локаторы для поиска элеменов:
Для поиска локатора в chrome использует devtools cmd+f //input[@name='first_name'] или console $x("//input[@name='first_name']")
```.find_element(By.XPATH, "//input[@name='first_name']")```    '//' выбор всех потомков элемента от корневого узла. <input> это тег, [ ] фильтрация согласно правилу в скобках, где 'name' - это атрибут, 'first_name' его значение.
```.find_element(By.XPATH, "//input[@name='last_name']")```    '//' выбор всех потомков элемента от корневого узла. <input> это тег, [ ] фильтрация согласно правилу в скобках, где 'name' - это атрибут, 'last_name' его значение.
```.find_element(By.XPATH, "//input[@class='form-control city']")```'//' выбор всех потомков элемента от корневого узла. <input> это тег, [ ] фильтрация согласно правилу в скобках, где 'class' - это атрибут, 'form-control city' его значение.
```.find_element(By.XPATH, "//button[@type='submit']")``` '//' выбор всех потомков элемента от корневого узла. <button> это тег, [ ] фильтрация согласно правилу в скобках, где 'type' - это атрибут, 'submit' его значение.

## Тестовые данные test_B
#### В программе использует:
- [x] Незарегестированный пользователь переходит по ссылке 
- [x] Ищет блоки с текстом.
- [x] Получает текст из первого и третьего элемента внутри блока.
- [x] Выводит полученый текст в консоль
#### В программе использует:
XPATH позволяет точно указать, какие элементы вы хотите найти, что очень удобно при работе с динамическими страницами.
```.find_elements(By.XPATH, "//div[@class='text']")``` Находит все элементы <div> с классом "text"
При итерации по элементам внутри списка:
```div.find_element(By.XPATH, './p[1]')``` Получает первый тег <p> в найденом элементе <div>
```div.find_element(By.XPATH, './p[3]')``` Получает третий тег <p> в найденом элементе <div>


## Пример использования x-path локатора для поиска элемента 'Второй пост'
```
<html>
<head>
    <title>Мои посты</title>
</head>
<body>
    <div id="posts" class="post-list">
        <div id="post1" class="item">
            <div class="title">Первый пост</div>
            <img src="./images/summer.png">
        </div>
        <div id="post2" class="item">
            <div class="title second">Второй пост</div>
            <div class="title">Второй пост</div>
            <img src="./images/summer.png">
        </div>
        <div id="post3" class="item">
            <div class="title">Третий пост</div>
            <img src="./images/summer.png">
        </div>
    </div>
</body>
</html>
```
#### Символ '/' выбирает прямых потомков div от /html ищет первого потомка body.
```.find_element(By.XPATH, "/html/body/div/div")``` \
Находит 3 элемента div id="post1", div id="post2", div id="post3" 

#### Символ '//' выбирает потомка от корневого /html любой вложенности, поиск будет по всему дереву DOM.
```.find_elements(By.XPATH, "/html/body/div//div")``` \
Находит 6 элементов div id="post1", div class="title", div id="post2", div class="title", div id="post3", div class="title"

#### Символ [ ] — фильтрация для выбора элементов. 
```.find_element(By.XPATH, "/html/body/div/div[@id='post2']")``` \
При наличии нескольких элементов будет произведена фильтрация согласно правилу в скобках.

#### Поиск по любому атрибуту
```.find_element(By.XPATH, "div[@id='post2']")``` \
Находит элемент по атрибуту, будь то id, class, title или любой другой. 

#### Поиск по порядковому номеру. 
```.find_element(By.XPATH, "div[@class='post-list']/div[2]")``` \
Находит элемент с классом "post-list" и вернет его второго потомка.

#### Поиск по полному совпадению текста.
```.find_element(By.XPATH, "//div[text()='Второй пост']")``` \
Находит элемент, только если текст полностью совпадет.

#### Поиск по частичному совпадению текста или атрибута.
```.find_element(By.XPATH, "//div[contains(text(), 'Второй')]")``` \
Функция contains вернет все абзацы текста, которые содержат слово 'Второй'.

```.find_element(By.XPATH, "/div[contains(@id, 'pos')]")``` \
Функция contains вернет все абзацы текста, по частичному совпадению других атрибутов @id или @class.

#### Поиск с использованием булевых операции and, or, not
```.find_element(By.XPATH, "//div[@id='post2' and @class='item']")``` \
Находит элемент, по @id и @class




