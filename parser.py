from automatas import *
from lex import *

prods = {
    'S': [

    ]
}

noTerminales = [

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