# -*- coding: utf-8 -*-
from GLex import *
from GSin import *

TRAMPA = -1
RESULTADO_ACEPTADO = "ACEPTADO"
RESULTADO_TRAMPA = "TRAMPA"
RESULTADO_NO_ACEPTADO = "NO_ACEPTADO"

digito = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letra = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", 
"p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", 
"F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", 
"U", "V", "W", "X", "Y", "Z"]

tokens = ["eof", "fun", "(", ")", ",", "var", ";", "=", "if", "for", "else", "return", 
"while", "{", "}", "or", "and", "==", "!=", ">", "<", "<=", ">=", "-", "+", "/", "*", 
"!", "true", "false", ".", "'", "Numeros", "ID", "String"]


#for posicion,char in enumerate(cadena):
#    if char != espacio:
#        lexeme += char # adding a char each time
#    if (posicion+1 < len(string)): # prevents error
#       if string[posicion+1] == espacio # if next char == ' '
#            if lexeme != '':
#                print(lexeme.replace('\n', '<newline>'))
#                lexeme = ''
espacio = ' '
lexeme = ''
lexer = []
cadena = " if else"

ej= cadena.split()

for posicion in range(0, len(ej)):
    if A_If(ej[posicion]) == RESULTADO_ACEPTADO:
        lexer += ("IF", ej[posicion])
    if A_Else(ej[posicion]) == RESULTADO_ACEPTADO:
        lexer += ("ELSE", ej[posicion])
    

for posicion,char in enumerate(cadena):
    if char != espacio:
        lexeme += char
        if A_AND(cadena) == RESULTADO_ACEPTADO:
            lexer += ("AND", lexeme) 
        if A_Apostrofo(cadena) == RESULTADO_ACEPTADO:
            lexer += ("'", lexeme)
        if A_Asterisco(cadena) == RESULTADO_ACEPTADO:
            lexer += ("*", lexeme)
        if A_Coma(cadena) == RESULTADO_ACEPTADO:
            lexer += (",", lexeme)      
        if A_CorcheteAbierto(cadena) == RESULTADO_ACEPTADO:
            lexer += ("[", lexeme)    
        if A_CorcheteCerrado(cadena) == RESULTADO_ACEPTADO:
            lexer += ("]", lexeme)
        if A_DobleIgual(cadena) == RESULTADO_ACEPTADO:
            lexer += ("==", lexeme)
        if A_Else(cadena) == RESULTADO_ACEPTADO:
            lexer += ("ELSE", lexeme)
        if A_EOF(cadena) == RESULTADO_ACEPTADO:
            lexer += ("EOF", lexeme)
        if A_Exclamacion(cadena) == RESULTADO_ACEPTADO:
            lexer += ("!", lexeme)
        if A_ExclamacionIgual(cadena) == RESULTADO_ACEPTADO:
            lexer += ("!=", lexeme)
        if A_False(cadena) == RESULTADO_ACEPTADO:
            lexer += ("FALSE", lexeme)
        if A_FOR(cadena) == RESULTADO_ACEPTADO:
            lexer += ("FOR", lexeme)
        if A_FUN(cadena) == RESULTADO_ACEPTADO:
            lexer += ("FUN", lexeme)
        if A_Guionmedio(cadena) == RESULTADO_ACEPTADO:
            lexer += ("-", lexeme)
        if A_ID(cadena) == RESULTADO_ACEPTADO:
            lexer += ("ID", lexeme)
        if A_If(cadena) == RESULTADO_ACEPTADO:
            lexer += ("IF", lexeme)
        if A_Igual(cadena) == RESULTADO_ACEPTADO:
            lexer += ("=", lexeme)
        if A_Mas(cadena) == RESULTADO_ACEPTADO:
            lexer += ("+", lexeme)
        if A_Mayor(cadena) == RESULTADO_ACEPTADO:
            lexer += (">", lexeme)
        if A_Mayorigual(cadena) == RESULTADO_ACEPTADO:
            lexer += (">=", lexeme)
        if A_Menorigual(cadena) == RESULTADO_ACEPTADO:
            lexer += ("<=", lexeme)
        if A_Menor(cadena) == RESULTADO_ACEPTADO:
            lexer += ("<", lexeme)
        if A_Numeros(cadena) == RESULTADO_ACEPTADO:
            lexer += ("NUMEROS", lexeme)
        if A_OR(cadena) == RESULTADO_ACEPTADO:
            lexer += ("OR", lexeme)
        if A_ParenClose(cadena) == RESULTADO_ACEPTADO:
            lexer += (")", lexeme)
        if A_ParenOpen(cadena) == RESULTADO_ACEPTADO:
            lexer += ("(", lexeme)
        if A_Punto(cadena) == RESULTADO_ACEPTADO:
            lexer += (".", lexeme)
        if A_PuntoComa(cadena) == RESULTADO_ACEPTADO:
            lexer += (";", lexeme)
        if A_Return(cadena) == RESULTADO_ACEPTADO:
            lexer += ("RETURN", lexeme)
        if A_Slash(cadena) == RESULTADO_ACEPTADO:
            lexer += ("/", lexeme)
        if A_String(cadena) == RESULTADO_ACEPTADO:
            lexer += ("STRING", lexeme)
        if A_True(cadena) == RESULTADO_ACEPTADO:
            lexer += ("TRUE", lexeme)
        if A_VAR(cadena) == RESULTADO_ACEPTADO:
            lexer += ("VAR", lexeme)
        if A_While(cadena) == RESULTADO_ACEPTADO:
            lexer += ("WHILE", lexeme)
    if (posicion+1 < len(cadena)): 
        if cadena[posicion+1] == espacio:
            if lexeme != '':
                lexeme = ''
print(lexer)