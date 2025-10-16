def pedir_Numero():
    print("ingrese un numero")
    num = float(input())
    return num
    
def validar_Numero_Par():
    num = pedir_Numero()
    while num!=0:
        if num%2==0:
            respuesta = ("el numero es par")   
        else:
            respuesta =("el numero es impar")

        mostrarMensaje(respuesta)
        
        num = pedir_Numero()
        
def mostrarMensaje(respuesta):
    print(respuesta)        
#------------------Codigo Principal
#Llamar Funciones
condicion = validar_Numero_Par()

