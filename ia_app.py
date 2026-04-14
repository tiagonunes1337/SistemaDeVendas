from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import robo
from styles import DARK_STYLESHEET

def analisar_estoque():
    """
    Função chamada ao clicar no botão de análise
    """
    try:
        # Obter produtos
        formulario_ia.textResultado.clear()
        formulario_ia.textResultado.append("🔄 Obtendo produtos do banco de dados...")
        
        produtos = robo.obter_produtos()
        
        if not produtos:
            formulario_ia.textResultado.append("❌ Erro: Não foi possível obter produtos do banco.")
            return
        
        formulario_ia.textResultado.append(f"✅ Encontrados {len(produtos)} produtos.\n")
        
        # Analisar com IA
        formulario_ia.textResultado.append("🤖 Analisando com IA Gemini...")
        resultado = robo.avaliar_estoque(produtos)
        
        formulario_ia.textResultado.append("📊 Resultado da Análise:")
        formulario_ia.textResultado.append("-" * 50)
        formulario_ia.textResultado.append(resultado)
        
    except Exception as erro:
        QMessageBox.critical(formulario_ia, "Erro", f"Falha na análise: {erro}")
        formulario_ia.textResultado.append(f"❌ Erro: {erro}")

app = QtWidgets.QApplication([])
app.setStyle('Fusion')
app.setStyleSheet(DARK_STYLESHEET)

formulario_ia = uic.loadUi('IA.ui')
formulario_ia.btnAnalisar.clicked.connect(analisar_estoque)
formulario_ia.show()

app.exec_()