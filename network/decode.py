
class Decode:
    def decode_binary_string(self, s):
        return ''.join(chr(\
                int(\
                    s[i*8:i*8+8], 2\
                )\
            ) for i in range(len(s) // 8))

    '''1 уровень, функция network_interface - отвечает за соединение с сетью
    передаём в функцию 2 аргумента:
        1 аргумент, data - это данные в виде бинарного числа
        2 аргумент, connection - это тип соединения (1 - 'Ethernet', 2 -'Wi-Fi', другие числа - "No connection")
    возвращаем:
        - если удалось установить соединение - то кортеж из 2 значений: данные в виде строки из нулей и единиц и тип соединения
        - если не удалось установить соединение, то строку "No connection"'''

    def network_interface(self, data, connection):
        if 0 < connection < 2:
            return str(data), connection
         
        return None, 'No connection'


    ''' 2 уровень, функция internet() - отвечает за маршрутизацию в сети. Она ищет кому и как доставить данные
    передаём в функцию результат работы функции  network_interface()
    возвращаем данные в виде строки, если данные переданы в кортеже и адресованы нам, иначе - передаём None'''

    def internet(self, data):
        ip = data[0][:4*8]
        # Если ip == нашему, то работаем дальше
        # иначе возвращаем None
        return data[0][4*8:]

    ''' 3 уровень, функция transport() - отвечает за способ передачи данных и их транспортировку
    передаём в функцию результат работы функции internet()
    возвращаем:
    - если c предыдущего уровня получены данные, то формируем кортеж из 2 значений: данные, протокол передачи
    - None - если данные не получены'''

    def transport(self, data):
        transport_protocol = int(data[:8], 2)
        if transport_protocol == 1:
            transport_protocol = 'TCP'
        elif transport_protocol == 2:
            transport_protocol = 'UDP'
        return data[8:], transport_protocol

    ''' 4 уровень, функция application() - отвечает за формат данных, их расшифровку
    передаём в функцию результат работы функции transport()
    возвращаем:  '''

    def application (self, data):
        cipher = data[0][:8]
        print(data[0][8:])
        return self.decode_binary_string(data[0][8:])
