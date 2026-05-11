# FTree

FTree es una aplicación desarrollada en Python para el análisis de Gramáticas Libres de Contexto (CFG), generación de derivaciones, árboles sintácticos y AST mediante una interfaz gráfica moderna construida con PyQt5.

---

# Características

- Análisis de gramáticas libres de contexto
- Validación de cadenas
- Derivación izquierda
- Derivación derecha
- Generación de árbol sintáctico
- Generación de AST simplificado
- Exportación automática de imágenes
- Interfaz gráfica moderna (Dark Mode)
- Compilable a archivo `.exe`

---

# Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python 3 | Lenguaje principal |
| PyQt5 | Interfaz gráfica |
| NLTK | Parsing y CFG |
| Graphviz | Renderizado de árboles |
| pydot | Conexión Python ↔ Graphviz |
| PyInstaller | Generación del ejecutable |

---

# Requisitos

- Python 3.11 o superior
- Graphviz instalado y agregado al PATH

---

# Instalación

## 1. Clonar repositorio

```bash
git clone https://github.com/TU_USUARIO/FTree.git
```

---

## 2. Entrar al proyecto

```bash
cd FTree
```

---

## 3. Instalar dependencias

```bash
pip install pyqt5
pip install nltk
pip install pydot
```

---

# Instalación de Graphviz

Descargar desde:

https://graphviz.org/download/

Agregar al PATH:

```text
C:\Program Files\Graphviz\bin
```

o

```text
C:\Program Files (x86)\Graphviz\bin
```

---

# Verificar instalación

```bash
dot -V
```

Debe mostrar algo similar a:

```text
dot - graphviz version 12.x
```

---

# Ejecutar el proyecto

```bash
python main.py
```

---

# Estructura del proyecto

```text
FTree/
│
├── main.py
├── analizador.py
├── derivacion.py
├── arbol.py
├── ast_modulo.py
│
├── arbol.png
├── ast.png
│
└── icono.ico
```

---

# Ejemplo de gramática

```text
E -> E '+' T | T
T -> T '*' F | F
F -> '(' E ')' | 'a' | 'b'
```

Cadena:

```text
(a + b) * a
```

---

# Funcionalidades principales

## Derivación izquierda

Genera paso a paso la expansión desde el símbolo inicial utilizando siempre el no terminal más a la izquierda.

---

## Derivación derecha

Genera la derivación utilizando el no terminal más a la derecha.

---

## Árbol sintáctico

Representación visual completa del proceso de derivación.

---

## AST (Abstract Syntax Tree)

Versión simplificada del árbol sintáctico eliminando nodos redundantes.

---

# Compilar a EXE

Instalar PyInstaller:

```bash
pip install pyinstaller
```

---

## Generar ejecutable

```bash
pyinstaller --onefile --windowed --icon=icono.ico main.py
```

---

# Resultado

El ejecutable se generará en:

```text
dist/main.exe
```

---

# Autor

Proyecto académico desarrollado para el análisis de gramáticas libres de contexto y construcción de árboles sintácticos.

---

# Capturas

Aquí puedes agregar imágenes del programa:

```md
![Interfaz](imagenes/interfaz.png)

![AST](imagenes/ast.png)
```

---

# Licencia

Uso académico y educativo.
