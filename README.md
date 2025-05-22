# SGHSS - Sistema de Gestão Hospitalar e de Serviços de Saúde

Este repositório contém a implementação Back-end do projeto SGHSS, desenvolvido como atividade final do curso de **Análise e Desenvolvimento de Sistemas** da **UNINTER**. O sistema tem como foco o gerenciamento de pacientes, profissionais, agendamentos e leitos da instituição fictícia **VidaPlus**, com atenção especial à segurança e à conformidade com a LGPD.

---

## 🧠 Objetivos do Projeto

- Cadastrar e gerenciar pacientes e profissionais da saúde
- Agendar consultas presenciais ou por telemedicina
- Emitir receitas digitais
- Gerenciar leitos hospitalares disponíveis
- Proteger dados sensíveis com criptografia
- Implementar autenticação segura via JWT

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.11+**
- **Django**
- **Django REST Framework**
- **PostgreSQL**
- **JWT (JSON Web Tokens)**
- **Criptografia AES-256**
- **Postman** para testes de API
- **Draw.io** para diagramas

---

## 📁 Estrutura de Diretórios

SGHSS/
├── core/ # Configurações principais do projeto Django
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── hospital/ # App principal com toda a lógica do sistema
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── tests.py
│ ├── views.py
│ └── migrations/
│ └── init.py
│
├── manage.py # Comando principal do Django
├── venv/ # Ambiente virtual Python
└── README.md # Este arquivo

---

## 🔐 Segurança

- **Criptografia AES-256** para campos como CPF
- Autenticação via **JWT**, usando `djangorestframework-simplejwt`
- Controle de acesso baseado em **perfis de usuário**
- Adequação à **LGPD**

---

## 🧪 Testes

- Testes manuais com **Postman**
- Casos cobertos: autenticação, cadastro, agendamento, segurança

---

## 📊 Diagramas e Modelagem

- **Diagrama de Classes** UML (paciente, profissional, consulta, receita, leito)
- **DER** com relacionamento entre tabelas
- Ferramenta utilizada: **Draw.io**

---