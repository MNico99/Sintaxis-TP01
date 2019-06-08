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
    ('LLAVE_ABIERTA', A_LlaveAbierta),
    ('LLAVE_CERRADA', A_LlaveCerrada),
    ('EXCLAMACION', A_Exclamacion),
    ('GUION_MEDIO', A_Guionmedio),
    ('MAS', A_Mas),
    ('PUNTO', A_Punto),
    ('COMA', A_PuntoComa),
    ('SLASH', A_Slash),
    ('IGUAL', A_Igual),
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



def lex(cadena):

    tokens = []
    index = 0
    cadenaPrefijo = cadena.split()
    
      
    while index < len(cadenaPrefijo):
        
        lexeme = ""
        lexeme = cadenaPrefijo[index]
        candidatos = []

        for  tipoDeToken, automata in TokenConfig:
            resultado = automata(lexeme)
            if resultado == RESULTADO_ACEPTADO:
                candidatos.append(tipoDeToken)
                break
        
        
        if len(candidatos) == 0:
            raise Exception("TOKEN NO ACEPTADO " + lexeme)
        else:
            index += 1
            tipoDeToken = candidatos[0]
            tokens.append((tipoDeToken, lexeme))

    return tokens
