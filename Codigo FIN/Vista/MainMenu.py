import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from UIasPython.ReservaRestauranteInicio import ReservaRestaurante
import AddReserva
import ModifyReservaTable


class VistaMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear una instancia de la interfaz
        self.uiMenu = ReservaRestaurante() # UI Menu principal
        self.AddRes = AddReserva.VentanaAddReserva() # AddReserva.py
        self.ModRes = ModifyReservaTable.VentanaModfyReserva()  # ModifyreservaTable.py

        # Configurar la interfaz de usuario
        self.uiMenu.setupUi(self)

        #Conecciones a este archivo
        self.uiMenu.pushButton.clicked.connect(self.abrirAgregarReserva)
        self.uiMenu.pushButton_2.clicked.connect(self.abrirModificarReserva)
        self.uiMenu.pushButton_3.clicked.connect(self.AlertaErrorNoAplica)
    def abrirAgregarReserva(self):
        self.Abrir = AddReserva.VentanaAddReserva()
        self.Abrir.show()

    def abrirModificarReserva(self):
        self.Abrir = ModifyReservaTable.VentanaModfyReserva()
        self.Abrir.IniciarAppend()
        if self.Abrir.IniciarAppend() == True:
            return self.AlertaErrorNoAplica()
        self.Abrir.show()
    def AlertaErrorNoAplica(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle("Error")
        msg_box.setText("Ventana no disponible para su visualización")
        msg_box.exec()

    def AlertaErrorCsvBlank(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle("Error")
        msg_box.setText("No se han efectuado reservas")
        msg_box.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VistaMenu()
    window.show()
    sys.exit(app.exec())