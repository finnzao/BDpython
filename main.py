from PyQt5 import uic
from PyQt5 import QtWidgets
import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='crud',
)
cursor = conexao.cursor()


def ready():
    valor = interface.lineEdit_1.text()
    quantidade = interface.lineEdit_2.text()
    material = interface.lineEdit_3.text()
    bloco = ""
    if interface.radioButton_2.isChecked():
        print("Bloco 1")
        bloco = "Bloco 1"
    elif interface.radioButton_3.isChecked():
        print("Bloco 2")
        bloco = "Bloco 2"
    elif interface.radioButton_4.isChecked():
        bloco = "Bloco 3"
        print("Bloco 3")

    print("Material:", material)
    print("Quantidade:", quantidade)
    print("Valor:", valor)
    mySQLCursor = conexao.cursor()
    comando = "insert into produtos(material, quantidade, preco, bloco) VALUES (%s,%s,%s,%s)"
    dados = (str(material), str(quantidade), str(valor), bloco)  # str : converte variavel em string
    mySQLCursor.execute(comando, dados)
    conexao.commit()
    interface.lineEdit_1.setText("")
    interface.lineEdit_2.setText("")
    interface.lineEdit_3.setText("")
    interface.radioButton_2.setCheckable(False)
    interface.radioButton_3.setCheckable(False)
    interface.radioButton_4.setCheckable(False)


def window():
    second_window.show()
    comando = f'select * from produtos'

    cursor.execute(comando)

    resultado = cursor.fetchall()  # ler o banco de dados

    second_window.tableWidget.setColumnCount(5)  # qunatidade de colunas da tabela
    second_window.tableWidget.setRowCount(len(resultado))  # criando linha da tabela

    for i in range(0, len(resultado)):
        for j in range(0, 5):
            second_window.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))


app = QtWidgets.QApplication([])
second_window = uic.loadUi("window.ui")
interface = uic.loadUi("IAcadastro.ui")
interface.pushButton.clicked.connect(ready)
interface.pushButton_2.clicked.connect(window)

interface.show()
app.exec()
