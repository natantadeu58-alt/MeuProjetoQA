# 🧪 Projeto de Automação de Testes e QA - Swag Labs (SauceDemo)

Este repositório contém a suíte de testes automatizados E2E (End-to-End) desenvolvida para validar as funcionalidades do e-commerce fictício [SauceDemo](https://saucedemo.com).

O projeto utiliza a arquitetura **Page Object Model (POM)** para garantir fácil manutenção, legibilidade e reutilização do código de testes.

---

## 🛠️ Tecnologias Utilizadas

* **Python**: Linguagem de programação principal.
* **Playwright**: Framework de automação de testes web rápido e moderno.
* **Pytest**: Framework de testes para execução e validação dos cenários.

---

## 📁 Estrutura do Projeto

```text
MeuProjetoQA/
│
├── pages/                # Classes com os seletores e ações das páginas (POM)
│   └── login_page.py
│
├── tests/                # Cenários de testes automatizados
│   └── test_login.py
│
├── .gitignore            # Arquivos ignorados pelo Git
└── README.md             # Documentação do projeto
```

---

## 🚀 Pré-requisitos e Instalação

Siga os passos abaixo para configurar o ambiente localmente:

1. **Clonar o repositório**
   ```bash
   git clone https://github.com
   cd MeuProjetoQA
   ```

2. **Criar e ativar o ambiente virtual (opcional, mas recomendado)**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar as dependências do Python**
   ```bash
   pip install pytest playwright
   ```

4. **Instalar os navegadores do Playwright**
   ```bash
   playwright install
   ```

---

## 🧪 Como Executar os Testes

Os testes são gerenciados pelo Pytest. Você pode executá-los de diferentes formas:

* **Execução padrão (modo Headless - em segundo plano):**
  ```bash
  pytest
  ```

* **Execução visual (modo Headed - abrindo o navegador):**
  ```bash
  pytest --headed
  ```

* **Execução com exibição detalhada dos logs (Verbose):**
  ```bash
  pytest -v
  ```

---

## 📝 Cenários Cobertos

Atualmente, o projeto valida os seguintes fluxos na página de login:
* **Login com sucesso**: Valida o acesso usando um usuário padrão válido.
* **Login com usuário bloqueado**: Valida a mensagem de erro esperada para a conta bloqueada.
* **Login com senha incorreta**: Valida o comportamento do sistema diante de credenciais inválidas.
