# Работа с cookies

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
python3 test_(cookies)/test_A.py
```
## Для вывода результата в отдельный файл зпускает командой 
```sh
python3 test_(cookies)/test_A.py >> test_(cookies)/output.txt
```
Где test_A.py -  скрипт с тестом, а output.txt - файл, в который будет записан вывод теста.

### Куки
Куки (cookie) — это мелкие фрагменты данных, отправляемые веб-сервером и хранящиеся на компьютере пользователя.\
**Сессионные куки:** Хранят информацию на короткий срок, включая записи форм и время пребывания на сайте. Удаляются при уходе с сайта.\
**Постоянные куки:** Сохраняются в браузере длительное время и могут включать логин и данные учетной записи, такие как местоположение в Google.\
Куки передаются между клиентом и сервером через заголовки HTTP


#### Добавление куки в текущую сессию браузера:
При работе с Selenium  не всегда возможно использовать один профиль браузера для нескольких скриптов.\
В таких случаях можно создать дополнительные профили или использовать одни и те же cookies для всех скриптов.\
```webdriver.add_cookie(cookie)```  
```webdriver.refresh()``` # После добавления куки следует обновить страницу\
Мы не можем передать в cookie любые данные. \
В браузере существуют заранее определенные поля, в которые можно записывать информацию.\
##### Добавляет файл cookie в текущий контекст браузера.\
```webdriver.add_cookie({"name": "key", "value": "value"})```

#### Получить  имена куки или их значения.\
Метод cookies = webdriver.get_cookies() получает список словарей, содержащих информацию, включая время истечения срока действия cookie ('expiry': 1685518907).\
```pprint(cookies)``` для "понятной печати" структур данных, таких как словари и списки.
```
[{'domain': '.ya.ru',
  'expiry': 1685518907,
  'httpOnly': False,
  'name': '_ym_d',
  'path': '/',
  'sameSite': 'None',
  'secure': True,
  'value': '1653982908'}]
```

#### Метод .get_cookie(name_cookie) находит и возвращает cookie по его имени.
```for cookie in cookies:```\
```        print(cookie['name'])``` # или cookie['value'] чтобы получить их значение
Пример кода для извлечения конкретного значения из cookie.\
```print(webdriver.get_cookie('_ym_uid')['expiry'])```

#### Удаление  куки из сессии:
```webdriver.delete_cookie(name_cookie)``` # Удаляет cookie по имени\
```webdriver.delete_all_cookies()``` # Удаляет все файлы cookie в рамках текущего сеанса\
```webdriver.refresh()``` # После удаления куки следует обновить страницу

## Тестовые данные test_A
- [x] Незарегестированный пользователь переходит по ссылке.
- [x] Получает все куки и сохраняет в переменную.
- [x] Извлекает значения куки с именами, содержащими 'secret_cookie_'.
- [x] Преобразует полученные значения в числа, суммирует их и выводит общую сумму в консоль.
#### В программе использует: 
```webdriver.get_cookies()```\
```if 'secret_cookie_' in cookie['name']:```

## Тестовые данные test_B
- [x] Незарегестированный пользователь переходит по ссылке.
- [x] Добавляет поочередно куки из файла в виде словаря.
- [x] После добавления куки и обновления страницы сохраняются появившиеся данные о возрасте и количестве навыков пользователя.
- [x] Находит пользователя с наименьшим возрастом и наибольшим количеством навыков.
#### В программе использует: 
```webdriver.add_cookie(cookie)``` # Добавляет куки в текущую сессию браузера
```for skill in webdriver.get_cookies():``` # Извлекает все куки, доступные на странице
```            val_cookie = skill['value']```  # Берет последнее значение куки
```candidat_find = max(result, key=lambda x: (-x[0], x[1]))```
max():
result — это коллекция кандидатов, где каждый кандидат представлен в виде кортежа или списка, содержащего, возраст и количество навыков.\
key — это лямбда-функция, которая определяет критерии для вычисления максимального значения.\
Лямбда-функция:\
(-x[0], x[1]) — мы берём отрицательное значение возраста, чтобы сначала искать по максимальному возрасту (поскольку мы работаем с отрицательным величиной, max() будет искать по убыванию), а затем, если есть совпадения по возрасту, по количеству навыков в обычном порядке (по возрастанию).

## Тестовые данные test_C
- [x] Незарегестированный пользователь переходит по ссылке
- [x] Собирает данные о жизни куки в каждой найденной ссылке на странице
- [x] Ищет куки с самым долгим сроком жизни и выводит в качестве ответа число из тега <p id="result">INT</p> на странице этого куки
#### В программе использует: 
Для перехода по сслыка на странице использует цикл for:
```for link in links:```
```    webdriver.back``` # для возврата на исходную страницу
 Находит самое большое значение куки 'expiry' из собранной информации
 Используется функция max, чтобы получить максимальное значение ключей словаря 
 'expiry_to_int_mapping', представляющих значения 'expiry' куки.
  Если словарь пуст (т.е. нет значений 'expiry'), параметр default=None гарантирует, что переменной max_expiry_value будет присвоено значение None вместо ошибки.
```max_expiry_value = max(expiry_to_int_mapping.keys(), default=None)```

## Тестовые данные test_D
- [x] Незарегестированный пользователь переходит по ссылке
- [x] Собирает данные о куки с четным числовым значением 
- [x] Суммирует полученные данные и вывоит в качестве ответа
#### В программе использует: 
Функция filter() получает функцию и итерируемый объект. Здесь используется str.isdigit, которая проверяет, является ли символ цифрой. 
Строка cookie['name'] — это итерируемый объект. filter оставляет только цифры, для которых str.isdigit возвращает True.
Функция filter() возвращает итератор с числовыми символами. Метод ''.join() объединяет их в одну строку без добавления дополнительных символов между ними.
```digit = ''.join(filter(str.isdigit, cookie['name']))```
Условие при котором значения куки можно считать четным числом
```if int(digit) %2 ==0:```