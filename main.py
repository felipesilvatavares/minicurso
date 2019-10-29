import conexao
import menu
import rotinas_sql


if __name__ == "__main__":
    # Mostrando o menu com as opções de seleção para o tipo de operação a ser feita no banco
    tipo_operacao = menu.retorna_tipo_operacao_banco()
    
    # Validando o tipo de operação informada
    if "Inserir" in tipo_operacao:
        # Retorna uma tupla com o nome e sobrenome informados no menu
        nome, sobrenome = menu.menu_inserir()

        # Chama a rotina para a inserção no banco de dados do nome e sobrenome informados
        rotinas_sql.inserir_registro(nome, sobrenome)
    elif "Listar" in tipo_operacao:
        # Chama a rotina de listagem do banco de dados para vistualizar todos os registros já cadastrados
        rotinas_sql.listar_registros()
