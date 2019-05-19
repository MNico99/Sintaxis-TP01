from GLex.py import *
from GSin.py import *

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
"!", "true", "false", ".", "'"]

def lexer(cadena):
