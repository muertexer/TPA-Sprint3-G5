from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text_edit1 = QTextEdit(self)
        self.text_edit2 = QTextEdit(self)
        self.text_edit3 = QTextEdit(self)
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit1)
        layout.addWidget(self.text_edit2)
        layout.addWidget(self.text_edit3)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.text_changed = False
        self.text_edit1.textChanged.connect(self.on_text_changed)
        self.text_edit2.textChanged.connect(self.on_text_changed)
        self.text_edit3.textChanged.connect(self.on_text_changed)

    def on_text_changed(self):
        text_edit = self.sender()
        if text_edit is not None:
            if text_edit == self.text_edit1:
                print("Text edit 1 changed:", text_edit.toPlainText())
            elif text_edit == self.text_edit2:
                print("Text edit 2 changed:", text_edit.toPlainText())
            elif text_edit == self.text_edit3:
                print("Text edit 3 changed:", text_edit.toPlainText())

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()