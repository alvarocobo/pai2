#!/usr/bin/env python
#Se importa el módulo
import auxiliar
import json
import ast
import socket
import ssl
#instanciamos un objeto para trabajar con el socket
ser = socket.socket()
 
#Puerto y servidor que debe escuchar
ser.bind(("", 8000))
 
#Aceptamos conexiones entrantes con el metodo listen. Por parámetro las conexiones simutáneas.
ser.listen(5)

#------------

total = 0
integros = 0

#-------


while True:
    try:
        #Instanciamos un objeto cli (socket cliente) para recibir datos
        print("Esperando conexiones de clientes...\n")
        
        cli,addr = ser.accept()

        connstream = ssl.wrap_socket(cli, server_side=True,
                                 certfile="server.crt",
                                 keyfile="server.key", ssl_version=ssl.PROTOCOL_TLSv1_2
                                 )
        #ciphers = "ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:AES128-GCM-SHA256:AES128-SHA256:HIGH:"

        print("connection accepted from " + str(addr[0]) + ":" + str(addr[1]) +  ". Processing the request")
        try:
            usuario = connstream.read().decode()
            print("usuario: ", usuario)
            contraseña = connstream.read().decode()
            print("Contraseña: ", contraseña)
            mensaje = connstream.read().decode("ISO-8859-1")
            if auxiliar.coincidencia("dic.json",usuario,contraseña):
                respuesta = "Mensaje recibido. " + "Su mensaje fue: " + mensaje
                connstream.write(respuesta.encode())
                auxiliar.almacen("almacen.json", usuario, mensaje)
                print(respuesta)
            else:
                respuesta = "El mensaje no se ha almacenado."
                connstream.write(respuesta.encode())
                print(respuesta)

        finally:
            connstream.shutdown(socket.SHUT_RDWR)
            connstream.close()
        #try:
        #    deal_with_client(connstream)
        #    connstream.send("Hola".encode())
        #finally:
        #    connstream.shutdown(socket.SHUT_RDWR)
        #    connstream.close()

        #mensaje = cli.recv(64).decode()
        #cli.send("Mensaje Recibido".encode())

        
        #cli.close()
    except ValueError:
        print("Oops! ha habido algún problema. Intentelo de nuevo")
    