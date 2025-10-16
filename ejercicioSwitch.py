def pedir_num():
    print("ingrese un numero del 1 al 12:")
    numero = int(input())
    return numero

def revisar_numero_mes(num_mes):
    mes = " "
    match num_mes:
        case 1:
            mes = "el mes es enero"
        case 2:
            mes = "el mes es febrero"
        case 3:
            mes = "el mes es marzo"
        case 4:
            mes = "el mes es abril"
        case 5:
            mes = "el mes es mayo"
        case 6:
            mes = "el mes es junio"
        case 7:
            mes = "el mes es julio"
        case 8:
            mes = "el mes es agosto"
        case 9:
            mes = "el mes es septiembre"
        case 10:
            mes = "el mes es octubre"
        case 11:
            mes = "el mes es noviembre"
        case 12:
            mes = "el mes es diciembre"
        
    return mes

def mostrar_mensaje(mes):
    print (mes)
             
#--------------------ZONA DE CODIGO PRINCIPAL----------------------
numero = pedir_num()
mes = revisar_numero_mes(numero)
mostrar_mensaje(mes)

            