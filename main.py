from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTextEdit, QLabel, QCheckBox, QScrollArea, QFileDialog
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import shutil
import os

from analizador import analizar_entrada
from derivacion import derivacion_izquierda, derivacion_derecha
from arbol import arbol_a_imagen, arbol_a_imagen_ast
from ast_modulo import construir_ast


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FTree")

        # ESTILO
        self.setStyleSheet("""
            QWidget {
                background-color: #0f1117;
                color: white;
                font-family: Consolas;
                font-size: 13px;
            }

            QTextEdit {
                background-color: #1a1d26;
                border: 1px solid #2c313c;
                border-radius: 8px;
                padding: 6px;
            }

            QPushButton {
                background-color: #2979ff;
                border-radius: 8px;
                padding: 8px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #5393ff;
            }

            QPushButton:pressed {
                background-color: #1c54b2;
            }

            QCheckBox::indicator:checked {
                background-color: #2979ff;
            }
        """)

        self.layout_principal = QHBoxLayout()

        # PANEL IZQUIERDO
        self.panel_izq = QVBoxLayout()

        self.input_gramatica = QTextEdit()
        self.input_gramatica.setPlaceholderText("Gramatica: E -> E '+' T | T")

        self.input_cadena = QTextEdit()
        self.input_cadena.setPlaceholderText("Cadena: a + b")

        self.btn_izq = QPushButton("Derivación Izquierda")
        self.btn_der = QPushButton("Derivación Derecha")

        self.btn_izq.clicked.connect(lambda: self.ejecutar("izquierda"))
        self.btn_der.clicked.connect(lambda: self.ejecutar("derecha"))

        self.check_ast = QCheckBox("Mostrar AST")

        self.panel_izq.addWidget(QLabel("Gramatica"))
        self.panel_izq.addWidget(self.input_gramatica)
        self.panel_izq.addWidget(QLabel("Cadena"))
        self.panel_izq.addWidget(self.input_cadena)
        self.panel_izq.addWidget(self.btn_izq)
        self.panel_izq.addWidget(self.btn_der)
        self.panel_izq.addWidget(self.check_ast)

        # PANEL DERECHO
        self.panel_der = QVBoxLayout()

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)

        self.contenedor = QWidget()
        self.layout_contenedor = QVBoxLayout(self.contenedor)

        self.resultado = QLabel("Resultado:")
        self.resultado.setTextFormat(1)
        self.resultado.setWordWrap(True)

        self.imagen = QLabel()
        self.imagen.setAlignment(Qt.AlignCenter)

        self.imagen_ast = QLabel()
        self.imagen_ast.setAlignment(Qt.AlignCenter)

        self.btn_descargar = QPushButton("Descargar imágenes")
        self.btn_descargar.clicked.connect(self.descargar_imagenes)

        self.layout_contenedor.addWidget(self.resultado)
        self.layout_contenedor.addWidget(QLabel("Arbol"))
        self.layout_contenedor.addWidget(self.imagen)
        self.layout_contenedor.addWidget(QLabel("AST"))
        self.layout_contenedor.addWidget(self.imagen_ast)
        self.layout_contenedor.addWidget(self.btn_descargar)

        self.scroll.setWidget(self.contenedor)
        self.panel_der.addWidget(self.scroll)

        self.layout_principal.addLayout(self.panel_izq, 1)
        self.layout_principal.addLayout(self.panel_der, 2)

        self.setLayout(self.layout_principal)

    def formatear_derivacion(self, pasos):
        if not pasos:
            return "Sin derivación"

        html = "<b>Derivación:</b><br><br>"
        html += "<span style='font-family:consolas; font-size:14px'>"

        html += "<br>".join(pasos)

        html += "</span>"
        return html

    def mostrar_imagen(self, ruta, label):
        pixmap = QPixmap(ruta)
        if not pixmap.isNull():
            ancho = self.scroll.viewport().width() - 40
            label.setPixmap(pixmap.scaled(
                ancho,
                800,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            ))

    def descargar_imagenes(self):
        carpeta = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta")

        if not carpeta:
            return

        try:
            if os.path.exists("arbol.png"):
                shutil.copy("arbol.png", os.path.join(carpeta, "arbol.png"))

            if os.path.exists("ast.png"):
                shutil.copy("ast.png", os.path.join(carpeta, "ast.png"))

            self.resultado.setText(self.resultado.text() + "<br><b>Imágenes guardadas</b>")

        except Exception as e:
            self.resultado.setText(str(e))

    def ejecutar(self, modo):
        try:
            g = self.input_gramatica.toPlainText()
            c = self.input_cadena.toPlainText()

            arboles = analizar_entrada(g, c)

            if not arboles:
                self.resultado.setText("Expresión no válida")
                self.imagen.clear()
                self.imagen_ast.clear()
                return

            arbol = arboles[0]

            arbol_a_imagen(arbol, "arbol.png")
            self.mostrar_imagen("arbol.png", self.imagen)

            if modo == "izquierda":
                pasos = derivacion_izquierda(arbol)
                titulo = "Izquierda"
            else:
                pasos = derivacion_derecha(arbol)
                titulo = "Derecha"

            salida = f"<b>Expresión válida</b><br><br><b>Derivación {titulo}:</b><br>"
            salida += self.formatear_derivacion(pasos)

            if self.check_ast.isChecked():
                ast = construir_ast(arbol)
                arbol_a_imagen_ast(ast, "ast.png")
                self.mostrar_imagen("ast.png", self.imagen_ast)
            else:
                self.imagen_ast.clear()

            self.resultado.setText(salida)

        except Exception as e:
            self.resultado.setText(str(e))


app = QApplication([])
ventana = App()
ventana.resize(1200, 700)
ventana.show()
app.exec()