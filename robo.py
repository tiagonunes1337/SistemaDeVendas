try:
    import google.genai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    print("Aviso: Biblioteca google-genai não instalada. Análise IA será pulada.")

import mysql.connector
import time

# Configure a API do Gemini
GEMINI_API_KEY = "...."
GEMINI_MODEL = "gemini-2.0-flash"

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
        return "Análise IA não disponível - biblioteca google-genai não instalada."
    if not GEMINI_API_KEY:
        return "Análise IA não disponível - chave Gemini não configurada."
    
    try:
        # Chamar API do Gemini usando google-genai com retry para quota exceeded
        max_retries = 3
        for attempt in range(max_retries):
            try:
                client = genai.Client(api_key=GEMINI_API_KEY)
                response = client.models.generate_content(
                    model=GEMINI_MODEL,
                    contents=prompt
                )
                return getattr(response, 'text', str(response))
            except Exception as api_error:
                error_str = str(api_error)
                if "RESOURCE_EXHAUSTED" in error_str or "429" in error_str:
                    if attempt < max_retries - 1:
                        wait_time = 2 ** attempt  # Exponential backoff: 1s, 2s, 4s
                        print(f"Quota excedida. Tentando novamente em {wait_time} segundos... (Tentativa {attempt + 1}/{max_retries})")
                        time.sleep(wait_time)
                        continue
                    else:
                        return f"Erro: Limite de quota da API Gemini excedido. Considere fazer upgrade do plano gratuito ou aguarde o reset diário. Detalhes: {api_error}"
                else:
                    # Outros erros, não retry
                    return f"Erro ao consultar IA: {api_error}"
        
        return "Falha após múltiplas tentativas de consulta à IA."
        
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