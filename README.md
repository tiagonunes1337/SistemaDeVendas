# Sistema de Vendas

Um sistema simples de gerenciamento de vendas desenvolvido em Python utilizando PyQt5 para a interface gráfica e MySQL para o banco de dados.

## Funcionalidades

- **Cadastrar Produtos**: Adicione novos produtos com nome, preço e quantidade em estoque.
- **Visualizar Relatório**: Liste todos os produtos cadastrados em uma tabela.
- **Editar Produtos**: Atualize as informações de produtos existentes.
- **Excluir Produtos**: Remova produtos do banco de dados.
- **Confirmações**: Mensagens de confirmação para operações de atualização e exclusão.

## Requisitos

- Python 3.x
- PyQt5
- MySQL Connector/Python
- Servidor MySQL (local ou remoto)

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/tiagonunes1337/SistemaDeVendas.git
   cd SistemaDeVendas
   ```

2. **Instale as dependências**:
   ```bash
   pip install PyQt5 mysql-connector-python
   ```

3. **Configure o banco de dados**:
   - Certifique-se de que o MySQL está instalado e rodando.
   - Execute o script `produtos.sql` para criar o banco de dados e a tabela:
     ```sql
     source produtos.sql;
     ```
   - Atualize as credenciais de conexão no arquivo `software.py` se necessário (padrão: host='127.0.0.1', user='dev', password='1234', database='cadastro_produtos').

## Como Usar

1. Execute o aplicativo:
   ```bash
   python software.py
   ```

2. Na interface principal:
   - Insira os dados do produto nos campos de texto.
   - Clique em "Cadastrar" para adicionar o produto.
   - Clique em "Relatório" para visualizar todos os produtos.
   - Na janela de relatório, selecione um produto e clique em "Alterar" para editar ou "Apagar" para excluir.
   - Use "Retornar" para voltar à tela principal.

## Estrutura do Projeto

- `software.py`: Código principal da aplicação.
- `bettersmart.ui`: Interface principal (formulário de cadastro).
- `relatoriobettersmart.ui`: Interface do relatório (tabela de produtos).
- `editar.ui`: Interface de edição de produtos.
- `produtos.sql`: Script SQL para criação do banco de dados.

## Plano Futuro

- **Integração com IA (Gemini)**: Implementar funcionalidade para buscar valores de mercado usando a API do Google Gemini, permitindo sugestões de preços baseados em dados do mercado.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.