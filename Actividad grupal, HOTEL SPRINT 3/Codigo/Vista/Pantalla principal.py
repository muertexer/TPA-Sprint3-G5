from PyQt6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, \
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
from PyQt6.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, \
    QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform
from PyQt6.QtWidgets import QApplication, QFrame, QHBoxLayout, QLabel, QMainWindow, QPushButton, \
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(819, 602)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(40, 20, 141, 31))
        self.label.setOpenExternalLinks(False)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 50, 811, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(220, 80, 361, 61))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 150, 811, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(60, 210, 681, 321))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_6.addWidget(self.label_5)

        self.pushButton_7 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_6.addWidget(self.pushButton_7)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.pushButton_8 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout_4.addWidget(self.pushButton_8)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_5.addWidget(self.label_6)

        self.pushButton_9 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout_5.addWidget(self.pushButton_9)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_7 = QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.pushButton_4 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Reserva Restaurante", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"LOGO #inserte imagen", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar reserva", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Modificar reserva", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Confirmar disponibilidad", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Texto Info 1", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Info 1 BTN", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Texto Info 2", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Info 2 BTN", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Texto Info 3", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Info 3 BTN", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Texto Info 4", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Info 4 BTN", None))
    # retranslateUi

