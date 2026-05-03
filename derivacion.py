def derivacion_izquierda(arbol):
    pasos = []

    actual = [arbol.label()]
    pasos.append(formatear(actual))

    def derivar(nodo, sentencia):
        if isinstance(nodo, str):
            return sentencia

        for i, simbolo in enumerate(sentencia):
            if simbolo == nodo.label():

                expansion = []
                for hijo in nodo:
                    if isinstance(hijo, str):
                        expansion.append(hijo)
                    else:
                        expansion.append(hijo.label())

                nueva = sentencia[:i] + expansion + sentencia[i+1:]

                pasos.append(formatear_color(sentencia, nueva, i, expansion))

                for hijo in nodo:
                    nueva = derivar(hijo, nueva)

                return nueva
        return sentencia

    derivar(arbol, actual)
    return pasos


def derivacion_derecha(arbol):
    pasos = []

    actual = [arbol.label()]
    pasos.append(formatear(actual))

    def derivar(nodo, sentencia):
        if isinstance(nodo, str):
            return sentencia

        for i in reversed(range(len(sentencia))):
            if sentencia[i] == nodo.label():

                expansion = []
                for hijo in nodo:
                    if isinstance(hijo, str):
                        expansion.append(hijo)
                    else:
                        expansion.append(hijo.label())

                nueva = sentencia[:i] + expansion + sentencia[i+1:]

                pasos.append(formatear_color(sentencia, nueva, i, expansion))

                for hijo in reversed(nodo):
                    nueva = derivar(hijo, nueva)

                return nueva
        return sentencia

    derivar(arbol, actual)
    return pasos



# FORMATO BASE

def formatear(lista):
    return " ".join(lista)


# FORMATO CON COLORES
def formatear_color(antes, despues, indice, expansion):
    resultado = []

    for i, simbolo in enumerate(despues):

        # NUEVA EXPANSIÓN (verde)
        if indice <= i < indice + len(expansion):
            resultado.append(f"<span style='color:#3fb950; font-weight:bold'>{simbolo}</span>")

        # RESTO NORMAL
        else:
            resultado.append(simbolo)

    # MARCAR EL REEMPLAZADO EN ROJO
    antes_str = " ".join(antes)
    antes_str = antes_str.replace(
        antes[indice],
        f"<span style='color:#f85149; text-decoration:line-through'>{antes[indice]}</span>",
        1
    )

    despues_str = " ".join(resultado)

    return antes_str + " ⇒ " + despues_str