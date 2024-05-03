# Тестировщик устанавливает Python3 в macOS через терминал

## Проверяет установленный python
```sh
$ python3 --version`
```

## Устанавливает python, если требуется

```sh
$ sudo apt-get update && sudo apt-get upgrade
```

```sh
$ sudo apt-get install python3.7
```

После установки открывает окно терминала и создает папку, где будут храниться виртуальные окружения.

```sh
$ mkdir env
```

Переходит в созданную папку.

```sh
$ cd env
```

## Создает виртуального окружения python3:
Виртуальное окружение создает изолированную среду. 
В этом окружении все установленные пакеты и библиотеки, не влияют на другие проекты или саму систему. 
Могут использоваться разные версии пакетов для разных проектов, не конфликтуя между собой. 
Каждый проект работает со своей собственной версией пакетов и библиотек.
При использовании виртуального окружения python вы могут использоваться разные версии одной и той же библиотеки или разные версии python, разделенные разными виртуальными окружениями.

```sh
$ python3 -m venv selenium_env
```

## Активирует виртуальное окружение:

```sh
$ source selenium_env/bin/activate
```

Если окружение активировано, видит в начале командной строки терминала название окружения в круглых скобках. 

## Установка зависимостей:
После создания виртуальной среды,  активирует её и и устанавливает необходимые пакеты с помощью pip, не влияя на глобальную установку Python или другие проекты.

```sh
$ pip install package_name
```

Эта команда устанавливает пакет с именем "package_name" в текущее виртуальное окружение. 
Можно также указать версию пакета или использовать файл requirements.txt для установки всех зависимостей.

## Запуск приложения:

```sh
$ python test_name.py
```

Команда деактивирует текущее виртуальное окружение и возвращает к основному окружению

```sh
deactivate
```

#После перезапуска терминала потребуется снова активировать нужное окружение.
проверка - запустить интепритатор ключевое слово python

### Выходит из интерпретатора

```sh
exit() 
```

(Опция -m в команде python или python3 используется для выполнения модуля как скрипта или запуска модуля с заданным именем.)
Когда вы пишете python -m module_name, Python будет искать модуль с именем "module_name", импортировать его и выполнить его код. Такой подход удобен, когда вам нужно запустить модуль, который находится внутри пакета.
