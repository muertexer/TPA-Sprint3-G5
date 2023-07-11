import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from UIasPython.AgregarReserva import AgregarReserva

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear una instancia de la clase Ui_MainWindow
        self.ui = AgregarReserva()

        # Configurar la interfaz de usuario
        self.ui.setupUi(self)

        # Conectar UI con estearchivo
        self.ui.comboBox_4.currentIndexChanged.connect(self.mostrarModalidad)
        self.ui.pushButton.clicked.connect(self.Reservar)
        self.ui.comboBox_3.hide()
        self.ui.label_2.hide()

    def Reservar(self):

        # and self.comboBox_4.itemText(self.comboBox_4.currentIndex()) == True \
        # and self.comboBox_5.itemText(self.comboBox_5.currentIndex()) == True \
        # and self.comboBox_3.itemText(self.comboBox_3.currentIndex()) == True \
        # and self.comboBox_2.itemText(self.comboBox_2.currentIndex()) == True \
        # and self.comboBox.itemText(self.comboBox.currentIndex()) == True \

        if self.ui.lineEdit_2.isModified() == True \
        and (self.ui.comboBox_4.currentIndex() == 0 or self.ui.comboBox_4.currentIndex() == 1) \
        and (self.ui.comboBox_5.currentIndex() == 0 or self.ui.comboBox_5.currentIndex() == 1 or self.ui.comboBox_5.currentIndex() == 2 ) \
        and (self.ui.comboBox_3.currentIndex() == 0 or self.ui.comboBox_3.currentIndex() == 1 or self.ui.comboBox_3.currentIndex() == 2 ) \
        and (self.ui.comboBox_2.currentIndex() == 0 or self.ui.comboBox_2.currentIndex() == 1 or self.ui.comboBox_2.currentIndex() == 2 ) \
        and (self.ui.comboBox.currentIndex() == 0 or self.ui.comboBox.currentIndex() == 1 or self.ui.comboBox.currentIndex() == 2 ) \
        and self.ui.lineEdit.isModified() == True \
        and self.ui.textEdit.textChanged() == True:
            # guardar
            # archivo = open("Dataset/DatosReserva.csv", "a")

            datos = f"{self.ui.comboBox_4.itemText(self.ui.comboBox_4.currentIndex())},{self.ui.lineEdit_2.text()},{self.ui.comboBox_5.itemText(self.ui.comboBox_5.currentIndex())},{self.ui.comboBox_3.itemText(self.ui.comboBox_3.currentIndex())},{self.ui.comboBox_2.itemText(self.ui.comboBox_2.currentIndex())},{self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())},{self.ui.lineEdit.text()},{self.ui.textEdit.toPlainText()}\n"
            print(datos)
            # archivo.write(datos)
            # archivo.close()
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("No puede haber campos vacíos")
            msg_box.exec()





        # dejar elementos por defecto:
        self.ui.comboBox_4.setCurrentIndex(0)  # T reserva
        self.ui.lineEdit_2.setText("")         # Texto cliente
        self.ui.comboBox_5.setCurrentIndex(0)  # Mesas
        self.ui.comboBox_3.setCurrentIndex(0)  # M Reserva
        self.ui.comboBox_2.setCurrentIndex(0)  # P Comida
        self.ui.comboBox.setCurrentIndex(0)    # P Degustacion
        self.ui.lineEdit.setText("Sector 1, 2, 3 ...")
        self.ui.textEdit.setText("Indicaciones del cliente")


    def mostrarModalidad(self, index):
        if index == 0:
            self.ui.comboBox_3.hide()
            self.ui.label_2.hide()
        elif index == 1:
            self.ui.comboBox_3.show()
            self.ui.label_2.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())