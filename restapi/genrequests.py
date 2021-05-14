import requests
import traceback 
from threading import Thread
from random import randint
import random
import time
import json


def getUrl(method):
    return f'http://localhost:50000/{method}'



def doNewOrder():
    
    """ Метод генерирует звонки """
    count_of_reqs = randint(200, 600)
    while count_of_reqs > 0:
        #print('doNewOrder')
        try:
            new_url = getUrl(method='new')
            new_resp = requests.post(new_url)
            if new_resp.status_code == 200:
                data_new = json.loads(new_resp.text)
                data_check = {'order':data_new.get('order')}
                check_url = getUrl(method='check')
                check_resp = requests.post(url=check_url, json=data_check)
                if check_resp.status_code == 200:
                    data_check = json.loads(check_resp.text)
                    #print(check_resp.text)
                print(f"Зарегистрирована заявка {data_new.get('order')} очередь {data_check.get('position')}")
            else:
                print('Не удалось зарегистрировать заявку')
        except:
            traceback.print_exc()
        count_of_reqs -= 1
        howManySleep = round(random.uniform(0, 1),1)
        print(f'Следующая заявка через {howManySleep} сек.')
        time.sleep(howManySleep)


COUNT_OF_MANAGERS = 3
free_managers = COUNT_OF_MANAGERS
manager_by_order = {}


def initManagers():
    global manager_by_order
    for i in range(COUNT_OF_MANAGERS):
        manager_by_order[i] = None


def getFreeManager():
    for k,v in manager_by_order.items():
        if v is None:
            return k
    return None


def doGetOrder():
    """ Метод обработки звонка """
    
    global manager_by_order
    while True:
        free_manager = getFreeManager()
        #print('doGetOrder', free_manager)
        #manager_by_order[free_manager] = free_manager
        if free_manager is None:
            time.sleep(1)
            continue
        try:
            url = getUrl(method='get')
            resp = requests.post(url)
            order = 0
            if resp.status_code == 200:
                data_get = json.loads(resp.text)
                order = data_get.get('order')
                if order == 0:
                    time.sleep(5)
                    continue
                manager_by_order[free_manager] = order
                print(f"Обрабатывается заявка {order}")
                time.sleep(randint(3, 10))
                print(f"Заявка {order} обработана")
                manager_by_order[free_manager] = None
                url = getUrl(method='del')
                data = {'order': order}
                resp = requests.post(url=url, json=data)
        except:
            traceback.print_exc()
            continue



def main():
    initManagers()
    newOrderListener = Thread(target=doNewOrder)
    getOrderListeners = []
    for _ in range(COUNT_OF_MANAGERS):
        getOrderListener = Thread(target=doGetOrder)
        getOrderListeners.append(getOrderListener)
    
    newOrderListener.start()
    for getOrderListener in getOrderListeners:
        getOrderListener.start()


main()

# def test1():
#     i = 5
#     while i > 0:
#         print('test1')
#         time.sleep(3)
#         i -= 1

# def test2():
#     i = 15
#     while i > 0:
#         print('test2')
#         time.sleep(1)
#         i -= 1

# l1 = Thread(target=test1)
# l3 = Thread(target=test1)
# l2 = Thread(target=test2)
# l1.start()
# l2.start()
# l3.start()

# l1.join()
# l2.join()
# l3.join()