Playwright QA Automation - Python

Framework de automação de testes E2E e API desenvolvido em Python usando Playwright e Pytest.

Tecnologias

- Python
- Playwright
- Pytest
- Git / GitHub
- Page Object Model (POM)

Estrutura do Projeto

Playplaywright/
│
├── .venv/                     # Ambiente virtual
│
├── pages/                     # Page Objects (UI)
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── screenshots/               # Evidências dos testes (ignorado no Git)
│
├── tests/
│   │
│   ├── api/                   # Testes de API
│   │   ├── clients/
│   │   │   └── petstore_client.py
│   │   │
│   │   └── tests/
│   │       ├── API.py
│   │       └── test_petstore.py
│   │
│   └── ui/                    # Testes de interface (E2E)
│       ├── test.py
│       └── test_saucedemo.py
│
├── .gitignore
├── config.py                  # URLs e configurações
├── conftest.py                # Fixtures globais do Pytest
├── requirements.txt
└── README.md

