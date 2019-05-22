# -*- coding: utf-8 -*-
from automatas import *

#DEVUELVE QUE AUTOMATA ACEPTA LA CADENA INGRESADA
tokens = []
def automata(src: str) -> tokens:
    
    if cadena[0] in digito:
        A_Num(cadena)
    if cadena[0].isalpha():
        A_AND(cadena)
        A_Else(cadena)
        A_EOF(cadena)
        A_False(cadena)
        A_FOR(cadena)
        A_FUN(cadena)
        A_If(cadena)
        A_OR(cadena)
        A_Return(cadena)
        A_True(cadena)
        A_VAR(cadena)
        A_While(cadena)
        A_ID(cadena)
    if cadena[0] in simbolos:
        A_Asterisco(cadena)
        A_Coma(cadena)
        A_CorcheteAbierto(cadena)
        A_CorcheteCerrado(cadena)
        A_DobleIgual(cadena)
        A_Exclamacion(cadena)
        A_ExclamacionIgual(cadena)
        A_Guionmedio(cadena)
        A_Igual(cadena)
        A_Mas(cadena)
        A_Mayor(cadena)
        A_Mayorigual(cadena)
        A_Menor(cadena)
        A_Menorigual(cadena)
        A_ParenClose(cadena)
        A_ParenOpen(cadena)
        A_PuntoComa(cadena)
        A_Slash(cadena)
    if cadena[0] == "'":
        A_Apostrofo(cadena)
        A_String(cadena)

lexeme = ''
cadena = "9999"

TokenConfig = [
    ('PALABRAS RESERVADAS', A_If),
    ('PALABRAS RESERVADAS', A_EOF),
    ('PALABRAS RESERVADAS', A_Else),
    ('PALABRAS RESERVADAS', A_False),
    ('PALABRAS RESERVADAS', A_FOR),
    ('PALABRAS RESERVADAS', A_FUN),
    ('PALABRAS RESERVADAS', A_Return),
    ('PALABRAS RESERVADAS', A_True),
    ('PALABRAS RESERVADAS', A_VAR),
    ('PALABRAS RESERVADAS', A_While),
    ('SIMBOLOS RESERVADOS', A_ParenOpen),
    ('SIMBOLOS RESERVADOS', A_ParenClose),
    ('SIMBOLOS RESERVADOS', A_Apostrofo),
    ('SIMBOLOS RESERVADOS', A_Asterisco),
    ('SIMBOLOS RESERVADOS', A_Coma),
    ('SIMBOLOS RESERVADOS', A_CorcheteAbierto),
    ('SIMBOLOS RESERVADOS', A_CorcheteCerrado),
    ('SIMBOLOS RESERVADOS', A_Exclamacion),
    ('SIMBOLOS RESERVADOS', A_Guionmedio),
    ('SIMBOLOS RESERVADOS', A_Mas),
    ('SIMBOLOS RESERVADOS', A_Punto),
    ('SIMBOLOS RESERVADOS', A_PuntoComa),
    ('SIMBOLOS RESERVADOS', A_Slash),
    ('OP RELACIONALES', A_DobleIgual),
    ('OP RELACIONALES', A_ExclamacionIgual),
    ('OP RELACIONALES', A_Menor),
    ('OP RELACIONALES', A_Mayor),
    ('OP RELACIONALES', A_Mayorigual),
    ('OP RELACIONALES', A_Menorigual),
    ('OP LOGICOS', A_AND),
    ('OP LOGICOS', A_OR),
    ("NUM", A_Num),
    ("ID", A_ID),
]

def lex(cadena):
  tokens = []
  start = 0
  index = 0
  while index <= len(cadena):
    # tomo un prefijo
    cadenaPrefijo = cadena[start: index + 1]
    todosTrampa = True
    # evaluo la cadena prefijo con cada automata (tiene que definir TokenConfig)
    for automata, tipoDeToken in TokenConfig: 
      resultado = automata(cadenaPrefijo)
      # si resultado NO es resultado trampa
      # entonces  todosTrampa va a ser False,
      # por ende podemos consumir mas caracteres, es decir
      # la cadena prefijo es mas larga

    # fuera del ciclo
    # si son todosTrampa entonces llegue a  la maxima cadena prefijo
    # vuelvo index para atras (index -= 1)
    # y hago tokens.append(nuevoToken)
    # donde nuevo token va a tener el tipo del primer candidato y el lexeme
    # es efectivamente cadenaPrefijo
 
    # SINO son todso tramapa simplemente avanzo el puntero
    #index += 1
      