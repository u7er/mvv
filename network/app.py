import encode
import decode


print("{0:08b}".format(127))


a = encode.Encode()
encode_data = (a.network_interface(a.internet(a.transport(a.application('text', 'HTTP'), 'TCP')), 1))

ten_base = int(encode_data[0], base=2)

print(ten_base)

b = decode.Decode()
data_from_network = b.network_interface (encode_data[0],1)
print ('network_interface level - ', data_from_network, len(data_from_network[0]))
data_ip = b.internet(data_from_network)
print ('internet level - ', data_ip, len(data_ip))
data_transport = b.transport (data_ip)
print ('transport level - ', data_transport, len(data_transport[0]))
data_app = b.application(data_transport)
print ('application level - ', data_app)
