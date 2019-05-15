TRAMPA = -1
RESULTADO_ACEPTADO = "ACEPTADO"
RESULTADO_TRAMPA = "TRAMPA"
RESULTADO_NO_ACEPTADO = "NO_ACEPTADO"

digito = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letra = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", 
"p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", 
"F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", 
"U", "V", "W", "X", "Y", "Z"]

#delta Numeros
def d_Numeros(estado_anterior, caracter):
    if estado_anterior == 0 and caracter in digito:
        return 1
    if estado_anterior == 1 and caracter in digito:
        return 1
    if estado_anterior == 1 and caracter == ".":
        return 2
    if estado_anterior == 2 and caracter in digito:
        return 3
    if estado_anterior == 3 and caracter in digito:
        return 3

    
    return TRAMPA

#automata Numeros
def A_Numeros(cadena):
    Finales = [1, 3]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_Numeros(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

casosNumeros = [
    ("13", RESULTADO_ACEPTADO),
    ("2.69a8", RESULTADO_TRAMPA),
    ("1323234.3", RESULTADO_ACEPTADO),
    ("2522.9.99", RESULTADO_TRAMPA),
    (".0111", RESULTADO_TRAMPA),
    ("1.0000003", RESULTADO_ACEPTADO)
]

for cadena, resultado in casosNumeros:
    assert A_Numeros(cadena) == resultado


#delta String
def d_String(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "´":
        return 1
    if estado_anterior == 1 and caracter in letra:
        return 2
    if estado_anterior == 1 and caracter in digito:
        return 2    
    if estado_anterior == 2 and caracter in letra:
        return 2
    if estado_anterior == 2 and caracter in digito:
        return 2 
    if estado_anterior == 2 and caracter == "´":
        return 3

    
    return TRAMPA

#automata String
def A_String(cadena):
    Finales = [3]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_String(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

casosString = [
    ("´AAAdssGFKHFga111skgAHADSF´", RESULTADO_ACEPTADO),    
    ("´aBcDe1F2g3´", RESULTADO_ACEPTADO),
    ("´aaaaas******´", RESULTADO_TRAMPA),
    ("´HolaMundo999´", RESULTADO_ACEPTADO),
    ("'-'", RESULTADO_TRAMPA),
    ("´MeGustanLasMilanesasYElNumero73´", RESULTADO_ACEPTADO),
    (":)", RESULTADO_TRAMPA),
]

for cadena, resultado in casosString:
    assert A_String(cadena) == resultado


#delta Identificador
def d_ID(estado_anterior, caracter):
    if estado_anterior == 0 and caracter in letra:
        return 1
    if estado_anterior == 1 and caracter in letra:
        return 1
    if estado_anterior == 1 and caracter in digito:
        return 1

    
    return TRAMPA

#automata Identificador
def A_ID(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_ID(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

casosID = [
    ("Adsga11sF", RESULTADO_ACEPTADO),    
    ("aBcDe1F2g3", RESULTADO_ACEPTADO),
    ("aaaaas******", RESULTADO_TRAMPA),
    ("999HolaMundo999", RESULTADO_TRAMPA),
    ("'-'", RESULTADO_TRAMPA),
    ("MeGustanLasMilanesasYElNumero73", RESULTADO_ACEPTADO),
    ("1S1", RESULTADO_TRAMPA),
]

for cadena, resultado in casosID:
    assert A_ID(cadena) == resultado