def menu():
    menu = """
    
    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Sair
    => """
    return input(menu)


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {saldo:.2f}\n'
        print('Valor depositado com sucesso!')
    else:
        print('Operação falhou! O valor é iválido.')
    
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print('Operação falhou! Você não tem saldo suficiente.')
    
    elif excedeu_limite:
        print('Operação falhou! O valor do saque excede o limite.')

    elif excedeu_saques:
        print('Operação falhou! Número máximo de saques excedidos.')

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_saques += 1
        print('Saque realizado com sucesso!')

    else:
        print('Operação falhou! Valor informado é inválido.')

    


def exibir_extrato(saldo, /, *, extrato):
    print("\n==============EXTRATO==============")
    print("Não formam realizadas movimentações."  if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===================================")



def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    conas = []

    while True:
        opcao = menu()

        if opcao == 1:
            valor = float(input('Informe o valor do depósito: '))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 2:
            valor = float(input('Informe o valor do saque: '))

            saldo, extrato = sacar(
            saldo = saldo,
            valor = valor,
            extrato = extrato,
            limite = limite,
            numero_saques = numero_saques,
            limite_saques = LIMITE_SAQUES
        )
            
        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)
            

