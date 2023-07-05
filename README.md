# Работа с базой данных:

# Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
# Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 
# SQL

`SELECT c.login,
       COUNT(o.id) AS orders_count
FROM "Couriers" AS c
INNER JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery" = TRUE
GROUP BY c.login;`

# Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
# Для этого: выведи все трекеры заказов и их статусы.Статусы определяются по следующему правилу:
# Если поле finished == true, то вывести статус 
# Если поле canсelled == true, то вывести статус -1.
# Если поле inDelivery == true, то вывести статус 1.
# Для остальных случаев вывести 0.
# SQL

SELECT track,
	CASE
	WHEN finished = true THEN 2
	WHEN cancelled = true THEN -1
	WHEN “inDelivery” = true THEN 1
	ELSE 0
	END AS status
FROM "Orders";


# Тесты на проверку создание заказа, получения трек номера и кода ответа.
# Для запуска тестов должны быть установлены пакеты pytest и requests
pip install pytest
pip install requests

## Содержимое проекта

* configuration.py - находятся две переменные:
   - URL_SERVICE: содержит URL-адрес сервиса, к которому нужно отправлять запросы.
   - CREATE_ORDER: содержит часть URL-адреса для создания нового заказа.
   - GET_ORDER: содержит часть URL-адреса для получения информации о заказе по его треку.
* data.py - находятся две переменные:
   - order_body: содержит данные о заказе, которые будут отправлены при создании нового заказа.
   - headers: содержит заголовки для запросов.
* sender_stand_request.py - находятся две функции:
   - post_new_order(order_body): отправляет POST-запрос для создания нового заказа с указанными данными.
   - get_order_by_track(order_token): отправляет GET-запрос для получения информации о заказе по его треку.
* check_order_data_by_number_test.py - находится тестовая функция:
   - get_new_order_token(): создает новый заказ и возвращает его трек.
   - test_order_data_responce_code(): отправляет GET-запрос для получения информации о заказе по его треку и проверяет,
  что код ответа равен 200.
* README.md - файл с описанием проекта и инструкцией для запуска тестов, а так же с SQL запросами 
* .gitignore - файл со списком файлов и каталогов, которые не должны попадать в репозиторий
