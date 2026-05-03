def construir_ast(nodo):
    # Si es terminal
    if isinstance(nodo, str):
        return nodo

    label = nodo.label()
    hijos = list(nodo)

    # Regla: eliminar paréntesis → quedarse con el contenido
    if len(hijos) == 3 and hijos[0] == '(' and hijos[2] == ')':
        return construir_ast(hijos[1])

    # Regla: operación binaria (E + E, T * T, etc)
    if len(hijos) == 3:
        izq = construir_ast(hijos[0])
        op = hijos[1]
        der = construir_ast(hijos[2])
        return (op, [izq, der])

    # Regla: nodo con un solo hijo → colapsar
    if len(hijos) == 1:
        return construir_ast(hijos[0])

    # fallback
    return (label, [construir_ast(h) for h in hijos])