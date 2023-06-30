def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero!"

# Função para exibir as opções de operação
def exibir_menu():
    print("Escolha uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0. Sair")

# Loop principal do programa
while True:
    exibir_menu()
    opcao = input("Digite o número da operação desejada: ")

    if opcao == "0":
        print("Encerrando a calculadora.")
        break

    # Obter os números de entrada
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == "1":
        resultado = adicao(num1, num2)
    elif opcao == "2":
        resultado = subtracao(num1, num2)
    elif opcao == "3":
        resultado = multiplicacao(num1, num2)
    elif opcao == "4":
        resultado = divisao(num1, num2)
    else:
        print("Opção inválida!")
        continue

    print("Resultado: ", resultado)
    print("-----------------------")
