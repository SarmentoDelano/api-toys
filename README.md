# API de Gerenciamento de Brinquedos

Uma API desenvolvida com Django REST Framework para gerenciar brinquedos, permitindo o cadastro, visualização, atualização e exclusão de informações sobre brinquedos disponíveis.

---

## Recursos da API

A API fornece funcionalidades para:

### Gerenciar Brinquedos:
- Criar novos brinquedos.
- Visualizar lista de brinquedos cadastrados.
- Atualizar informações de brinquedos existentes.
- Excluir brinquedos.

---

## Tecnologias Utilizadas

- Python: Linguagem de programação principal.
- Django: Framework web.
- Django REST Framework (DRF): Criação da API RESTful.
- SQLite: Banco de dados padrão para desenvolvimento.

---

## Configuração do Ambiente

### 1. Pré-requisitos
- Python 3.11+
- Pipenv ou pip para gerenciamento de pacotes
- Git instalado
- Banco de dados SQLite ou outro configurado

### 2. Clonar o Repositório

```bash
git clone https://github.com/SeuUsuario/api-toys.git
cd api-toys
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Executar Migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Rodar o Servidor

```bash
python manage.py runserver
```

A API estará disponível em http://127.0.0.1:8000/.

---

## Endpoints

### Brinquedos

| Método | Endpoint      | Descrição                                   |
|--------|----------------|---------------------------------------------|
| GET    | /api/toys/      | Lista todos os brinquedos                   |
| POST   | /api/toys/      | Cria um novo brinquedo                      |
| GET    | /api/toys/{id}  | Recupera informações de um brinquedo específico |
| PUT    | /api/toys/{id}  | Atualiza informações de um brinquedo        |
| DELETE | /api/toys/{id}  | Remove um brinquedo                         |

---

## Validações

A API realiza validações específicas para assegurar a integridade dos dados:

- O nome (`name`) do brinquedo é obrigatório.
- A categoria (`toy_category`) do brinquedo é obrigatória.
- A data de lançamento (`release_date`) é obrigatória.
- A descrição é opcional.
- O campo `was_included_in_home` indica se o brinquedo foi incluído em um catálogo doméstico.

---
