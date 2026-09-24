# 🛡️ CYBER USER ACCESS ANALYZER

Projeto educacional desenvolvido em Python para simular um fluxo básico de controle de acesso e análise de usuários.

O projeto foi desenvolvido como parte dos meus estudos de Programação Python aplicada à Cibersegurança.

## 🎯 Objetivo

Simular, de forma simples, algumas etapas de um processo de autenticação e análise de acesso, utilizando fundamentos de programação Python.

## 🔍 O que o programa faz?

O programa realiza diferentes verificações:

1. **Identificação do usuário**
   - Verifica se o usuário informado está na lista de usuários autorizados.

2. **Verificação de senha**
   - Solicita uma senha.
   - Permite um número limitado de tentativas.
   - Interrompe o processo quando a senha correta é informada.

3. **Verificação de IP**
   - Compara o IP informado com uma lista de IPs conhecidos.

4. **Análise de usuários**
   - Percorre uma lista de usuários.
   - Procura determinados padrões nos nomes.
   - Utiliza um contador para registrar ocorrências.

5. **Decisão de acesso**
   - Utiliza condições lógicas para determinar se o acesso será permitido ou negado.

## 🧠 Conceitos de Python utilizados

- Variáveis
- Strings
- Booleanos
- `input()` e `print()`
- Listas
- `if`, `elif` e `else`
- `for` e `while`
- `range()`
- `break`
- `continue`
- `for...else`
- Operadores `and`, `or` e `not`
- `in` e `not in`
- `.strip()`
- `.lower()`
- `.startswith()`
- Contadores com `+=`

## 🛠️ Tecnologia

- Python 3

## ▶️ Como executar

No terminal:

```bash
python3 cyber_user_access_analyzer.py
