# Solicita o primeiro nome do usuário
pnome = input("Digite o seu primeiro nome: ")

# Solicita o último nome do usuário
unome = input("Digite o seu último nome: ")

# Pergunta se o usuário possui um sobrenome intermediário
pergunta = input("Você possui um sobrenome intermediário? (s/n) ")

# Verifica se a resposta é "s" ou "S"
if pergunta == "S" or pergunta == "s":
    # Solicita o sobrenome intermediário do usuário
    mnome = input("Digite o seu sobrenome intermediário: ")
    # Exibe a saudação com o nome completo
    print("Olá " + pnome + " " + mnome + " " + unome + "!")
else:
    # Exibe a saudação com o primeiro e último nome
    print("Olá " + pnome + " " + unome + "!")
