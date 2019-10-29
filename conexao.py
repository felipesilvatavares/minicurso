import pymysql


def conectar_banco_mysql():
    conexao_mysql = None

    try:
        # Efetua a conexão com o banco de dados mysql mantendo o auto commit off para ser feito manualmente
        conexao_mysql = pymysql.connect('127.0.0.1', 'quantum', 'quantum28042004', 'minicurso', 3390)
    except Exception as erro:
        print("\nOcorreu um erro na chamada da função 'conectar_banco_mysql'. Erro Original: " + str(erro) + "\n")
    
    # Retorna a instância da conexão
    return conexao_mysql


def desconectar_banco_mysql(conexao_mysql, cursor_mysql):
    try:
        if conexao_mysql != None:
            conexao_mysql.close()
        
        if cursor_mysql != None:
            cursor_mysql.close()
    except Exception as erro:
        print("\nOcorreu um erro na chamada da função 'desconectar_banco_mysql'. Erro Original: " + str(erro)+ "\n")

