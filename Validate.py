def validar_lenght (cadena: str, longitud_minima: int, longitud_maxima: int)->bool:
    longitud = len(cadena)

    return longitud >= longitud_minima and longitud <= longitud_maxima                        




def validar_number (numero: int | float, minima: float | int, maxima: float | int)->bool:

    return numero >= minima and numero <= maxima                           

                                                                                          

