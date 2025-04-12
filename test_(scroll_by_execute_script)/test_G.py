import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице




# Ссылка на страницу
link = "https://parsinger.ru/selenium/7/7.5/index.html"
# Измеряет время выполнения определенного участка кода.
start = time.time()

with (webdriver.Chrome() as driver):  # Создаёт экземпляр драйвера Chrome и автоматически закрывает его по завершении блока кода.
    driver.get(link)  # Переходит по ссылке.
    time.sleep(1)  # Убеждается что открыта искомая страница.
    assert link == driver.current_url, f'\nОжидаемый   URL: {link}, \nФактический URL: {driver.current_url}'  # Ошибка будет выведена в консоль в случае если URL не совпадают

    total = 0  # Общая сумма значений после клика на кнопку.
    list_button = []  # Создает пустой список для хранения нажатых.

    while True:  # Начинает бесконечный цикл для постоянной обработки кнопок.
        button_like = [x for x in driver.find_elements(By.CLASS_NAME,'like-btn')]  # Находит все кнопки на странице.
        numbers = [x for x in driver.find_elements(By.CLASS_NAME,'big-number')]  # Находит элементы с связанными числовыми значениями.
        new_buttons_found = False  # Флаг, указывает, были ли найдены новые кнопки за итерацию.

        # Проходит по всем найденным кнопкам и соответствующим им значениям.
        for button, number in zip(button_like, numbers):
            if button not in list_button:  # Проверяет, была ли текущая кнопка уже обработана.
                driver.execute_script("return arguments[0].scrollIntoView(true);",button)  # Скроллит страницу до кнопки.
                button.click()  # Нажимаем на кнопку.
                total += int(number.text)  # Инкримент связаных числовых значений после нажатия кнопки.
                list_button.append(button)  # Добавляет кнопку в список обработанных, чтобы избежать повторного нажатия.
                new_buttons_found = True  # Обновляет флаг, так как нашли новую кнопку.
                time.sleep(0.01)

        # Проверяет, были ли найдены новые кнопки, если нет, то завершаем цикл.
        if not new_buttons_found:  # Если флаг new_buttons_found остается False, значит, новые кнопки не найдены.
            break  # Выходим из бесконечного цикла.

        time.sleep(0.1)  # Делает паузу перед следующей итерацией цикла.

    # Выводит итог полученной суммы total в качестве ответа.
    print(f"Ответ: {total}")

# Завершение отсчета времени
end = time.time()
print(f"Время выполнения: {end - start} секунд.")