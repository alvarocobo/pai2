import json
import ast

def coincidencia(archivo,usuario,contraseña):
    f = open(archivo,"r")
    dic = ast.literal_eval(f.read())
    for t in dic:
        if t == usuario:
            if dic[t] == contraseña:
                return True
    f.close()
    return False
  


def almacen(archivo,usuario,mensaje):
    existe = False
    diccionario = dict()
    try:
        f = open(archivo, 'r')
        dic = ast.literal_eval(f.read())
        for t in dic:
            if t == usuario:
                existe = True
                lista = dic[t]
                lista.append(mensaje)
                diccionario[t] = lista
            else:
                diccionario[t] = dic[t]


    except:
        f = open(archivo, 'w')
        dic = dict()
        d = json.dumps(dic)
        f.write(d)
        
    if(existe==False):
        diccionario[usuario] = [mensaje]  

    f = open(archivo, 'w')
    jso = json.dumps(diccionario)
    f.write(jso)
    f.close()


