
#Variables
host = 'localhost'
port = 8000
#Se importa el módulo
import socket
import ssl

try:
    #Creación de un objeto socket (lado cliente)
    obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ssl_socket = ssl.wrap_socket(obj,ca_certs="server.crt",
                            cert_reqs=ssl.CERT_REQUIRED, ssl_version=ssl.PROTOCOL_TLSv1_2
                            )
    #ciphers = "ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:AES128-GCM-SHA256:AES128-SHA256:HIGH:"
    
    #Conexión con el servidor. Parametros: IP (puede ser del tipo 192.168.1.1 o localhost), Puerto
    ssl_socket.connect((host, port))

    usuario = input("Introduzca su usuario: ")
    ssl_socket.write(usuario.encode())
    print("usuario: ", usuario)

    contraseña = input("Introduzca la contraseña: ")
    ssl_socket.write(contraseña.encode())
    print("contraseña: ", contraseña)
    
    mensaje = input("Introduzca el mensaje: ")
    ssl_socket.write(mensaje.encode("ISO-8859-1"))
    print("mensaje: ", mensaje)

    respuesta = ssl_socket.read().decode()
    print("respuesta: ", respuesta)
    ssl_socket.close()

except ValueError:
    print("\nconexión fallida. Inténtelo de nuevo")   
    #ssl_socket.send(mensaje.encode())
    #print(ssl_socket.recv(64).decode())