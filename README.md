# 💰 Sistema de Controle de Investimentos - GF Innovation

## 📋 Descrição do Projeto
Sistema completo para controle de investimentos desenvolvido como parte do processo seletivo da **GF Innovation**. A aplicação permite o gerenciamento de ativos financeiros com operações de **CRUD** (Create, Read, Update, Delete) através de uma interface intuitiva e uma **API RESTful** robusta.

---

## 🚀 Tecnologias Utilizadas

**Backend**
- Python com Flask  
- SQLAlchemy (ORM)  
- Flask-Migrate para migrações de banco  
- SQLite (banco de dados)  

**Frontend**
- HTML5 semântico  
- CSS3 com Bootstrap 5.3  
- JavaScript ES6+ (com Fetch API)  
- Design responsivo  

---

## ⚙️ Funcionalidades Implementadas

### ✅ Funcionalidades Obrigatórias
- Cadastro de investimentos (nome, tipo, valor, data)  
- Listagem completa de investimentos  
- Edição de investimentos existentes  
- Exclusão de investimentos  
- Validação de valor investido (> 0)  
- Validação de data (não pode ser futura)  
- Interface para todas as operações  

### ✅ Extras Implementados
- Validações detalhadas no frontend e backend  
- Mensagens de sucesso/erro para todas as operações  
- Interface responsiva com Bootstrap  
- Confirmação de exclusão  
- Código organizado em camadas (**Controller-Service-Repository**)  
- Documentação completa  

---

## 🏗️ Arquitetura do Sistema

**Backend (Padrão MVC)**

app/

├── __init__.py     
├── config.py          
├── extensions.py         
├── models.py             
├── controllers/         
│   └── investment_controller.py
├── services/           
│   └── investment_service.py
└── repositories/        
    └── investment_repository.py

**Frontend**

frontend/

├── index.html       
├── list.html             
├── script.js             
└── style.css             


---

## 📦 Instalação e Execução

### Pré-requisitos
- Python 3.8 ou superior  
- Navegador  

### Configuração do Backend

```bash
# Clone o repositório
git clone <url-do-repositorio>
cd investments-app/backend

# Crie e ative um ambiente virtual
python -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Configure o banco de dados
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Execute a aplicação
python run.py
```

## 💻 Servidor e Frontend

### Servidor Backend
Após executar o comando para rodar a aplicação Flask, o servidor estará ativo em:  
[http://localhost:5000](http://localhost:5000)

### Configuração do Frontend
1. Navegue até a pasta `frontend`:

```bash
# Na pasta frontend:
python -m http.server 8000
```

Acesse a aplicação:

Cadastro: http://localhost:8000/index.html

Listagem: http://localhost:8000/list.html


| Método | Endpoint          | Descrição                    | Exemplo de Body                                                                         |
| ------ | ----------------- | ---------------------------- | --------------------------------------------------------------------------------------- |
| GET    | /investments/     | Lista todos os investimentos | -                                                                                       |
| POST   | /investments/     | Cria um novo investimento    | `{"name": "Tesouro Direto", "type": "Título", "amount": 1500.00, "date": "2024-01-15"}` |
| PUT    | /investments/<id> | Atualiza um investimento     | `{"name": "Novo Nome", "amount": 2000.00}`                                              |
| DELETE | /investments/<id> | Exclui um investimento       | -                                                                                       |


# 🎯 Como Utilizar

## Cadastrar um Investimento
1. Acesse a página de cadastro.  
2. Preencha os campos:
   - **Nome**: Nome do investimento (ex: "Tesouro Direto IPCA 2026")  
   - **Tipo**: Tipo de investimento (Ação, Fundo ou Título)  
   - **Valor**: Valor investido (maior que 0)  
   - **Data**: Data do investimento (não pode ser futura)  
3. Clique em **"Cadastrar"**.

## Visualizar Investimentos
- Acesse a página de listagem.  
- Visualize todos os investimentos em formato de tabela.  
- Utilize os botões de ação para **editar** ou **excluir**.

## Editar um Investimento
1. Na listagem, clique no campo que deseja alterar.  
2. Modifique o valor.  
3. Clique no botão **💾** para salvar as alterações.

## Excluir um Investimento
1. Na listagem, clique no botão **🗑️** do investimento desejado.  
2. Confirme a exclusão no diálogo de confirmação.

---

# 🔧 Validações Implementadas

### Frontend
- Campos obrigatórios.  
- Valor numérico positivo.  
- Data no formato correto (YYYY-MM-DD).  
- Data não futura.

### Backend
- Tipos de investimento válidos (Ação, Fundo, Título).  
- Valor positivo (maior que 0).  
- Data não futura.  
- Formato de data correto.  
- Existência do registro para operações de update/delete.

---

# 📊 Estrutura de Dados

Tabela `Investment`:

| Campo  | Tipo        | Restrições     |
| ------ | ----------- | -------------- |
| id     | Integer     | Chave primária |
| name   | String(100) | Não nulo       |
| type   | String(50)  | Não nulo       |
| amount | Float       | Não nulo       |
| date   | Date        | Não nulo       |

---

# 🚀 Diferenciais Implementados
- **Arquitetura em Camadas**: Separação clara de responsabilidades.  
- **Validações Duplas**: Tanto no frontend quanto no backend.  
- **Interface Responsiva**: Adaptada para diferentes tamanhos de tela.  
- **Feedback ao Usuário**: Mensagens de sucesso e erro para todas as operações.  
- **Tratamento de Erros**: Robustez contra falhas e entradas inválidas.  
- **Código Documentado**: Comentários e estrutura clara.

---

# 📝 Próximas Melhorias Possíveis
- Autenticação e autorização de usuários.  
- Filtros e busca na listagem.  
- Paginação de resultados.  
- Gráficos de distribuição de investimentos.  
- Exportação de relatórios (PDF/Excel).  
- Sistema de categorias personalizadas.  
- Alertas e notificações.  
- Histórico de alterações.

---

# 👨‍💻 Desenvolvido por
**[Luan da Silva Lima]**  

- **Email:** [luandasilva1413@example.com]  
- **LinkedIn:** [www.linkedin.com/in/luan13]  
- **GitHub:** [https://github.com/Hyakk3]  

---

# 📄 Licença
Este projeto foi desenvolvido para o processo seletivo da **GF Innovation** e está sob a licença **MIT**.  

