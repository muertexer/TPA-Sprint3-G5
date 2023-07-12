import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from UIasPython.AgregarReserva import AgregarReserva

with open("reservaciones.csv", "w") as archivo:
    archivo.write("")
archivo.close()
# Vacia el archivo reservaciones.csv, para trabajar con datos nuevos siempre

class VentanaAddReserva(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear una instancia de la clase Ui_MainWindow
        self.ui = AgregarReserva()

        # Configurar la interfaz de usuario
        self.ui.setupUi(self)

        # Conectar UI con este archivo
        self.ui.comboBox_4.currentIndexChanged.connect(self.mostrarModalidad)
        self.ui.pushButton.clicked.connect(self.Reservar)
        self.ui.pushButton2.clicked.connect(self.Cerrar)
        self.ui.comboBox_3.hide()
        self.ui.label_2.hide()

    def Cerrar(self):
        self.close()
    def Reservar(self):
        self.ui.pushButton2.setText("Cerrar")
        # Escribir archivos
        archivo = open("reservaciones.csv", "a")


        if self.TipoModalidad() == False: # Revisa si el tipo de reserva es Normal o Evento
        # Hace esto SI es EVENTO
            if \
                    self.ui.lineEdit_2.isModified() == True \
                    and (self.ui.comboBox_4.currentIndex() == 0 or self.ui.comboBox_4.currentIndex() == 1) \
                    and (self.ui.comboBox_5.currentIndex() == 0 or self.ui.comboBox_5.currentIndex() == 1 or self.ui.comboBox_5.currentIndex() == 2) \
                    and (self.ui.comboBox_3.currentIndex() == 0 or self.ui.comboBox_3.currentIndex() == 1 or self.ui.comboBox_3.currentIndex() == 2) \
                    and (self.ui.comboBox_2.currentIndex() == 0 or self.ui.comboBox_2.currentIndex() == 1 or self.ui.comboBox_2.currentIndex() == 2) \
                    and (self.ui.comboBox.currentIndex() == 0 or self.ui.comboBox.currentIndex() == 1 or self.ui.comboBox.currentIndex() == 2) \
                    and self.ui.lineEdit.isModified() == True \
                    and self.ui.textEdit.toPlainText() != "":

                # Guardar Datos
                datos = f"{self.ui.comboBox_4.itemText(self.ui.comboBox_4.currentIndex())}¤ " \
                        f"{self.ui.lineEdit_2.text()}¤" \
                        f"{self.ui.comboBox_5.itemText(self.ui.comboBox_5.currentIndex())}¤" \
                        f"{self.ui.comboBox_3.itemText(self.ui.comboBox_3.currentIndex())}¤" \
                        f"{self.ui.comboBox_2.itemText(self.ui.comboBox_2.currentIndex())}¤" \
                        f"{self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())}¤" \
                        f"{self.ui.lineEdit.text()}¤" \
                        f"{self.ui.textEdit.toPlainText()}\n"
                # print(datos), es netamente para ver si los datos se guardaban correctamente
                archivo.write(datos)
                archivo.close()

                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Icon.Information)
                msg_box.setWindowTitle("Informacíon")
                msg_box.setText("Reserva guardada con exito")
                msg_box.exec()
            else:
                self.AlertaErrorBlank()
        # Hace esto si es NORMAL
        elif self.TipoModalidad() == True:
            if \
                self.ui.lineEdit_2.isModified() == True \
                and (self.ui.comboBox_4.currentIndex() == 0 or self.ui.comboBox_4.currentIndex() == 1) \
                and (self.ui.comboBox_5.currentIndex() == 0 or self.ui.comboBox_5.currentIndex() == 1 or self.ui.comboBox_5.currentIndex() == 2) \
                and (self.ui.comboBox_2.currentIndex() == 0 or self.ui.comboBox_2.currentIndex() == 1 or self.ui.comboBox_2.currentIndex() == 2) \
                and (self.ui.comboBox.currentIndex() == 0 or self.ui.comboBox.currentIndex() == 1 or self.ui.comboBox.currentIndex() == 2) \
                and self.ui.lineEdit.isModified() == True \
                and self.ui.textEdit.toPlainText() != "":

                # Guardar Datos
                datos = f"{self.ui.comboBox_4.itemText(self.ui.comboBox_4.currentIndex())}¤" \
                        f"{self.ui.lineEdit_2.text()}¤" \
                        f"{self.ui.comboBox_5.itemText(self.ui.comboBox_5.currentIndex())}¤" \
                        f"No Aplica¤"\
                        f"{self.ui.comboBox_2.itemText(self.ui.comboBox_2.currentIndex())}¤" \
                        f"{self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())}¤" \
                        f"{self.ui.lineEdit.text()}¤" \
                        f"{self.ui.textEdit.toPlainText()}\n"
                # print(datos), es netamente para ver si los datos se guardaban correctamente
                archivo.write(datos)
                archivo.close()

                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Icon.Information)
                msg_box.setWindowTitle("Informacíon")
                msg_box.setText("Reserva guardada con exito")
                msg_box.exec()
            else:
                self.AlertaErrorBlank()
        else:
            self.AlertaErrorDesconocido()


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


    def TipoModalidad(self):
        index = self.ui.comboBox_4.currentIndex()
        if index == 0:
            return True
        elif index == 1:
            return False

    def AlertaErrorBlank(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle("Error")
        msg_box.setText("No puede haber campos vacíos")
        msg_box.exec()

    def AlertaErrorDesconocido(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle("Error Critico")
        msg_box.setText("Error desconocido, contacte al soporte")
        msg_box.exec()


