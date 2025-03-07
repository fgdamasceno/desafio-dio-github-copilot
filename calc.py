def calculator():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite a escolha(1/2/3/4): ")

    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    if escolha == '1':
        print(f"{num1} + {num2} = {num1 + num2}")

    elif escolha == '2':
        print(f"{num1} - {num2} = {num1 - num2}")

    elif escolha == '3':
        print(f"{num1} * {num2} = {num1 * num2}")

    elif escolha == '4':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Erro! Divisão por zero.")

    else:
        print("Escolha inválida")

if __name__ == "__main__":
    calculator()