# -*- coding: utf-8 -*-
from automatas import *


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
'''
def lex(cadena):
    tokens = []
    start = 0
    index = 0
    aux = cadena.split()
    for index in range(0, len(aux)):
        if automata(aux[index]) == RESULTADO_ACEPTADO:
            lexer.append("IF", aux[index])
'''
cadena = "999"