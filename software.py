from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector

conexao = mysql.connector.connect(
    host='127.0.0.1',
    user='dev',
    password='1234',
    database='cadastro_produtos'
)

def inserir():
    try:
        produto = formulario.txtProduto.text()
        preco_texto = formulario.txtPreco.text().replace(',', '.')
        estoque = formulario.txtEstoque.text()

        # Validação básica
        if not produto or not preco_texto:
            QMessageBox.warning(formulario, "Erro", "Preencha os campos obrigatórios!")
            return

        preco = float(preco_texto)

        cursor = conexao.cursor()
        comando_SQL = 'INSERT INTO produtos (produto, preco, estoque) VALUES (%s, %s, %s)'
        cursor.execute(comando_SQL, (produto, preco, estoque))
        conexao.commit()
        cursor.close() # Sempre feche o cursor

        formulario.txtProduto.clear()
        formulario.txtPreco.clear()
        formulario.txtEstoque.clear()
        formulario.lblConfirmacao.setText('Produto cadastrado com sucesso!')
        
    except ValueError:
        QMessageBox.critical(formulario, "Erro", "Preço deve ser um número válido!")
    except mysql.connector.Error as erro:
        QMessageBox.critical(formulario, "Erro no Banco", f"Falha ao inserir: {erro}")

    

def listar():
    global relatorio
    relatorio = uic.loadUi('relatoriobettersmart.ui')
    carregar_tabela()
    relatorio.btnAlterar.clicked.connect(editar)
    relatorio.btnApagar.clicked.connect(excluir)
    relatorio.btnRetornar.clicked.connect(relatorio.close)
    relatorio.show()

def carregar_tabela():
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM produtos')
    resultado = cursor.fetchall()

    relatorio.tableWidget.setRowCount(0)
    for row_number, row_data in enumerate(resultado):
        relatorio.tableWidget.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            item = QtWidgets.QTableWidgetItem(str(data))
            relatorio.tableWidget.setItem(row_number, column_number, item)

def editar():
    global alterar_form
    linha_selecionada = relatorio.tableWidget.currentRow()
    if linha_selecionada == -1:
        return  # nenhuma linha selecionada

    idProduto = relatorio.tableWidget.item(linha_selecionada, 0).text()
    produto = relatorio.tableWidget.item(linha_selecionada, 1).text()
    preco = relatorio.tableWidget.item(linha_selecionada, 2).text()
    estoque = relatorio.tableWidget.item(linha_selecionada, 3).text()

    alterar_form = uic.loadUi('editar.ui')
    alterar_form.txtAlterarProduto.setText(produto)
    alterar_form.txtAlterarPreco.setText(preco)
    alterar_form.txtAlterarEstoque.setText(estoque)
    alterar_form.btnConfirmar.clicked.connect(lambda: atualizar(idProduto))
    alterar_form.show()

def atualizar(idProduto):
    produto = alterar_form.txtAlterarProduto.text()
    preco = alterar_form.txtAlterarPreco.text()
    estoque = alterar_form.txtAlterarEstoque.text()

    cursor = conexao.cursor()
    comando_SQL = 'UPDATE produtos SET produto = %s, preco = %s, estoque = %s WHERE idProduto = %s'
    cursor.execute(comando_SQL, (produto, preco, estoque, idProduto))
    conexao.commit()

    QMessageBox.information(alterar_form, "Sucesso", "Produto atualizado com sucesso!")
    alterar_form.close()
    carregar_tabela()
    


def excluir():
    linha_selecionada = relatorio.tableWidget.currentRow()
    if linha_selecionada == -1:
        return

    idProduto = relatorio.tableWidget.item(linha_selecionada, 0).text()

    cursor = conexao.cursor()
    comando_SQL = 'DELETE FROM produtos WHERE idProduto = %s'
    cursor.execute(comando_SQL, (idProduto,))
    conexao.commit()

    QMessageBox.information(relatorio, "Sucesso", "Produto excluído com sucesso!")
    carregar_tabela()

app = QtWidgets.QApplication([])

formulario = uic.loadUi('bettersmart.ui')
formulario.btnCadastrar.clicked.connect(inserir)
formulario.btnRelatorio.clicked.connect(listar)
formulario.show()

app.exec_()