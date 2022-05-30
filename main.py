from PyQt5 import uic
from PyQt5 import QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='crud',
)
cursor = conexao.cursor()


def print_page():
    comando = "SELECT * FROM produtos"
    cursor.execute(comando)
    dados = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("cadastro_produtos.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200, 800, "Produtos cadastros:")
    pdf.setFont("Times-Bold", 18)

    pdf.drawString(10, 750, "ID")
    pdf.drawString(110, 750, "Material")
    pdf.drawString(210, 750, "Valor")
    pdf.drawString(310, 750, "Quantidade")
    pdf.drawString(410, 750, "Bloco")
    for i in range(0, len(dados)):
        y += 50
        pdf.drawString(10, 750 - y, str(dados[i][0]))
        pdf.drawString(110, 750 - y, str(dados[i][1]))
        pdf.drawString(210, 750 - y, str(dados[i][2]))
        pdf.drawString(310, 750 - y, str(dados[i][3]))
        pdf.drawString(410, 750 - y, str(dados[i][4]))

    pdf.save()
    print("PDF SAVE.")


def update():
    row = second_window.tableWidget.currentRow()
    column = second_window.tableWidget.currentColumn()
    print(column)
    cursor.execute("SELECT id FROM produtos")
    dados = cursor.fetchall()
    value_id = dados[row][0]
    print(value_id)


def delete():
    row = second_window.tableWidget.currentRow()
    second_window.tableWidget.removeRow(row)

    cursor.execute("SELECT id FROM produtos")
    dados = cursor.fetchall()

    value_id = dados[row][0]
    print(value_id)
    cursor.execute("DELETE FROM produtos WHERE id =" + str(value_id))


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
second_window.pushButton_print.clicked.connect(print_page)
second_window.pushButton_delete.clicked.connect(delete)
second_window.pushButton_update.clicked.connect(update)

interface.show()
app.exec()
