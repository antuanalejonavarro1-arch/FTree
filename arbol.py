import pydot

def arbol_a_imagen(arbol, archivo="arbol.png"):
    graph = pydot.Dot(graph_type='digraph')
    contador = 0

    def agregar(nodo, padre=None):
        nonlocal contador

        nombre_nodo = f"{nodo}_{contador}"
        contador += 1

        if isinstance(nodo, str):
            nodo_actual = pydot.Node(nombre_nodo, label=nodo)
        else:
            nodo_actual = pydot.Node(nombre_nodo, label=nodo.label())

        graph.add_node(nodo_actual)

        if padre:
            graph.add_edge(pydot.Edge(padre, nodo_actual))

        if not isinstance(nodo, str):
            for hijo in nodo:
                agregar(hijo, nodo_actual)

    agregar(arbol)
    graph.write_png(archivo)


def arbol_a_imagen_ast(ast, archivo="ast.png"):
    graph = pydot.Dot(graph_type='digraph')
    contador = 0

    def agregar(nodo, padre=None):
        nonlocal contador

        nombre = f"n{contador}"
        contador += 1

        if isinstance(nodo, str):
            nodo_actual = pydot.Node(nombre, label=nodo)
        else:
            etiqueta, hijos = nodo
            nodo_actual = pydot.Node(nombre, label=etiqueta)

        graph.add_node(nodo_actual)

        if padre:
            graph.add_edge(pydot.Edge(padre, nodo_actual))

        if not isinstance(nodo, str):
            for hijo in hijos:
                agregar(hijo, nodo_actual)

    agregar(ast)
    graph.write_png(archivo)