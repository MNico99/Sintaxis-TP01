# -*- coding: utf-8 -*-
from automatas import *



TokenConfig = [
    ('IF', A_If),
    ('EOF', A_EOF),
    ('ELSE', A_Else),
    ('FALSE', A_False),
    ('FOR', A_FOR),
    ('FUN', A_FUN),
    ('RETURN', A_Return),
    ('TRUE', A_True),
    ('VAR', A_VAR),
    ('WHILE', A_While),
    ('PAREN_OPEN', A_ParenOpen),
    ('PAREN_CLOSE', A_ParenClose),
    ('APOSTROFO', A_Apostrofo),
    ('ASTERISCO', A_Asterisco),
    ('COMA', A_Coma),
    ('CORCHETE_ABIERTO', A_CorcheteAbierto),
    ('CORCHETE_CERRADO', A_CorcheteCerrado),
    ('EXCLAMACION', A_Exclamacion),
    ('GUION_MEDIO', A_Guionmedio),
    ('MAS', A_Mas),
    ('PUNTO', A_Punto),
    ('COMA', A_PuntoComa),
    ('SLASH', A_Slash),
    ('DOBLE_IGUAL', A_DobleIgual),
    ('EXCLAMACION_IGUAL', A_ExclamacionIgual),
    ('MENOR', A_Menor),
    ('MAYOR', A_Mayor),
    ('MAYOR_IGUAL', A_Mayorigual),
    ('MENOR_IGUAL', A_Menorigual),
    ('AND', A_AND),
    ('OR', A_OR),
    ("NUM", A_Num),
    ("STRING", A_String),
    ("ID", A_ID),
]

cadena = "if"

def lex(cadena):
    tokens = []
    index = 0
    start = 0
    
      
    while index < len(cadena):
        posible_candidato = []
        candidatos = []
        lexeme = ""
        cadenaPrefijo = ""
        todosTrampa = False

        while not todosTrampa:
            todosTrampa = True
            lexeme  = cadenaPrefijo
            cadenaPrefijo = cadena[start: index + 1]
            posible_candidato = candidatos 
            candidatos = []

            for automata, tipoDeToken  in TokenConfig:
                resultado = automata(cadenaPrefijo)
                if resultado == RESULTADO_ACEPTADO:
                    posible_candidato.append(tipoDeToken)
                    todosTrampa = False
                elif resultado == RESULTADO_NO_ACEPTADO:
                    todosTrampa = False
        
            index += 1

        index -= 1

        tipoDeToken = candidatos[0]
        tokens.append([lexeme, tipoDeToken])

    return tokens



        
                    
        