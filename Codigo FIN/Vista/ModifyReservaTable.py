import csv
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from UIasPython.ModificarReserva import TablaModificarReserva
import EditReserva
import AddReserva
class VentanaModfyReserva(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear una instancia de la clase Ui_MainWindow
        self.uiTabla = TablaModificarReserva()
        self.EditRes = EditReserva.VentanaEditReserva
        self.AddRES2 = AddReserva.VentanaAddReserva

        # Configurar la interfaz de usuario
        self.uiTabla.setupUi(self)

        # Conectar UI con este archivo
        self.uiTabla.tableWidget.cellClicked.connect(self.SelectedCell)
        self.uiTabla.pushButton.clicked.connect(self.cerrar)

    def cerrar(self):
        self.close()
    def IniciarAppend(self):
        # Abre el archivo CSV y lee el contenido
        with open("reservaciones.csv", 'r') as File:
            contenido = File.read()
        File.close()
            # Verifica si el contenido del archivo es una cadena vacía
        if not contenido:
            return True
        else:
            self.AppdendLinesInTable("reservaciones.csv")


    def AppdendLinesInTable(self, File):
        # Abre el archivo CSV y lee todas las líneas
        with open(File, 'r') as archivo_csv:
            lineas = archivo_csv.readlines()

        # Configura el número de filas y columnas en el QTableWidget
        self.uiTabla.tableWidget.setRowCount(len(lineas))
        self.uiTabla.tableWidget.setColumnCount(len(lineas[0].split('¤')))

        # Inserta las líneas en el QTableWidget
        for fila, linea in enumerate(lineas):
            valores = linea.strip().split('¤')
            for columna, valor in enumerate(valores):
                item = QTableWidgetItem(valor)
                self.uiTabla.tableWidget.setItem(fila, columna, item)



    # Definir la ranura para manejar la señal "cellClicked"
    def SelectedCell(self):
        celdas_seleccionadas = self.uiTabla.tableWidget.selectedItems()

        filas_seleccionadas = set()
        for celda in celdas_seleccionadas:
            fila = celda.row()
            filas_seleccionadas.add(fila)

        for fila in filas_seleccionadas:
            valores_fila = []
            for columna in range(self.uiTabla.tableWidget.columnCount()):
                celda = self.uiTabla.tableWidget.item(fila, columna)
                if celda is not None:
                    valores_fila.append(celda.text())
            valor_fila = '¤'.join(valores_fila)

            row = fila
            self.AbrirEdit = EditReserva.VentanaEditReserva(valor_fila,row)
            self.AbrirAdd = AddReserva.VentanaAddReserva()

            # Encontrar que hay en los elementos de la tabla por modificar
            partes = valor_fila.split("¤")

            TReserva = partes[0]
            Cliente = partes[1]
            Mesas = partes[2]
            MoReserva = partes[3]
            PComida = partes[4]
            PDegustacion = partes[5]
            Sectores = partes[6]
            Indicaciones = partes[7]

            self.AbrirEdit.uiEditar.comboBox_4.setCurrentIndex(self.AbrirEdit.uiEditar.comboBox_4.findText(TReserva))
            self.AbrirEdit.uiEditar.lineEdit_2.setText(Cliente)
            self.AbrirEdit.uiEditar.comboBox_5.setCurrentIndex(self.AbrirEdit.uiEditar.comboBox_5.findText(Mesas))
            self.AbrirEdit.uiEditar.comboBox_3.setCurrentIndex(self.AbrirEdit.uiEditar.comboBox_3.findText(MoReserva))
            self.AbrirEdit.uiEditar.comboBox_2.setCurrentIndex(self.AbrirEdit.uiEditar.comboBox_2.findText(PComida))
            self.AbrirEdit.uiEditar.comboBox.setCurrentIndex(self.AbrirEdit.uiEditar.comboBox.findText(PDegustacion))
            self.AbrirEdit.uiEditar.lineEdit.setText(Sectores)
            self.AbrirEdit.uiEditar.textEdit.setText(Indicaciones)

            self.AbrirEdit.show()


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



