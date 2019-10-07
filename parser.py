from automatas import *
from lex import *

prods = {
    'Programa':[
        ['ListaDecl', '"eof"']
    ],

    'ListaDecl':[
        ['ListaDecl', 'Declaracion'],
        ['λ']
    ],

    'Declaracion':[
        ['FunDecl'],
        ['VarDecl'],
        ['Sentencia']
    ],

    'FunDecl':[
        ['"fun"', 'Funcion']
    ],

    'Funcion':[
        ['Identificador', '"("', 'ListaParametros', '")"', 'Bloque']
    ],

    'ListaParametros':[
        ['λ'],
        ['Parametros']
    ],

    'Parametros':[
        ['Identificador'],
        ['Parametros', '","', 'Identificador']
    ],

    'VarDecl':[
        ['"var"', 'Identificador', '";"'],
        ['"var"', 'Identificador', '"="', 'Expresion', '";"']
    ],

    'Sentencia':[
        ['ExprSent'],
        ['ForSent'],
        ['IfSent'],
        ['ReturnSent'],
        ['WhileSent'],
        ['Bloque'],
    ],

    'ExprSent':[
        ['Expresion', '";"']
    ],

    'Expresion':[
        ['Asignacion']
    ],

    'Asignacion':[
        ['Identificador', '"="', 'Primitivo'],
        ['OLogico', '";"'],
    ],

    'ForSent':[
        ['"for"', '"("', 'PriArg', 'AdicArg', '";"', 'AdicArg', '")"', 'Sentencia']
    ],

    'PriArg':[
        ['VarDecl'],
        ['ExprSent'],
        ['";"']
    ],

    'AdicArg':[
        ['λ'],
        ['Expresion']
    ],

    'IfSent':[
        ['"if"', '"("', 'Expresion', '")"', 'Sentencia', '"else"', 'Sentencia'],
        ['"if"', '"("', 'Expresion', '")"', 'Sentencia']
    ],

    'ReturnSent':[
        ['"return"', 'Expresion', '";"'],
        ['"return"', '";"']
    ],

    'WhileSent':[
        ['"while"', '"("', 'Expresion', '")"', 'Sentencia']
    ],

    'Bloque':[
        ['"{"', 'ListaSent', '"}"']
    ],

    'ListaSent':[
        ['Sentencia', 'ListaSent'],
        ['λ'],
    ],

    'OLogico':[
        ['YLogico'],
        ['YLogico', '"or"', 'OLogico']
    ],

    'YLogico':[
        ['Igua'],
        ['Igua', '"and"', 'YLogico']
    ],

    'Igua':[
        ['Comparacion'],
        ['Comparacion', '"=="', 'Igua'],
        ['Comparacion', '"!="', 'Igua']
    ],

    'Comparacion':[
        ['Suma'],
        ['Suma', '">"', 'Comparacion'],
        ['Suma', '">="', 'Comparacion'],
        ['Suma', '"<"', 'Comparacion'],
        ['Suma', '"<="', 'Comparacion']
    ],

    'Suma':[
        ['Mult'],
        ['"-"', 'Suma'],
        ['"+"', 'Suma']
    ],

    'Mult':[
        ['Unario'],
        ['"/"', 'Mult'],
        ['"*"', 'Mult']
    ],

    'Unario':[
        ['"!"', 'Unario'],
        ['"-"', 'Unario'],
        ['Primitivo']
    ],

    'Primitvo':[
        ['"true"'],
        ['"false"'],
        ['Numero'],
        ['String'],
        ['Identificador'],
        ['"("', 'Expresion', '")"']
    ]

}

noTerminales = ['Programa',
                'ListaDecl',
                'Declaracion',
                'FunDecl',
                'Funcion',
                'ListaParametros',
                'Parametros',
                'VarDecl',
                'Sentencia',
                'ExprSent',
                'Expresion',
                'Asignacion',
                'ForSent',
                'PriArg',
                'AdicArg',
                'IfSent',
                'ReturnSent',
                'WhileSent',
                'Bloque',
                'ListaSent',
                'OLogico',
                'YLogico',
                'Igua',
                'Comparacion',
                'Suma',
                'Mult',
                'Unario',
                'Primitivo'
]

def parser(tokens):
    
    self={
        'tokens': tokens,
        'index': 0,
        'error': False,
        }


    def parse():
        error = False
        index = 0
        pni('S')
        
        if not error == True and tokens(index) == "#":
            return True
        else:
            return False
    

    def procesar(parteDerecha):

        for simbolo in parteDerecha:
            if esTerminal(simbolo):
                if simbolo == tokens[index]:
                    index+=1
                else:
                    error = True
                    break

            if esNoTerminal(simbolo):
                pni(simbolo)
                if error == True:
                    break


    def pni(noTerminal):

        for parteDerecha in prods[noTerminal]:
            error = False
            index_aux = index
            procesar(parteDerecha)
            if error == False:
                break
            else:
                index = index_aux


def esTerminal(simbolo):