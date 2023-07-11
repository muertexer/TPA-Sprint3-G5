import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from UIasPython.ReservaRestauranteInicio import ReservaRestaurante

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear una instancia de la clase Ui_MainWindow
        self.ui = ReservaRestaurante()

        # Configurar la interfaz de usuario
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())