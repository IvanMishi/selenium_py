# Основные методы Selenium

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
python3  test_(methods)/test_A.py
```
## Для вывода результата в отдельный файл зпускает командой 
```sh
python3 test_(methods)/test_A.py >> test_A2/output.txt
```
Где test_A.py -  скрипт с тестом, а output.txt - файл, в который будет записан вывод теста.




## Тестовые данные test_A
Узнат свой ip через терминал ```curl ifconfig.me```
Узнать свой IP на сайте


## Тестовые данные test_B
Код модифицируется для отправки запроса через прокси, который должен иметь формат IP:PORT.
В начале был передан параметр --proxy-server=%s' % proxy методу .add_argument() в класс дополнительных опций .ChromeOptions(), указывая прокси из переменной proxy.
Если прокси активен, его можно протестировать в IDE.
В противном случае, следует приобрести надежный прокси и запустить код с ним. (proxy6.net)  


## Тестовые данные test_C
В процессе работы с прокси-сервером для загрузки страниц используется таймаут, задаваемый с помощью параметра ```timeout=```. 
При истечении этого времени происходит либо закрытие окна, либо переход к следующему прокси из списка ```proxy_list```. 
Скрипт итерирует через этот список, передавая на каждой итерации новый IP в переменную ```PROXY```.
Чтобы избежать падения скрипта из-за ошибок, таких как ```Message: unknown error: net::ERR_TUNNEL_CONNECTION_FAILED```, 
когда время ожидания истекает или прокси настроен неправильно, код обернут в конструкцию try/except. 
Это позволяет продолжать выполнение работы даже при возникновении исключений.
Таймаут в Selenium устанавливается методом ```.set_page_load_timeout(5)```, где число 5 обозначает количество секунд ожидания загрузки страницы. 
Если страница не загружается в течение этого времени, выбрасывается исключение ```TimeoutException```. 
После этого браузер перезапускается с новыми настройками прокси для каждой новой попытки запроса.


## Тестовые данные test_D
Для настройки прокси с авторизацией необходимо установить расширение selenium-wire. Это делается с помощью команды:
```pip install selenium-wire```
Импортировать модуль можно так:
from seleniumwire import webdriver
Структура кода почти не изменилась: 
вместо использования options=options теперь применяют seleniumwire_options=options, 
где в словаре options содержится информация о прокси с авторизацией. 
При этом не требуется использовать метод .add_argument('--proxy-server=%s' % PROXY).
Когда покупают прокси, они могут предлагать два типа авторизации: по логину и паролю или по IP-адресу. 
В случае использования динамического IP, который меняется при перезагрузке ПК или роутера, 
предпочтительнее выбирать авторизацию по логину и паролю. 
Если IP статический, лучше использовать авторизацию по IP.``