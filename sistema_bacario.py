menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
SAQUE_MAXIMO = 500
numero_saques = 0
extrato = ''
LIMITE_SAQUES = 3


while True:
    
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Informe o valor a ser depositado: R$ '))
        
        if valor > 0:     
            saldo += valor
            extrato += f'\ndeposito R$ {valor:.2f}'
        else:
            print('Valor de deposito invalido!')
    
    elif opcao == 's':

        if numero_saques > 3:
            print( 'Limite de saque diario excedido, tente novamente amnanhã!')
        else:
            valor = float(input('Informe o valor a ser sacado: R$ '))
            
            if valor > saldo:
                print(f'Valor de saque indisponivel...\nSaldo em conta R$ {saldo:.2f}')

            elif valor > SAQUE_MAXIMO:
                print('Limite maximo por saque atingido (R$ 500,00)')
            
            elif valor <= 0:
                print(f'Valor de saque icorreto R$ {valor}')
            
            else:           
                saldo -= valor
                extrato += f'\nsaque R$ {valor:.2f}'
                            
            numero_saques += 1
        
    elif opcao == 'e':
        print('\n*************** EXTRATO ***************\n')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('\n***************************************')
        
    elif opcao == 'q':
        break
    
    else:
        print('Operação invalida tente novamente')