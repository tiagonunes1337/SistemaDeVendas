try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    print("Aviso: Biblioteca google-generativeai não instalada. Análise IA será pulada.")

import mysql.connector

# Configure a API do Gemini
if GEMINI_AVAILABLE:
    genai.configure(api_key="AIzaSyBlWMneqX5YZIGn_rHszH0xkwfFsY2-c0w")

def obter_produtos():
    """
    Obtém a lista de produtos do banco de dados com tratamento de erros.
    
    Returns:
        list: Lista de dicionários com produtos ou None se erro
    """
    try:
        conexao = mysql.connector.connect(
            host='127.0.0.1',
            user='dev',
            password='1234',
            database='cadastro_produtos'
        )
        
        cursor = conexao.cursor()
        cursor.execute('SELECT idProduto, produto, preco, estoque FROM produtos')
        resultado = cursor.fetchall()
        cursor.close()
        conexao.close()
        
        # Converter para lista de dicionários
        produtos = []
        for row in resultado:
            produto = {
                'id': row[0],
                'nome': row[1],
                'preco': float(row[2]),
                'estoque': int(row[3])
            }
            produtos.append(produto)
        
        return produtos
        
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao banco de dados: {erro}")
        return None
    except Exception as erro:
        print(f"Erro inesperado: {erro}")
        return None

def avaliar_estoque(produtos):
    """
    Avalia estoque e valores usando a API do Gemini
    
    Args:
        produtos: lista de dicionários com produtos
    """
    
    if not produtos:
        return "Nenhum produto encontrado para análise."
    
    # Formatar dados para análise
    dados_estoque = "\n".join([
        f"- {p['nome']}: Estoque={p['estoque']}, Preço=R${p['preco']:.2f}"
        for p in produtos
    ])
    
    prompt = f"""
    Analise os seguintes dados de produtos e identifique possíveis problemas:
    
    {dados_estoque}
    
    Verificar:
    1. Valores inconsistentes (preços muito altos ou baixos)
    2. Quantidades suspeitas (negativas ou excessivamente altas)
    3. Possíveis erros de entrada
    4. Alertas de baixo estoque (menos de 10 unidades)
    5. Sugestões de preços baseados no mercado
    
    Responda de forma estruturada com os problemas encontrados e recomendações.
    """
    
    if not GEMINI_AVAILABLE:
        return "Análise IA não disponível - biblioteca google-generativeai não instalada."
    
    try:
        # Chamar API do Gemini
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        
        return response.text
        
    except Exception as erro:
        return f"Erro ao consultar IA: {erro}"

# Exemplo de uso
if __name__ == "__main__":
    print("Obtendo produtos do banco de dados...")
    produtos = obter_produtos()
    
    if produtos:
        print(f"Encontrados {len(produtos)} produtos.")
        resultado = avaliar_estoque(produtos)
        print("\nAnálise do Estoque:")
        print(resultado)
    else:
        print("Falha ao obter produtos.")