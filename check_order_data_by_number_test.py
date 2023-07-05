import sender_stand_request
import data


# Керимова Яна, 6-я когорта — Финальный проект. Инженер по тестированию плюс

def get_new_order_token():
    order_token = sender_stand_request.post_new_order(data.order_body)
    return str(order_token.json()["track"])


# Тест 1. Код 200 на запрос получения заказа по треку заказа

def test_order_data_response_code():
    order_token = get_new_order_token()
    order_response = sender_stand_request.get_order_by_track(order_token)
    assert order_response.status_code == 200
