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
lexer = [('', '')]
cadena = "and"

for posicion,char in enumerate(cadena):
    if char != espacio:
        lexeme += char # adding a char each time    
        if A_AND(cadena) == RESULTADO_ACEPTADO:
            lexer = ("AND", lexeme)   
        if A_Apostrofo == RESULTADO_ACEPTADO:
            lexer = ("'", lexeme)
        if A_Asterisco == RESULTADO_ACEPTADO:
            lexer = ("*", lexeme)
        if A_Coma == RESULTADO_ACEPTADO:
            lexer = (",", lexeme)      
        if A_CorcheteAbierto == RESULTADO_ACEPTADO:
            lexer = ("[", lexeme)    
        if A_CorcheteCerrado == RESULTADO_ACEPTADO:
            lexer = ("]", lexeme)
        if A_DobleIgual == RESULTADO_ACEPTADO:
            lexer = ("==", lexeme)
        if A_Else == RESULTADO_ACEPTADO:
            lexer = ("ELSE", lexeme)
        if A_EOF == RESULTADO_ACEPTADO:
            lexer = ("EOF", lexeme)
        if A_Exclamacion == RESULTADO_ACEPTADO:
            lexer = ("!", lexeme)
        if A_ExclamacionIgual == RESULTADO_ACEPTADO:
            lexer = ("!=", lexeme)
        if A_False == RESULTADO_ACEPTADO:
            lexer = ("FALSE", lexeme)
        if A_FOR == RESULTADO_ACEPTADO:
            lexer = ("FOR", lexeme)
        if A_FUN == RESULTADO_ACEPTADO:
            lexer = ("FUN", lexeme)
        if A_Guionmedio == RESULTADO_ACEPTADO:
            lexer = ("-", lexeme)
        if A_ID == RESULTADO_ACEPTADO:
            lexer = ("ID", lexeme)
        if A_If == RESULTADO_ACEPTADO:
            lexer = ("IF", lexeme)
        if A_Igual == RESULTADO_ACEPTADO:
            lexer = ("=", lexeme)
        if A_Mas == RESULTADO_ACEPTADO:
            lexer = ("+", lexeme)
        if A_Mayor == RESULTADO_ACEPTADO:
            lexer = (">", lexeme)
        if A_Mayorigual == RESULTADO_ACEPTADO:
            lexer = (">=", lexeme)
        if A_Menorigual == RESULTADO_ACEPTADO:
            lexer = ("<=", lexeme)
        if A_Menor == RESULTADO_ACEPTADO:
            lexer = ("<", lexeme)
        if A_Numeros == RESULTADO_ACEPTADO:
            lexer = ("NUMEROS", lexeme)
        if A_OR == RESULTADO_ACEPTADO:
            lexer = ("OR", lexeme)
        if A_ParenClose == RESULTADO_ACEPTADO:
            lexer = (")", lexeme)
        if A_ParenOpen == RESULTADO_ACEPTADO:
            lexer = ("(", lexeme)
        if A_Punto == RESULTADO_ACEPTADO:
            lexer = (".", lexeme)
        if A_PuntoComa == RESULTADO_ACEPTADO:
            lexer = (";", lexeme)
        if A_Return == RESULTADO_ACEPTADO:
            lexer = ("RETURN", lexeme)
        if A_Slash == RESULTADO_ACEPTADO:
            lexer = ("/", lexeme)
        if A_String == RESULTADO_ACEPTADO:
            lexer = ("STRING", lexeme)
        if A_True == RESULTADO_ACEPTADO:
            lexer = ("TRUE", lexeme)
        if A_VAR == RESULTADO_ACEPTADO:
            lexer = ("VAR", lexeme)
        if A_While == RESULTADO_ACEPTADO:
            lexer = ("WHILE", lexeme)
print(lexer)