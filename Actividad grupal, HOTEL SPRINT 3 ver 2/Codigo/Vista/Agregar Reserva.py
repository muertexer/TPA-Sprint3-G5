import sys
from PyQt6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, \
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
from PyQt6.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, \
    QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform
from PyQt6.QtWidgets import QApplication, QComboBox, QHBoxLayout, QLabel, QLineEdit, QPushButton, \
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget, QMainWindow, QMessageBox

class formAgregarReserva(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(820, 700)
        font = QFont()
        font.setStyleStrategy(QFont.StyleStrategy.PreferAntialias)
        Form.setFont(font)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(70, 40, 520, 441))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox_4 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout.addWidget(self.comboBox_4)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.lineEdit_2 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_5.addWidget(self.lineEdit_2)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.comboBox_5 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.horizontalLayout_7.addWidget(self.comboBox_5)

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.comboBox_3 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_3.addWidget(self.comboBox_3)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.comboBox_2 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_4.addWidget(self.comboBox_2)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.comboBox = QComboBox(self.verticalLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_6.addWidget(self.lineEdit)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.textEdit = QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 120))

        self.verticalLayout.addWidget(self.textEdit)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(470, 490, 111, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Agregar Reserva", None))
        self.label.setText(QCoreApplication.translate("Form", u"Tipo de reserva", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("Form", u"Normal", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("Form", u"Evento", None))
        self.comboBox_4.currentIndexChanged.connect(self.mostrarModalidad)

        self.label_6.setText(QCoreApplication.translate("Form", u"Cliente", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Mesas", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("Form", u"Para dos", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("Form", u"Para tres", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("Form", u"Para cinco", None))

        self.label_2.setText(
            QCoreApplication.translate("Form", u"Modalidad de reserva", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Form", u"Abierta", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Form", u"Semi-Cerrada", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Form", u"Cerrada", None))
        self.comboBox_3.hide()
        self.label_2.hide()

        self.label_3.setText(QCoreApplication.translate("Form", u"Plan de comida", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"Inicial", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Form", u"Intermedio", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Form", u"Avanzado", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"Plan de degustaci\u00f3n", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Locales", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Internacionales", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"Cocina Fusi\u00f3n", None))

        self.label_5.setText(QCoreApplication.translate("Form", u"Sectores a reservar", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"Sector 1, 2, 3 ...", None))
        self.textEdit.setHtml(QCoreApplication.translate("Form", u"Indicaciones del cliente", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Actualizar", None))
        self.pushButton.clicked.connect(self.Actualizar)


    # retranslateUi

    def Actualizar(self):

        # and self.comboBox_4.itemText(self.comboBox_4.currentIndex()) == True \
        # and self.comboBox_5.itemText(self.comboBox_5.currentIndex()) == True \
        # and self.comboBox_3.itemText(self.comboBox_3.currentIndex()) == True \
        # and self.comboBox_2.itemText(self.comboBox_2.currentIndex()) == True \
        # and self.comboBox.itemText(self.comboBox.currentIndex()) == True \

        if self.lineEdit_2.isModified() == True \
        and (self.comboBox_4.currentIndex() == 0 or self.comboBox_4.currentIndex() == 1) \
        and (self.comboBox_5.currentIndex() == 0 or self.comboBox_5.currentIndex() == 1 or self.comboBox_5.currentIndex() == 2 ) \
        and (self.comboBox_3.currentIndex() == 0 or self.comboBox_3.currentIndex() == 1 or self.comboBox_3.currentIndex() == 2 ) \
        and (self.comboBox_2.currentIndex() == 0 or self.comboBox_2.currentIndex() == 1 or self.comboBox_2.currentIndex() == 2 ) \
        and (self.comboBox.currentIndex() == 0 or self.comboBox.currentIndex() == 1 or self.comboBox.currentIndex() == 2 ) \
        and self.lineEdit.isModified() == True \
        and self.textEdit.textChanged() == True:
            # guardar
            # archivo = open("Dataset/DatosReserva.csv", "a")

            datos = f"{self.comboBox_4.itemText(self.comboBox_4.currentIndex())},{self.lineEdit_2.text()},{self.comboBox_5.itemText(self.comboBox_5.currentIndex())},{self.comboBox_3.itemText(self.comboBox_3.currentIndex())},{self.comboBox_2.itemText(self.comboBox_2.currentIndex())},{self.comboBox.itemText(self.comboBox.currentIndex())},{self.lineEdit.text()},{self.textEdit.toPlainText()}\n"
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
        self.comboBox_4.setCurrentIndex(0)  # T reserva
        self.lineEdit_2.setText("")         # Texto cliente
        self.comboBox_5.setCurrentIndex(0)  # Mesas
        self.comboBox_3.setCurrentIndex(0)  # M Reserva
        self.comboBox_2.setCurrentIndex(0)  # P Comida
        self.comboBox.setCurrentIndex(0)    # P Degustacion
        self.lineEdit.setText("Sector 1, 2, 3 ...")
        self.textEdit.setText("Indicaciones del cliente")


    def mostrarModalidad(self, index):
        if index == 0:
            self.comboBox_3.hide()
            self.label_2.hide()
        elif index == 1:
            self.comboBox_3.show()
            self.label_2.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = QMainWindow()
    vista = formAgregarReserva()
    vista.setupUi(ventana)
    ventana.show()
    sys.exit(app.exec())