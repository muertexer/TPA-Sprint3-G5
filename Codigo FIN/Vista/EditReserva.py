import sys
import csv
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from UIasPython.EditarReserva import EditarReserva
import ModifyReservaTable
class VentanaEditReserva(QMainWindow):
    def __init__(self, valor_fila, row):
        super().__init__()

        self.valor_fila = valor_fila
        self.row = row
        # print(self.valor_fila)
        # Crear una instancia de la clase Ui_MainWindow
        self.uiEditar = EditarReserva()
        self.ModyResforEditor = ModifyReservaTable.VentanaModfyReserva()
        # Configurar la interfaz de usuario
        self.uiEditar.setupUi(self)
        self.uiEditar.pushButton2.clicked.connect(self.CerrarEditar)
        self.uiEditar.comboBox_4.currentIndexChanged.connect(self.mostrarModalidad)
        self.uiEditar.pushButton.clicked.connect(self.Actualizar)
        self.uiEditar.pushButton3.clicked.connect(self.eliminar)
    def Actualizar(self):
        self.uiEditar.pushButton2.setText("Cerrar")
        archivo = open("reservaciones.csv", "a")

        # Revisa si el tipo de reserva es Normal o Evento
        # Hace esto SI es EVENTO
        if self.TipoModalidad() == False \
            and self.uiEditar.lineEdit_2.isModified() == True \
            and (self.uiEditar.comboBox_4.currentIndex() == 0 or self.uiEditar.comboBox_4.currentIndex() == 1) \
            and (self.uiEditar.comboBox_5.currentIndex() == 0 or self.uiEditar.comboBox_5.currentIndex() == 1 or self.uiEditar.comboBox_5.currentIndex() == 2) \
            and (self.uiEditar.comboBox_3.currentIndex() == 0 or self.uiEditar.comboBox_3.currentIndex() == 1 or self.uiEditar.comboBox_3.currentIndex() == 2) \
            and (self.uiEditar.comboBox_2.currentIndex() == 0 or self.uiEditar.comboBox_2.currentIndex() == 1 or self.uiEditar.comboBox_2.currentIndex() == 2) \
            and (self.uiEditar.comboBox.currentIndex() == 0 or self.uiEditar.comboBox.currentIndex() == 1 or self.uiEditar.comboBox.currentIndex() == 2) \
            and self.uiEditar.lineEdit.isModified() == True \
            and self.uiEditar.textEdit.toPlainText() != "":

                # Guardar Datos
                datos = f"{self.uiEditar.comboBox_4.itemText(self.uiEditar.comboBox_4.currentIndex())}¤ " \
                        f"{self.uiEditar.lineEdit_2.text()}¤" \
                        f"{self.uiEditar.comboBox_5.itemText(self.uiEditar.comboBox_5.currentIndex())}¤" \
                        f"{self.uiEditar.comboBox_3.itemText(self.uiEditar.comboBox_3.currentIndex())}¤" \
                        f"{self.uiEditar.comboBox_2.itemText(self.uiEditar.comboBox_2.currentIndex())}¤" \
                        f"{self.uiEditar.comboBox.itemText(self.uiEditar.comboBox.currentIndex())}¤" \
                        f"{self.uiEditar.lineEdit.text()}¤" \
                        f"{self.uiEditar.textEdit.toPlainText()}\n"
                # print(datos), es netamente para ver si los datos se guardaban correctamente


                lineas_actualizadas = []
                with open("reservaciones.csv", 'r') as archivo_csv:
                    lector_csv = csv.reader(archivo_csv)
                    for indice, linea in enumerate(lector_csv, start=1):
                        if indice == self.row:
                            lineas_actualizadas.append(self.row)
                        else:
                            lineas_actualizadas.append(linea)

                with open("reservaciones.csv", 'w', newline='') as archivo_csv:
                    escritor_csv = csv.writer(archivo_csv)
                    escritor_csv.writerows(lineas_actualizadas)
                    archivo_csv.close()


                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Icon.Information)
                msg_box.setWindowTitle("Informacíon")
                msg_box.setText("Reserva guardada con exito")
                msg_box.exec()

        # Hace esto si es NORMAL
        elif self.TipoModalidad() == True \
            and self.uiEditar.lineEdit_2.isModified() == True \
            and (self.uiEditar.comboBox_4.currentIndex() == 0 or self.uiEditar.comboBox_4.currentIndex() == 1) \
            and (self.uiEditar.comboBox_5.currentIndex() == 0 or self.uiEditar.comboBox_5.currentIndex() == 1 or self.uiEditar.comboBox_5.currentIndex() == 2) \
            and (self.uiEditar.comboBox_2.currentIndex() == 0 or self.uiEditar.comboBox_2.currentIndex() == 1 or self.uiEditar.comboBox_2.currentIndex() == 2) \
            and (self.uiEditar.comboBox.currentIndex() == 0 or self.uiEditar.comboBox.currentIndex() == 1 or self.uiEditar.comboBox.currentIndex() == 2) \
            and self.uiEditar.lineEdit.isModified() == True \
            and self.uiEditar.textEdit.toPlainText() != "":

                # Guardar Datos
                datos = f"{self.uiEditar.comboBox_4.itemText(self.uiEditar.comboBox_4.currentIndex())}¤" \
                        f"{self.uiEditar.lineEdit_2.text()}¤" \
                        f"{self.uiEditar.comboBox_5.itemText(self.uiEditar.comboBox_5.currentIndex())}¤" \
                        f"No Aplica¤" \
                        f"{self.uiEditar.comboBox_2.itemText(self.uiEditar.comboBox_2.currentIndex())}¤" \
                        f"{self.uiEditar.comboBox.itemText(self.uiEditar.comboBox.currentIndex())}¤" \
                        f"{self.uiEditar.lineEdit.text()}¤" \
                        f"{self.uiEditar.textEdit.toPlainText()}\n"
                # print(datos), es netamente para ver si los datos se guardaban correctamente


                lineas_actualizadas = []
                with open("reservaciones.csv", 'r') as archivo_csv:
                    lector_csv = csv.reader(archivo_csv)
                    for indice, linea in enumerate(lector_csv, start=1):
                        if indice == self.row:
                            lineas_actualizadas.append(self.row)
                        else:
                            lineas_actualizadas.append(linea)

                with open("reservaciones.csv", 'w', newline='') as archivo_csv:
                    escritor_csv = csv.writer(archivo_csv)
                    escritor_csv.writerows(lineas_actualizadas)
                    archivo_csv.close()


                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Icon.Information)
                msg_box.setWindowTitle("Informacíon")
                msg_box.setText("Reserva guardada con exito")
                msg_box.exec()
        else:
            self.AlertaErrorDesconocido()

    def eliminar(self):
        self.uiEditar.pushButton2.setText("Cerrar")
        archivo_csv = "reservaciones.csv"
        lineas = []

        with open(archivo_csv, 'r') as archivo:
            lector_csv = csv.reader(archivo)
            lineas = list(lector_csv)

        linea_a_eliminar = self.row  # Índice de la línea que deseas eliminar

        del lineas[linea_a_eliminar]

        with open(archivo_csv, 'w', newline='') as archivo:
            escritor_csv = csv.writer(archivo)
            escritor_csv.writerows(lineas)
            archivo.close()

    def mostrarModalidad(self, index):
        if index == 0:
            self.uiEditar.comboBox_3.hide()
            self.uiEditar.label_2.hide()
        elif index == 1:
            self.uiEditar.comboBox_3.show()
            self.uiEditar.label_2.show()

    def TipoModalidad(self):
        index = self.uiEditar.comboBox_4.currentIndex()
        if index == 0:
            return True
        elif index == 1:
            return False

    def CerrarEditar(self):
        self.close()

    def AlertaErrorBlank(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle("Error")
        msg_box.setText("No puede haber campos vacíos")
        msg_box.exec()

    def AlertaErrorDesconocido(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle("Error")
        msg_box.setText("Error para actualizar debe haber cambios")
        msg_box.exec()



