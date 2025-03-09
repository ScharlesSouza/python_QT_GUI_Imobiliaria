from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5 import QtWidgets
import sys

def on_clicked():
    print('Pressionado')

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    
    window.setGeometry(200,100,300,300)
    window.setWindowTitle('Minha primeira janela')
    
    text = QLabel(window)
    text.setText('Este é o meu primeiro campo de texto')
    text.move(50,50)
    
    btn1 = QtWidgets.QPushButton(window)
    btn1.setText('Clique aqui!')
    btn1.clicked.connect(on_clicked)
    btn1.move(100,150)
    
    
    window.show()    
    sys.exit(app.exec())


#print(sys.argv)

main()