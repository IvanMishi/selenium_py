# Инстукция по запуску тестов

Инженер по тестированию проверяет установленный python
```sh
python3 --version
```

Устанавливает python, если требуется

После установки открывает окно терминала и создает директорию, предназначенную для хранения файлов с тестами
```sh
mkdir selenium_tests
```
В  директоии selenium_tests создает папку, где будут храниться виртуальные окружения.

```sh
mkdir selenium_env
```

Переходит в созданную директорию.

```sh
cd selenium_env
```

## Создает виртуальное окружения python3:
Виртуальное окружение обеспечивает изоляцию среды: установленные пакеты и библиотеки не влияют на другие проекты или систему.\
Различные проекты могут использовать разные версии пакетов без конфликтов.
Каждый проект имеет свою собственную версию пакетов и библиотек, позволяя использовать разные версии библиотек или Python в разных виртуальных окружениях.

```sh
python3 -m venv selenium_env
```

## Активирует виртуальное окружение:

Из директории selenium_tests выполняет команду.
```sh
source selenium_env/bin/activate
```

Если окружение активировано, видит в начале командной строки терминала название окружения в круглых скобках. 
```(selenium_env)```

## Устанавливает зависимости:
После создания виртуальной среды,  активирует её и и устанавливает необходимые пакеты с помощью pip, не влияя на глобальную установку Python или другие проекты.


Можно также  использовать файл requirements.txt для установки всех зависимостей, вактивированном окружении выполняет команду.

```pip install -r requirements.txt```
Файл requirements.txt добавлен в проект

Обновляет pip, если требуется

```sh
python3 -m pip install --upgrade pip
```

Устанавливает библиотеку Selenium
```sh
pip install -U selenium
```


Устанавливает драйвер для браузера
```sh
pip install webdriver-manager
```


## Запускает приложение:
Из директории selenium_env в активированном окружении запускает тест
```sh
python3 test_name.py
```

Деактивирует текущее виртуальное окружение, если требуется вернутся к основному окружению
```sh
deactivate
```

После перезапуска терминала потребуется снова активировать нужное окружение.
