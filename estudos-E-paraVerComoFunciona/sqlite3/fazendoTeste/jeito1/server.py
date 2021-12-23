from opcua import Server
import PegandoVariavel as v
import time
server = Server()

url = 'opc.tcp://localhost:4840' 

server.set_endpoint(url)

name = 'OPCUA_SIMULATION_SERVER'
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object(addspace, "Parameters")
Dados = Param.add_variable(addspace, 'Dados', 0)
Dados.set_writable()


# começando servidor
server.start()


while True:
    
    for tuplas in v.get_Pessoas():
        
        # Dados.set_value(tuplas)
        print('tupla:', map(dict, tuplas))
        # print('tipo:', type(tuplas))
    
        time.sleep(1)
