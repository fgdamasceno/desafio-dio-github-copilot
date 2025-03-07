# Solicita a entrada do usuário
texto = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

# Repete o texto o número de vezes informado com espaço entre as repetições
resultado = ' '.join([texto] * numero)

# Exibe o resultado
print(resultado)