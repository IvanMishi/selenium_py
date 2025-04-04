# Методы ActionChains
Это способ автоматизации низкоуровневых взаимодействий, таких как движения мыши, действия с кнопками мыши, нажатие клавиш и взаимодействие с контекстным меню. 

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
python3 test_(action_chains)/test_A.py
```
## Для вывода результата в отдельный файл запускает команду
```sh
python3 test_(action_chains)/test_A.py >> test_(action_chains)/output.txt
```
Где test_A.py — скрипт с тестом, а output.txt — файл, в который будет записан вывод теста.




ActionChains — класс, предназначенный для автоматизации сложных последовательностей действий пользователя.
# Import 
from selenium.webdriver.common.action_chains import ActionChains
# Использование ActionChains для выполнения последовательности действий
```actions = ActionChains(browser)``` # Создаём экземпляр класса ActionChains
```action.click(element)``` # Кликает по элементу.
```action.double_click(element)``` # Имитация двойного клика левой кнопки мыши.
```actions.move_to_element(menu)``` # Переместить курсор на элемент меню

```action.click_and_hold(element)``` # Удерживает левую кнопку мыши на элементе.
```action.release(self, on_element=None)```  # Метод release используется для отпускания удерживаемой кнопки мыши на элементе.
```actions.perform()``` # Метод используется для выполнения всех сохраненных операций в экземпляре действия класса ActionChains. Запускает всю цепочку действий. 

```action.pause(seconds)``` # Метод паузы используется для приостановки всех входящих данных на указанное время в секундах. Метод паузы очень важен и полезен в случае выполнения какой-либо команды, для загрузки которой требуется какой-либо JavaScript, или в подобной ситуации, когда между двумя операциями есть временной промежуток.


## Тестовые данные test_A
- [x] Незарегестированный пользователь переходит по ссылке.
- [x] Находит кнопку для двойного клика.
- [x] Выполняет операцию двойного клика по найденному элементу.
#### В программе использует: 
```action.double_click(element)``` # Имитация двойного клика левой кнопки мыши.


## Тестовые данные test_B
- [x] Незарегестированный пользователь переходит по ссылке.
- [x] Нажимает комбинацию клавиш CTRL + ALT + SHIFT + T, чтобы получить секретный пароль.
#### В программе использует: 
```action.key_down(value, element)``` предназначен для отправки нажатия клавиши без её отпускания.
Его следует применять только с клавишами-модификаторами, такими как Control, Alt и Shift. 
Параметр value представляет собой значение клавиши, которую необходимо нажать, и может включать любые клавиши на клавиатуре, например, A, B, C и так далее. 
Параметр element указывает на конкретный элемент на веб-странице, на котором будет выполнено действие. Если он указан, то клавиша будет "нажата" именно на этом элементе.
 ```action.key_up(value, element)``` служит для отпускания ранее нажатой клавиши с помощью метода key_down. 
 Необходимо помнить, что после выполнения действий клавишу следует отпустить. 
 Параметр value соответствует клавише, которую нужно отпустить, и чаще всего это константы из класса Keys, такие как Keys.CONTROL, Keys.ALT или Keys.SHIFT. 
 Параметр element указывает элемент, на котором появится действие отпускания клавиши. Если этот параметр не указан, клавиша будет отпущена на текущем элементе с фокусом.


## Тестовые данные test_C
- [x] Незарегестированный пользователь переходит по ссылке.
- [x] Нажимает комбинацию клавиш CTRL + ALT + SHIFT + T, чтобы получить секретный пароль.
#### В программе использует: 
```action.context_click(element)``` # Используется для выполнения контекстного щелчка (щелчка правой кнопкой мыши) по элементу.
```actions.click(submenu)``` # Кликнуть по подменю