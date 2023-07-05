from PyQt6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, \
    QRect, QSize, QTime, QUrl, Qt
from PyQt6.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, \
    QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform
from PyQt6.QtWidgets import QAbstractButton, QApplication, QDialog, QDialogButtonBox, \
    QLabel, QSizePolicy, QWidget

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(349, 159)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(110, 90, 191, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 30, 221, 41))

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Alerta Eliminar", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u00bfDesea eliminar la reserva seleccionada?", None))
    # retranslateUi

