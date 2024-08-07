# Поиск элемента по тексту в ссылке с помощью Selenium

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
python3 test_4(find_elements)/test_A.py
```
## Для вывода результата в отдельный файл зпускает командой 
```sh
python3 test_4(find_elements)/test_A.py >> test_4(find_elements)/output.txt
```
Где test_A.py -  скрипт с тестом, а output.txt - файл, в который будет записан вывод теста.

## Тестовые данные
- [x] незарегистрированный пользователь переходит по ссылке http://suninjuly.github.io/find_link_text
- [x] использует переменную с математическим выражением для поиска элемента по подстроке
- [x] кликает по этому элементу и переходит по ссылке на страницу с регистрационной формой
- [x] заполняет формы данными и нажимает  кнопку submit
- [x] закрывает браузер

## В задаче test_A
Программа ищет элементы по тексту ссылки, используя метод `find_element_by_link_text`. \
В ходе теста программа формирует математическое выражение `str(math.ceil(math.pow(math.pi, math.e) * 10000))`. \
Результат вычисления этого выражения преобразуется в строку и сохраняется в переменной `m = '224592'` \
Далее программа использует переременную `m` для поиска ссылки, ведущей на страницу регистрации пользователя. \
Для этого применяется метод `find_element()`, где в качестве метода поиска указывается `LINK_TEXT`, а в качестве аргумента передается переменная `m` содержащая текст ссылки, который необходимо найти.\
Текст данной ссылки на странице находится между открывающим и закрывающим тегами `<a>224592</a>` в структуре DOM страницы.

Ищет элемент по полному тексту ссылки
```sh
link = browser.find_element(By.LINK_TEXT, 'some text')
```

## В задаче test_B

Ищет элемент по подстроке в тексте ссылки
```sh
link = browser.find_element(By.PARTIAL_LINK_TEXT, 'text').click()
```

