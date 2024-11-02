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

С помощью метода ```.get_cookies()``` можно получить как имена куков, так и их значения.\
Метод .get_cookies() возвращает список словарей, содержащих информацию, включая время истечения срока жизни cookie ('expiry': 1685518907).\
```
[{'domain': '.ya.ru',
  'expiry': 1685518907,
  'httpOnly': False,
  'name': '_ym_d',
  'path': '/',
  'sameSite': 'None',
  'secure': True,
  'value': '1653982908'},
  ...
   {'domain': '.ya.ru',
  'expiry': 1656574906,
  'httpOnly': False,
  'name': 'yandex_gid',
  'path': '/',
  'sameSite': 'None',
  'secure': True,
  'value': '239'}]
```
```.get_cookie(name_cookie)```
находит и возвращает cookie по его имени.\
```for cookie in cookies:```\
```        print(cookie['name'])``` # или cookie['value'] чтобы получить их значение

Пример кода для извлечения конкретного значения из cookie.\
```print(webdriver.get_cookie('_ym_uid')['expiry'])```

## Тестовые данные test_A

#### В программе использует: 
