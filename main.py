from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel
from PyQt5 import QtWidgets, QtCore, QtGui
import sys, random

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setGeometry(200,100,300,300)
        self.setWindowTitle('Minha primeira janela')
        
        self.setupUI()
    
    def setupUI(self):
        self.text = QLabel(self)
        self.text.setText('Este é o meu primeiro campo de texto')
        self.text.move(50,50)
        self.text.adjustSize()
        
        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setText('Alterar texto!')
        self.btn1.clicked.connect(self.on_clicked)
        self.btn1.move(100,150)
        
        self.radioButton = QtWidgets.QRadioButton(self)
        self.radioButton.setGeometry(QtCore.QRect(120,180,151,41))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName('radioButton')
        
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setGeometry(QtCore.QRect(180,180,151,41))
        self.checkBox.setObjectName('checkBox')
        
        
        #Botão para abri o Show Dialog
        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setText('Show Dialog')
        #self.btn2.clicked.connect(self.show_dialog)
        self.btn2.move(100,100)        
        self.btn2.clicked.connect(self.show_dialog)#Listen do clique do botão
        
    def on_clicked(self):
        self.text.setText('este texto foi alterado! Numero aleatorio: %d' %(random.randint(0,10)))
        self.text.adjustSize()#ajustar o label ao tamanho do texto
        #print('Pressionado')
        
        #Verificação do radioButton
        if self.radioButton.isChecked() == True:
            print('Radio marcado.')
        else:
            print('Radio desmarcado')
        #Verificação do checkBox
        if self.checkBox.isChecked() == True:
            print('checkBox marcado.')
        else:
            print('checkBox desmarcado')
        
    def show_dialog(self):
        dialog = QtWidgets.QMessageBox(self)
        dialog.setText('Meu primeiro dialog!')
        dialog.setWindowTitle('Meu primeiro dialog')
        dialog.setIcon(QtWidgets.QMessageBox.Information)#Icons = Critical, Warning, Information, Question
        
        dialog.setInformativeText('conteudo da informação')#mensagem no corpo do dialog
        dialog.setDetailedText('Informação detalhada.')#informação detalhada.
        dialog.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel|QMessageBox.Retry)#adicionando algun botões padrão do dialog
        dialog.buttonClicked.connect(self.dialog_clicked)#Listen do clique dos botoes do dialog.
        dialog.exec_()
        
    #Tratar o clique em botões do Dialog.    
    def dialog_clicked(self, dialog_button):
        print(dialog_button.text())

def main():
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    
    window.show()    
    sys.exit(app.exec())


'''
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
'''

#print(sys.argv)

main()