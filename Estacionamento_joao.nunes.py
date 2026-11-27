
CAPACIDADE = 20
VALOR_HORA = 8.00

carros = 0
faturamento = 0


def mostrar_menu():
    print("===== SISTEMA DE ESTACIONAMENTO =====")
    print("1 - Registrar entrada de veículo")
    print("2 - Registrar saída de veículo")
    print("3 - Consultar vagas disponíveis")
    print("4 - Consultar faturamento")
    print("0 - Sair")


def calcular_valor(horas):
    return horas * VALOR_HORA


opcao = ""

while opcao != "0":
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        placa = input("Placa do veículo: ")
        if carros < CAPACIDADE:
            carros = carros + 1
            print("Entrada registrada!")
        else:
            print("Estacionamento lotado")

    elif opcao == "2":
        if carros == 0:
            print("Não há veículos estacionados.")
        else:
            placa = input("Placa do veículo: ")
            horas = int(input("Horas estacionado: "))
            valor = calcular_valor(horas)
            print("Valor a pagar: R$", valor)
            faturamento = faturamento + valor
            carros = carros - 1

    elif opcao == "3":
        print("Capacidade total:", CAPACIDADE)
        print("Veículos estacionados:", carros)
        print("Vagas disponíveis:", CAPACIDADE - carros)

    elif opcao == "4":
        print("Faturamento total: R$", faturamento)

    elif opcao == "0":
        print("Saindo...")

    else:
        print("Opção inválida!")