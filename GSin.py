TRAMPA = -1
RESULTADO_ACEPTADO = "ACEPTADO"
RESULTADO_TRAMPA = "TRAMPA"
RESULTADO_NO_ACEPTADO = "NO_ACEPTADO"

digito = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letra = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", 
"p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", 
"F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", 
"U", "V", "W", "X", "Y", "Z"]

#delta while
def d_While(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "w":
        return 1
    if estado_anterior == 1 and caracter == "h":
        return 2
    if estado_anterior == 2 and caracter == "i":
        return 3
    if estado_anterior == 3 and caracter == "l":
        return 4
    if estado_anterior == 4 and caracter == "e":
        return 5

    
    return TRAMPA

#automata While
def A_While(cadena):
    Finales = [5]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_While(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

casosWhile = [
    ("while", RESULTADO_ACEPTADO),
    ("2.69a8", RESULTADO_TRAMPA),
    ("whi", RESULTADO_NO_ACEPTADO),
]

for cadena, resultado in casosWhile:
    assert A_While(cadena) == resultado

#############################

#delta {
def d_CorcheteAbierto(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "{":
        return 1

    
    return TRAMPA

#automata {
def A_CorcheteAbierto(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_CorcheteAbierto(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

casosCorcheteAbierto = [
    ("{", RESULTADO_ACEPTADO),
    ("}", RESULTADO_TRAMPA),
]

for cadena, resultado in casosCorcheteAbierto:
    assert A_CorcheteAbierto(cadena) == resultado

#############################

#delta }
def d_CorcheteCerrado(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "}":
        return 1

    
    return TRAMPA

#automata }
def A_CorcheteCerrado(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_CorcheteCerrado(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

casosCorcheteCerrado = [
    ("}", RESULTADO_ACEPTADO),
    ("{", RESULTADO_TRAMPA),
]

for cadena, resultado in casosCorcheteCerrado:
    assert A_CorcheteCerrado(cadena) == resultado

#############################

#delta OR
def d_OR(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "o":
        return 1
    if estado_anterior == 1 and caracter == "r":
        return 2

    
    return TRAMPA

#automata OR
def A_OR(cadena):
    Finales = [2]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_OR(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

casosOR = [
    ("or", RESULTADO_ACEPTADO),
    ("trampa", RESULTADO_TRAMPA),
    ("o", RESULTADO_NO_ACEPTADO),
]

for cadena, resultado in casosOR:
    assert A_OR(cadena) == resultado

#############################

#delta AND
def d_AND(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "a":
        return 1
    if estado_anterior == 1 and caracter == "n":
        return 2
    if estado_anterior == 2 and caracter == "d":
        return 3

    
    return TRAMPA

#automata AND
def A_AND(cadena):
    Finales = [3]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_AND(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

casosAND = [
    ("and", RESULTADO_ACEPTADO),
    ("trampa", RESULTADO_TRAMPA),
    ("an", RESULTADO_NO_ACEPTADO),
]

for cadena, resultado in casosAND:
    assert A_AND(cadena) == resultado

#############################

#delta ==
def d_DobleIgual(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "=":
        return 1
    if estado_anterior == 1 and caracter == "=":
        return 2

    
    return TRAMPA

#automata ==
def A_DobleIgual(cadena):
    Finales = [2]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_DobleIgual(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

casosDobleIgual = [
    ("==", RESULTADO_ACEPTADO),
    ("trampa", RESULTADO_TRAMPA),
    ("=", RESULTADO_NO_ACEPTADO),
]

for cadena, resultado in casosDobleIgual:
    assert A_DobleIgual(cadena) == resultado

#############################

#delta !=
def d_ExclamacionIgual(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "!":
        return 1
    if estado_anterior == 1 and caracter == "=":
        return 2

    
    return TRAMPA

#automata !=
def A_ExclamacionIgual(cadena):
    Finales = [2]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_ExclamacionIgual(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

casosExclamacionIgual = [
    ("!=", RESULTADO_ACEPTADO),
    ("trampa", RESULTADO_TRAMPA),
    ("!", RESULTADO_NO_ACEPTADO),
]

for cadena, resultado in casosExclamacionIgual:
    assert A_ExclamacionIgual(cadena) == resultado

#############################

#delta >
def d_Mayor(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == ">":
        return 1

    
    return TRAMPA

#automata >
def A_Mayor(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_Mayor(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

casosMayor = [
    (">", RESULTADO_ACEPTADO),
    ("trampa", RESULTADO_TRAMPA),
]

for cadena, resultado in casosMayor:
    assert A_Mayor(cadena) == resultado

#################################################################

#delta '
def d_Apostrofo(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "'":
        return 1

    return TRAMPA

#automata '

def A_Apostrofo(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = D_Apostrofo(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta *
def d_Asterisco(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "*":
        return 1

    return TRAMPA

#automata *

def A_Asterisco(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = D_Asterisco(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta !
def d_Exclamacion(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "!":
        return 1

    return TRAMPA

#automata !

def A_Exclamacion(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_Exclamacion(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta false
def d_False(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "f":
        return 1
    if estado_anterior == 1 and caracter == "a":
        return 2
    if estado_anterior == 2 and caracter == "l":
        return 3
    if estado_anterior == 3 and caracter == "s":
        return 4
    if estado_anterior == 4 and caracter == "e":
        return 5

    return TRAMPA

#automata false

def A_False(cadena):
    Finales = [5]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_False(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO


#################################################################

#delta -
def d_Guionmedio(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "-":
        return 1

    return TRAMPA

#automata -

def A_Guionmedio(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_Guionmedio(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta +
def d_Mas(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "+":
        return 1

    return TRAMPA

#automata +

def A_Mas(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_Mas(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta >=
def d_Mayorigual(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == ">":
        return 1
    if estado_anterior == 1 and caracter == "=":
        return 2

    return TRAMPA

#automata >=

def A_Mayorigual(cadena):
    Finales = [2]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_Mayorigual(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta <=
def d_Menorigual(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "<":
        return 1
    if estado_anterior == 1 and caracter == "=":
        return 2

    return TRAMPA

#automata <=

def A_Menorigual(cadena):
    Finales = [2]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_Menorigual(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta .
def d_Punto(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == ".":
        return 1

    return TRAMPA

#automata .

def A_Punto(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_Punto(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta /
def d_Slash(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "/":
        return 1

    return TRAMPA

#automata /

def A_Slash(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_Slash(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta true
def d_True(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "t":
        return 1
    if estado_anterior == 1 and caracter == "r":
        return 2
    if estado_anterior == 2 and caracter == "u":
        return 3
    if estado_anterior == 3 and caracter == "e":
        return 4

    return TRAMPA

#automata true

def A_True(cadena):
    Finales = [4]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_True(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################