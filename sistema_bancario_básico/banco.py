menu = ''' 
Selecione uma operacao:
[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] SAIR
'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == '1':
        print('Insira um valor')
        deposito = float(input())
        if deposito <= 0:
            print('Depósito Inválido')
        else:
            saldo += deposito
            extrato += f'Deposito R$: {deposito:.2f}\n'
            print('Depósito Efetuado')    

    elif opcao == '2':
           print('Insira um valor')
           saque = float(input())
           if saque <= 0 or saque > saldo:
            print('Saque Inválido')

           elif numero_saques == LIMITE_SAQUES or  saque > 500:
               print('Limite diário excedido')
               break 

           else:
            print('Saque Efetuado')
            saldo -= saque 
            extrato += f'Saque R$: {saque:.2f}\n'
            numero_saques += 1   


    elif opcao == '3':
        print(extrato)
        extrato = saldo
        print('Seu saldo é R$', extrato)    

    elif opcao == '4':
        break            

    else:
        print('Operação inválida')