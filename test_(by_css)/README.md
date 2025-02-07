# Поиск элементов типа чекбокса и радиокнопки с помощью Selenium, включая использование CSS-локаторов и их потомков.

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
python3 test_6(by_css)/test_A.py
```
## Для вывода результата в отдельный файл зпускает командой 
```sh
python3 test_6(by_css)/test_A.py >> test_6(by_css)/output.txt
```
Где test_A.py -  скрипт с тестом, а output.txt - файл, в который будет записан вывод теста.

## Тестовые данные test_A
- [x] Незарегистрированный пользователь переходит по ссылке 
- [x] Ищет цифру-подсказку для вычисления математическим выражением и заполнения поля данными.
- [x] Отмечает 'checkbox'.
- [x] Выбирает радиокнопку 'Robots rule!'.
- [x] Нажимает кнопку 'Submit'.

#### В программе использует CSS локаторы для поиска элеменов:
```div.container div.form-group input.form-control``` Находит элемент <input>, который находится внутри элемента <div class="form-group">, который, в свою очередь, находится внутри элемента <div class="container">.
```div.form-check [type='checkbox']``` Выбирает элементы типа <input>, у которых атрибут type равен checkbox. Эти элементы находятся внутри <div class="form-check">.
```[name='ruler'][value='robots']``` Выбирает элементы, у которых атрибут name равен ruler и атрибут value равен robots.
```form > [type='submit']``` Находит элементы, у которых атрибут type равен submit, и которые являются непосредственными дочерними элементами тега <form>


## Пример использования CSS локатора для поиска элемента 'Второй пост'
Для поиска локатора в chrome использует devtools cmd+f [name='first_name'] или console $$([name='first_name']")
```
<div id="posts" class="post-list">
    <div id="post1" class="item">
        <div class="title">Первый пост</div>
        <img src="./images/image-1.png">
    </div>
    <div id ="post2" class="item">
        <div class="title second">Второй пост</div>
       <div class="title">Второй пост</div>
        <img src="./images/image-2.png">
    </div>
    <div id="post3" class="item">
        <div class="title">Третий пост</div>
        <img src="./images/image-3.png">
    </div>
```
### Использование потомков ```.```
#### ищет в DOM:
```#post2 .title```\
или\
```#post2 .second```\
или\
```#post2 .title.second```\
или \
```div.post-list div.item#post2```\
```div.post-list div.item div.title.second```\
```#``` означает, что надо искать элемент с id post2\
```пробел``` - что также нужно найти элемент-потомок\
```.``` элемент-потомок должен иметь класс со значением title или second или несколько классов записываются подряд через точку

### Использование дочерних элементов ```>```
#### ищет в DOM:
```#post2 > div.title```
или\
```#post2 > div.second```\
div.title или div.second, который находится > строго на один уровень иерархии ниже чем элемент #post2

### Использование порядкового номера дочернего элемента
#### ищет в DOM:
```#posts > .item:nth-child(2) > .title```\
Псевдо-класс :nth-child(2) — позволяет найти второй по порядку элемент среди дочерних элементов для #posts.\
Затем с помощью конструкции > .title мы указываем, что нам нужен элемент .title, родителем которого является найденный ранее элемент .item 