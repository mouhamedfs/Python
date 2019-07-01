
#pip install zeep


import zeep

wsdl = 'http://192.168.0.100:8080/axis/services/ChatRoom?wsdl'
client = zeep.Client(wsdl=wsdl)
print(client.service.getUsersOnline())


