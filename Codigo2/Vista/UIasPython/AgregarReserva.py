# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AgregarReservaCGzvSA.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class AgregarReserva(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(790, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(450, 490, 111, 31))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(50, 40, 520, 441))
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

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Agregar Reserva", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Reservar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tipo de reserva", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Evento", None))



        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Mesas", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"Para dos", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"Para tres", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"Para cinco", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Modalidad de reserva", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Abierta", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Semi-Cerrada", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Cerrada", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Plan de comida", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Inicial", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Intermedio", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Avanzado", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Plan de degustaci\u00f3n", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Locales", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Internacionales", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cocina Fusi\u00f3n", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Sectores a reservar", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Sector 1, 2, 3 ...", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"Indicaciones del cliente", None))
    # retranslateUi

