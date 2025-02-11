import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox


def click():
    msg = QMessageBox()
    msg.setWindowTitle("Уведомление")
    msg.setText("Внимание! Нажми ещё раз!")
    msg.setIcon(QtWidgets.QMessageBox.Critical)
    result = msg.exec_()

def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(400, 400, 400, 300)
    win.setWindowTitle("GUI на Python")

    # Добавление lable
    label = QLabel(win)
    label.resize(300, 50)
    label.setText("Привет! Я будущий текст заголовка!")
    label.move(100, 100)

    # Добавление тестового поля
    textbox = QtWidgets.QLineEdit(win)
    textbox.move(100, 150)
    textbox.resize(180, 30)

    # Добавление кнопки
    button = QtWidgets.QPushButton(win)
    button.setText("Нажми меня!")
    button.move(100, 200)
    button.clicked.connect(click)

    win.show()
    sys.exit(app.exec_())
main()



