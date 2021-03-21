
class Encode:
    def __encode1(self, data, cipher, protocol):
        encode_data = None
        metainf = int('0000_0000', 2)
        if cipher == 1:
            encode_data = ''.join(
                ord(x) + cipher for x in data
            )
            cipher = int('0000_0100', 2)
        else:
            encode_data = ''.join(format(ord(i), '08b') for i in data)
            cipher = int('0000_0000', 2)

        if protocol.upper() == 'HTTP':
            protocol = int('0000_0001', 2)
        else:
            protocol = int('0000_0000', 2)
        
        assert encode_data is not None, 'encode_data is none'

        encode_data = format(metainf | cipher | protocol, '08b') + encode_data
        return encode_data
    
    
    def get_binary(self, data):
        return int(''.join(format(ord(x), '08b') for x in data), 2)

    """4 уровень, функция application() - отвечает за формат данных, их шифрование
    input функции - данные, которые хотим отправить по сети, протокол данных ('SMTP','HTTP','FTP')
    output: данные + информация про формат данных и шифрование"""
    def application (self, data, protocol):
        ret = self.__encode1(data, 0, protocol)
        return ret

    """ 3 уровень, функция transport() - отвечает за способ передачи данных и их транспортировку
    input: результат работы функции application(), протокол транспортировки данных ('TCP', 'UDP')
    output: данные + информация про транспортировку"""

    def transport(self, data, protocol):
        #metainf = int(data[:8], 2)
        transport_protocol = int('0000_0001', 2)
        data = format(transport_protocol, '08b') + data
        return data

    """ 2 уровень, функция internet() - отвечает за маршрутизацию в сети. Она ищет кому и как доставить данные
    input: результат работы функции transport()
    output: данные + информация про адресата и маршрут доставки"""

    def internet(self, data):
        #metainf = int('00000000_00000000_00000000_00000000', 2)
        ip_mask = ''
        ip = '127.0.0.1'.split('.')
        for i in range(len(ip)):
            #ip_mask = int("{0:08b}".format(int(ip[i])) + '00000000'*(len(ip)-i-1), 2)
            ip_mask = ip_mask + "{0:08b}".format(int(ip[i]))
            #metainf = ip_mask | metainf
        data = ip_mask + data
        return data

    """1 уровень, функция network_interface - отвечает за соединение с сетью
    input: результат работы функции internet(), информация о соединении
    output: кортеж из 2 значений:
        1. данные, преобразованные в бинарный формат
        2. информация о типе соединения (1 - 'Ethernet', 2 -'Wi-Fi', другие числа - "No connection")"""

    def network_interface (self, data, connection):
        if connection == 1:
            connection_name = 'Ethernet'
        elif connection == 2:
            connection_name = 'Wi-Fi'
        else:
            connection_name = 'No connection'

        return data, connection_name
        #return bin(int.from_bytes(bytes=data.encode('utf-8'), byteorder='big')), connection_name
