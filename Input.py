from Validate import *



def get_int (mensaje: str, mensaje_error: str, intentos: int)->int|None:

    errores = 0
    numero = int(input(mensaje))
    resultado = None

    while validar_number(numero,1,5) == False:
        errores += 1
 
        if errores == intentos:
            print("SE ACABARON LOS INTENTOS")
            
            break

        numero = int(input(mensaje_error))


    if validar_number(numero,1,5) == True:
        resultado = numero

    return resultado


print(get_int("INGRESE UN NUMERO: ", "INGRESE UN NUMERO VALIDO: ", 3))




def get_float (mensaje: str, mensaje_error: str, intentos: int)->float|None:

    errores = 0
    numero = float(input(mensaje))
    resultado = None

    while validar_number(numero,1.5,5.5) == False:
        errores += 1
 
        if errores == intentos:
            print("SE ACABARON LOS INTENTOS")
           
            break

        numero = float(input(mensaje_error))


    if validar_number(numero,1.5,5.5) == True:
        resultado = numero

    return resultado


print(get_float("INGRESE UN NUMERO: ", "INGRESE UN NUMERO VALIDO: ", 3))




def get_string (mensaje: str, mensaje_error: str, intentos: int)->str|None:

    errores = 0
    cadena = input(mensaje)
    resultado = None

    while validar_lenght(cadena,1,5) == False:
        errores += 1
 
        if errores == intentos:
            print("SE ACABARON LOS INTENTOS")
           
            break

        cadena = input(mensaje_error)


    if validar_lenght(cadena,1,5) == True:
        resultado = cadena

    return resultado


print(get_string("INGRESE UNA CADENA: ", "INGRESE UNA CADENA VALIDO: ", 3))                         

                                                                                          
