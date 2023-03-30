menu="""
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito no valor de R$ {valor:.2f}\n"
            print(f"Depósito no valor de R$ {valor:.2f} realizado com sucesso")
        else:
            print("Operação inválida. Informe um valor positivo para o depósito.")

    elif opcao == "s":
        valor = float(input("Informe o valor para o saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("O valor para saque é maior que o saldo em conta. Operação não realizada.")

        elif excedeu_limite:
            print(f"O valor do saque excede o valor de limite: R$ {limite}. Operação não realizada.")

        elif excedeu_saques:
            print("A operação excede o número de saques permitidos. Operação não realidada.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque no valor de R$ {valor:.2f}\n"
            print(f"Saque no valor de R$ {valor:.2f} realizado com sucesso. Retire o seu dinheiro no compartimento.")
            numero_saques += 1

        else:
            print("O valor informado para saque é inválido.")

    elif opcao == "e":
        print("######### EXTRATO BANCÁRIO ##########")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"Saldo em conta: R$ {saldo:.2f}")
        print("#####################################")

    elif opcao == "q":
        print("Obrigado por utilizar o sistema bancário!")
        break

    else:
        print("Opção inválida. Tente novamente.")