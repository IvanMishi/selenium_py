Установка Python3 в macOS через терминал

# Проверка установленного python
$ python3 --version


#Установить python
$ sudo apt-get update && sudo apt-get upgrade
$ sudo apt-get install python3.7


#После установки откройте окно терминала и создайте папку, где будут храниться наши виртуальные окружения, затем перейдите в созданную папку:
$ mkdir env
$ cd env

#Создание виртуального окружения python3:
#Виртуальное окружение создает изолированную среду. 
#Это означает, что все пакеты и библиотеки, которые вы устанавливаете в этом окружении, не будут влиять на другие проекты или саму систему. 
#Это очень удобно, потому что вы можете использовать разные версии пакетов для разных проектов, и они не будут конфликтовать между собой. 
#Таким образом, каждый проект будет работать со своей собственной версией пакетов и библиотек.
#При использовании виртуального окружения python вы можете использовать разные версии одной и той же библиотеки или разные версии python, разделенные разными виртуальными окружениями
$ python3 -m venv selenium_env

Активация виртуального окружения:
$ source selenium_env/bin/activate

#Если окружение активировано, то мы увидим в начале командной строки терминала название окружения в круглых скобках. 
#Теперь мы можем устанавливать нужные нам пакеты и запускать скрипты для тестов, которые мы напишем:

#Установка зависимостей:
#После создания виртуальной среды, вы можете активировать её и устанавливать необходимые пакеты с помощью pip, не влияя на глобальную установку Python или другие проекты.

$ pip install package_name
#Эта команда устанавливает пакет с именем "package_name" в текущее виртуальное окружение. 
#Можно также указать версию пакета или использовать файл requirements.txt для установки всех зависимостей.

#Запуск приложения:
$ python test_name.py



#Эта команда деактивирует текущее виртуальное окружение и возвращает вас к основному окружению
deactivate

#Обратите внимание, что после перезапуска терминала нужно будет снова активировать нужное окружение.
#проверка - запустить интепритатор ключевое слово python
exit() #- выйти из интерпретатора


#(Опция -m в команде python или python3 используется для выполнения модуля как скрипта или запуска модуля с заданным именем.)
#Когда вы пишете python -m module_name, Python будет искать модуль с именем "module_name", импортировать его и выполнить его код. Такой подход удобен, когда вам нужно запустить модуль, который находится внутри пакета.
