# cyber_user_access_analyzer.py

print("=" * 45)
print("      CYBER USER ACCESS ANALYZER")
print("=" * 45)

usuarios_autorizados = [
    "Romeu",
    "Carlos",
    "Ana",
    "Maman",
    "Jack"
]

ips_conhecidos = [
    "192.168.1.10",
    "10.0.0.5",
    "192.168.1.20"
]

tentativas_maximas = 3
tentativas = 0
acesso_concedido = False

print("\n--- AUTENTICAÇÃO ---")

nome = input("Digite seu nome: ").strip()

for usuario in usuarios_autorizados:
    if usuario.lower() == nome.lower():
        print("Usuário encontrado:", usuario)
        acesso_concedido = True
        break
else:
    print("Usuário não encontrado.")

if acesso_concedido:
    print("\n--- VERIFICAÇÃO DE SENHA ---")

    senha_correta = "Cyber@2026"

    while tentativas < tentativas_maximas:
        senha = input("Digite sua senha: ")

        if senha == senha_correta:
            print("Senha correta!")
            acesso_concedido = True
            break
        else:
            tentativas += 1
            print("Senha incorreta.")

            if tentativas < tentativas_maximas:
                print("Tentativas restantes:", tentativas_maximas - tentativas)

    if tentativas == tentativas_maximas and senha != senha_correta:
        acesso_concedido = False
        print("Número máximo de tentativas atingido.")

if acesso_concedido:

    print("\n--- ANÁLISE DE REDE ---")

    ip = input("Digite o IP de acesso: ").strip()

    if ip in ips_conhecidos:
        print("IP conhecido.")
    else:
        print("IP não reconhecido.")
        acesso_concedido = False

if acesso_concedido:

    print("\n--- ANÁLISE DO USUÁRIO ---")

    nomes_analisados = [
        "Romeu",
        "Carlos",
        "Ana",
        "Alicia",
        "Maman"
    ]

    contador_a = 0

    for usuario in nomes_analisados:

        if usuario.startswith("A"):
            print("Usuário começa com A:", usuario)

        if "a" in usuario.lower():
            contador_a += 1
        else:
            continue

    print("Usuários que contêm a letra A:", contador_a)

    print("\n--- VERIFICAÇÃO FINAL ---")

    autorizado = True
    bloqueado = False
    administrador = False

    if autorizado and not bloqueado and acesso_concedido:
        print("ACESSO PERMITIDO")
    elif administrador or autorizado:
        print("Acesso autorizado por regra alternativa.")
    else:
        print("ACESSO NEGADO.")

else:
    print("\nACESSO NEGADO.")
    print("A análise foi encerrada.")

print("\n=== FIM DA ANÁLISE ===")
