from nltk import CFG
from nltk.parse import ChartParser

def analizar_entrada(texto_gramatica, texto_cadena):
    gramatica = CFG.fromstring(texto_gramatica)
    parser = ChartParser(gramatica)
    cadena = texto_cadena.split()

    arboles = list(parser.parse(cadena))
    return arboles