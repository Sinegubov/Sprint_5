# Sprint_5
Финальный проект 5 спринта по курсу AQA Yandex по теме UI-тестирование. Автотесты для сервиса 
[Stellar Burgers](https://stellarburgers.nomoreparties.site/). Это космический фастфуд: можно собрать и заказать бургер 
из необычных ингредиентов.

Проект состоит из файлов:

/tests - Папка с тестовыми классами и методами содержащими UI-проверки. Для тестирования используется фреймворк pytest, 
используется параметризация входных данных
conftest.py - Содержит фикстуры для запуска вебдрайвера и логона с базовой учетной записью
data.py - Файл со статичными данными для тестирования и генератором тестовых данных
locators.py - Сборник используемых локаторов с описанием
Для запуска UI-тестов необходимо установить библиотеки: 

`pip3 install pytest
pip3 install selenium`

Запустить тесты из терминала можно командой:

`pytest -v`