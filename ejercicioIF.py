def pedir_numero():
    print("ingrese un numero")
    numero = int(input())
    return numero

def verificar_tipo_num(numero):
    if numero>0:
        tipo_num = "el numero es positivo"
    elif numero <0:
        tipo_num = "el numero es negativo"
    else:
        tipo_num = "el numero es neutro"
    return tipo_num

def mostrar_mensaje(tipo_numero):
    print (tipo_numero)
    
#-----------------------ZONA DE CODIGO PRINCIPAL------------------------
num = pedir_numero()
tipo_numero = verificar_tipo_num(num)
mostrar_mensaje(tipo_numero)

        