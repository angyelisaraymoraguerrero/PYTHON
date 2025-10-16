# ------- zona de funciones -------------------
def hacer_bucle():
    while True:
        print("digite la letra A para actualizar el sistema")
        print("digite la letra E para eliminar el catalogo")
        print("digite la letra C para crear productos")
        print("digite la letra S para salir del programa")
    
        letra = str(input())
        
        if letra == 's' or letra == 'S':
            print("ha finalizado con exito")
            break
        else:
            print("sigue dentro del proceso do while")
   
    
    return letra
    
def hacerSegunCaso():
    
    dato_letra = hacer_bucle()
    
    match dato_letra:
        case "A":
            print(" sistema actualizado ")
        case "C":
            print(" catalogo eliminado ")
        case "E":
            print(" producto creado ")
            
            
# -------------- zona de codigo principal -------    
#Llamar funciones
hacerSegunCaso()
#si hay argumento siempre debe haber parametro
            