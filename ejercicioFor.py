def pedir_cantidad_numeros():
    print("digite la cantidad de numeros que desea sumar:")
    cantidad = int(input())
    return cantidad
    
def sumar_numeros(cantidad):
    suma = 0
    for i in range (cantidad):
        print(f"digite el numero {i+1} que desea sumar")
        numero = int(input())
        suma = suma + numero
    return suma 
        
def mostrar_mensaje(sumatoria):
    print(f"la suma de los numeros anteriores es:{sumatoria}")
        
#---------------------------ZONA DE CODIGO PRINCIPAL--------------------------------------
cantidad = pedir_cantidad_numeros()
cantidadSumada = sumar_numeros(cantidad)
mostrar_mensaje(cantidadSumada)
