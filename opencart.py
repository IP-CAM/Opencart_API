import json
import requests
import datetime


# ключ доступа
KEY = ''

SITE_URL = 'сайт/api.php/'

DATA_URLS = {
    'bonus': 'oc_customer_reward'
}

url = SITE_URL + DATA_URLS['bonus']

headers_auth = {
        'Content-Type': 'application/json',
        'key': KEY
    }


# GET запрос для получения информации о бонусах на сайте TDSILA для вызова функции = name()
def bonus_get():
    '''
        В заголовке передаем, что работаем с JSON и ключ сгенерированный в админке
        (Обязательно в админке указать IP адресс с которого будет идти запрос)
    '''
    url_get = requests.get(url, headers=headers_auth)


# POST запрос для отправки данных о бонусах
def bonus_post():
    """
    Данные передаются в JSON

    'customer_reward_id': 5, - идентификатор операции с бонусной картой (Пополнение, списание). Для добавления новой
    операции можно не указывать, тогда система Opencart создаст свой id(int)

    'customer_id': 1, - идентификатор пользователя в системе opencart (int) * важно
    'order_id': 0, - если заказ совершен в интернет магазине, передается id заказа (int) необязательно
    'description': 'Пополнение', - описание операции Пополнение, списание и т.д (str) * важно
    'points': 200, - сумма операции, принимает как положительное так и отрицательное число(example: -200) (int) * важно
    'date_added': '' - Время совершенной операции, если не указать,сортировка будет сбита (str) * важно
    """
    today = datetime.datetime.today()
    data = {
        'customer_reward_id': 5,
        'customer_id': 1,
        'order_id': 0,
        'description': 'Пополнение',
        'points': 200,
        'date_added': f'{ today.strftime("%Y-%m-%d %H:%M:%S") }'
    }
    data_oc = json.dumps(data, ensure_ascii=False).encode('utf8')
    url_post = requests.post(url, headers=headers_auth, data=data_oc)
    
# PUT запрос для обновления данных
def bonus_put():
    """
    Данные передаются в JSON

    В url указываем id транзакции если сделка совершена не верно или информация не точна.

    'customer_id': 1, - идентификатор пользователя в системе Opencart (int) * важно
    'order_id': 0, - если заказ совершен в интернет магазине, передается id заказа (int) необязательно
    'description': 'Пополнение', - описание операции Пополнение, списание и т.д (str) * важно
    'points': 200, - сумма операции, принимает как положительное так и отрицательное число(example: -200) (int) * важно
    'date_added': '' - Время совершенной операции, если не указать,сортировка будет сбита (str) * важно
    """
    today = datetime.datetime.today()
    data = {
        # 'customer_reward_id': 1, не нужно
        'customer_id': 7,
        'order_id': 0,
        'description': 'Обновление бонуса',
        'points': 500,
        'date_added': f'{ today.strftime("%Y-%m-%d %H:%M:%S") }'
    }
    data_oc = json.dumps(data, ensure_ascii=False).encode('utf8')
    url_put = requests.put(url + '/1', headers=headers_auth, data=data_oc)


def bonus_delete():
    """
    В случае если была отправленна ошибочная транзакция в url запросе использовать id операции
    """
    url_delete = requests.delete(url + '/5', headers=headers_auth)
