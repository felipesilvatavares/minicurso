import os


def retorna_tipo_operacao_banco():
    nome_operacao = None
    confirmacao_operacao = None
    lista_operacoes = {}

    lista_operacoes[1] = 'Inserir'
    lista_operacoes[2] = 'Listar'

    print('\nInforme o tipo de operação que deseja executar.\n')

    while (True):
        for i in lista_operacoes:
            print(str(i) + ' -> ' + lista_operacoes[i])

        IndiceSair = len(lista_operacoes) + 1
        print(str(IndiceSair) + ' -> Sair')

        indice_operacao = input("\nInforme o índice que representa a operação: ")

        try:
            if int(IndiceSair) == int(indice_operacao):
                print("\nOperação cancelada pelo usuário.\n")

                os.system('pause')
                os._exit(1)
        except:
            print("\nOpção inválida. Informe corretamente o índice que representa a operação.\n")
            
            continue
        
        # Valida se o valor informado não está vazio
        if not (indice_operacao.strip()):
            print("\nInforme corretamente o número do índice que representa a operação.\n")
            
            continue

        try:
            nome_operacao = lista_operacoes[int(indice_operacao)]
        except:
            print("\nOpção inválida. Informe corretamente o índice que representa a operação.\n")
            
            continue
        
        print("\n",nome_operacao,"\n")
        
        confirmacao_operacao = input("Deseja utilizar a operação '" + str(nome_operacao) + "' selecionada? (S/N/C): \n")
        if (confirmacao_operacao.upper() == "S"):
            break

        if (confirmacao_operacao.upper() == "C"):
            break

    if (confirmacao_operacao.upper() == "C"):
        print("\nOperação cancelada pelo usuário.\n")
        
        os.system('pause')
        os._exit(1)

    return nome_operacao


def menu_inserir():
    nome_pessoa = None
    sobrenome_pessoa = None

    while True:
        print('\nInserir informações da pessoa.\n')

        while True:
            nome_pessoa = input("\nInforme o nome da pessoa: ")

            if not (nome_pessoa.strip()):
                print("\nInforme corretamente o nome da pessoa.\n")
                
                continue
            else:
                break
        
        print("\n", nome_pessoa, "\n")

        sobrenome_pessoa = input("\nInforme o sobrenome da pessoa: ")

        while True:
            if not (sobrenome_pessoa.strip()):
                print("\nInforme corretamente o sobrenome da pessoa.\n")
                
                continue
            else:
                break
        
        print("\n", sobrenome_pessoa, "\n")
            
        confirmacao_operacao = input("Deseja utilizar o nome e sobrenome informados Nome: '" + 
        str(nome_pessoa) + "' Sobrenome: '" + str(sobrenome_pessoa) + "' informado? (S/N/C): \n")
        
        if (confirmacao_operacao.upper() == "S"):
            break

        if (confirmacao_operacao.upper() == "C"):
            break

        if (confirmacao_operacao.upper() == "C"):
            print("\nOperação cancelada pelo usuário.\n")
            
            os.system('pause')
            os._exit(1)

    return nome_pessoa, sobrenome_pessoa