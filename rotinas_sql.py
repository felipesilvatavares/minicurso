import conexao


def inserir_registro(nome, sobrenome):
    # Definindo as variáveis vazias
    conexao_banco = None
    cursor_banco = None

    try:
        # Retorna a instância de conexão com o banco de dados
        conexao_banco = conexao.conectar_banco_mysql()

        # Cria o cursor para executação da inserção
        cursor_banco = conexao_banco.cursor()

        # String sql
        sql = 'INSERT INTO pessoa (nome, sobrenome) VALUES (%s, %s)'

        # Executa a operação de inserção no banco de dados
        cursor_banco.execute(sql, (nome, sobrenome))

        # Efetiva a transação no banco
        conexao_banco.commit()

    except Exception as erro:
        print("Ocorreu um erro na chamada da função 'inserir_registro'. Erro Original: " + str(erro))
    finally:
        # Fecha as conexões de acesso ao banco caso tenham sido abertas
        conexao.desconectar_banco_mysql(conexao_banco, cursor_banco)


def listar_registros():
    # Definindo as variáveis vazias
    conexao_banco = None
    cursor_banco = None

    try:
        # Retorna a instância de conexão com o banco de dados
        conexao_banco = conexao.conectar_banco_mysql()

        # Cria o cursor para executação da inserção
        cursor_banco = conexao_banco.cursor()

        # String sql
        sql = 'SELECT * FROM pessoa'

        # Abre o cursor com a consulta no banco de dados
        cursor_banco.execute(sql)

        # Retorna para a variável os dados que foram consultados do banco
        retorno_consulta = cursor_banco.fetchall()

        # Laço de repetição para mostrar os dados retornados
        for pessoa in retorno_consulta:
            print('Id: ', str(pessoa[0]) ,' - Nome: ', str(pessoa[1]), ' - Sobrenome: ', str(pessoa[2]))

    except Exception as erro:
        print("Ocorreu um erro na chamada da função 'listar_registros'. Erro Original: " + str(erro))
    finally:
        # Fecha as conexões de acesso ao banco caso tenham sido abertas
        conexao.desconectar_banco_mysql(conexao_banco, cursor_banco)