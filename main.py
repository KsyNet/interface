import sys
import os # Отсюда нам понадобятся методы для отображения содержимого директорий
from PyQt5 import QtWidgets
import desing


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

class ExampleApp (QtWidgets.QMainWindow, desing.Ui_MainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self) #Инициализация дизайна
        self.btnBrowseFolder.clicked.connect(self.browse_folder)

    def browse_folder(self):
        self.listWidget.clear() #На случай, если в списке уже есть элементы
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")

        if directory: # не продолжать выполнение, если пользователь не выбрал директорию
            for file_name in os.listdir(directory): # для каждого файла в директории
                self.listWidget.addItem(file_name) # добавить файл в listWidget

if __name__ == '__main__': # Если мы запускаем файл напрямую, а не импортируем
    main() # то запускаем функцию main()

