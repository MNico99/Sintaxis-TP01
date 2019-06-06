# -*- coding: utf-8 -*-
from automatas import *


tokenList = [
    ('IF', "if"),
    ('EOF', "eof"),
    ('ELSE', "else"),
    ('FALSE', "false"),
    ('FOR', "for"),
    ('FUN', "fun"),
    ('RETURN', "return"),
    ('TRUE', "true"),
    ('VAR', "var"),
    ('WHILE', "while"),
    ('PAREN_OPEN', "("),
    ('PAREN_CLOSE', ")"),
    ('APOSTROFO', "'"),
    ('ASTERISCO', "*"),
    ('COMA', ","),
    ('LLAVE_ABIERTA', "{"),
    ('LLAVE_CERRADA', "}"),
    ('EXCLAMACION', "!"),
    ('GUION_MEDIO', "-"),
    ('MAS', "+"),
    ('PUNTO', "."),
    ('COMA', ","),
    ('SLASH', "/"),
    ('IGUAL', "="),
    ('DOBLE_IGUAL', "=="),
    ('EXCLAMACION_IGUAL', "!="),
    ('MENOR', "<"),
    ('MAYOR', ">"),
    ('MAYOR_IGUAL', ">="),
    ('MENOR_IGUAL', "<="),
    ('AND', "and"),
    ('OR', "or")
    ]

tokenA = [
    ("NUM", A_Num),
    ("STRING", A_String),
    ("ID", A_ID)
]

def lex(cadena):
    tokens = []
    cadenaPrefijo = cadena.split()
    index = 0
    
      
    while index < len(cadena.split()):
      
        lexeme = ""
        lexeme  = cadenaPrefijo[index]
        candidatos = []

        for  tipoDeToken, word in tokenList:
            if word == lexeme:
                candidatos.append(tipoDeToken)
                break

        if len(candidatos) == 0:
            for tipoDeToken, automata in tokenA:
                resultado = automata(lexeme)
                if resultado == RESULTADO_ACEPTADO:
                    candidatos.append(tipoDeToken)
                    tokens.append((tipoDeToken, lexeme))
                    index +=1
            if len(candidatos) == 0: 
                raise Exception("TOKEN NO ACEPTADO " + lexeme)
        else:
            tipoDeToken = candidatos[0]
            tokens.append((tipoDeToken, lexeme))
            index +=1

    return tokens
