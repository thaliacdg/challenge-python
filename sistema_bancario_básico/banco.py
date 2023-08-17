menu = ''' 
Selecione uma operacao:
[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] SAIR
[5] CRIAR USUARIO
[6] CRIAR CONTA CORRENTE
'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(saldo, extrato, valor):
    if valor <= 0:
        print('Depósito Inválido')
    else:
        saldo += valor
        extrato += f'Depósito R$: {valor:.2f}\n'
        print('Depósito Efetuado')
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, limite_saques, valor):
    if valor <= 0 or valor > saldo:
        print('Saque Inválido')
    elif numero_saques == limite_saques or valor > 500:
        print('Limite diário excedido')
    else:
        print('Saque Efetuado')
        saldo -= valor
        extrato += f'Saque R$: {valor:.2f}\n'
        numero_saques += 1
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print(extrato)
    print('Seu saldo é R$', saldo)

def criar_usuario(usuarios, nome, data_nascimento, cpf, endereco):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print('Usuário com CPF já cadastrado')
            return usuarios
    
    endereco_formatado = ', '.join(endereco)
    novo_usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco_formatado
    }
    usuarios.append(novo_usuario)
    print('Usuário cadastrado com sucesso')
    return usuarios

def criar_conta_corrente(contas, usuarios, usuario_id):
    numero_conta = len(contas) + 1
    agencia = '0001'
    nova_conta = {
        'agencia': agencia,
        'numero_conta': numero_conta,
        'usuario': usuarios[usuario_id]
    }
    contas.append(nova_conta)
    print('Conta corrente criada com sucesso')
    return contas

usuarios = []
contas = []

while True:
    opcao = input(menu)

    if opcao == '1':
        print('Insira um valor')
        deposito = float(input())
        saldo, extrato = depositar(saldo, extrato, deposito)

    elif opcao == '2':
        print('Insira um valor')
        saque = float(input())
        saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, saque)

    elif opcao == '3':
        exibir_extrato(saldo, extrato)

    elif opcao == '4':
        break

    elif opcao == '5':
        nome = input('Digite o nome: ')
        data_nascimento = input('Digite a data de nascimento: ')
        cpf = input('Digite o CPF (somente números): ')
        endereco = input('Digite o endereço (logradouro, número, bairro, estado): ').split(', ')
        usuarios = criar_usuario(usuarios, nome, data_nascimento, cpf, endereco)

    elif opcao == '6':
        for i, usuario in enumerate(usuarios):
            print(f"{i + 1}. {usuario['nome']} - CPF: {usuario['cpf']}")
        usuario_id = int(input('Escolha o número do usuário: ')) - 1
        contas = criar_conta_corrente(contas, usuarios, usuario_id)

    else:
        print('Operação inválida')
