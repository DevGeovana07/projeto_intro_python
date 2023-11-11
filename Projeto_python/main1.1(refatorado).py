# Função para cadastrar uma despesa ou receita no dicionário
def cadastra(dic):
    try:
        info = []
        nome = input("Descrição: ")
        valor = float(input("Valor: "))
        print("Agora informe a data.")
        dia = int(input("Dia: "))
        mes = int(input("Mês: "))
        ano = int(input("Ano: "))
        info.extend([nome, valor, dia, mes, ano])
        dic[len(dic) + 1] = info
    except ValueError:
        print('ERRO: É necessario inserir um número no campo "Valor" e números inteiros nos campos "Dia", "Mês" e "Ano".')


# Função para listar despesas ou receitas
def listar(dic, tipo):
    if not dic:
        print(f"Não há {tipo}.")
    else:
        for indice, dados in dic.items():
            print(f"{tipo.capitalize()} #{indice}")
            print(f"Descrição: {dados[0]}")
            print(f"Valor: R$ {dados[1]:.2f}")
            print(f"Data: {dados[2]}/{dados[3]}/{dados[4]}\n")


# Função para calcular o valor total 
def calcular_total(dic):
    total = sum(dados[1] for dados in dic.values())
    return total


# Função para gerar o relatório com todas as informações do usuário
def relatorio(despesas, receitas):
    total_despesas = calcular_total(despesas)
    total_receitas = calcular_total(receitas)
    saldo = total_receitas - total_despesas

    print("========== Extrato ==========")
    if not despesas and not receitas:
        print("Não há despesas ou receitas.")
    else:
        if despesas:
            print("========== Despesas ==========")
            listar(despesas, 'despesa')

        if receitas:
            print("========== Receitas ==========")
            listar(receitas, 'receita')

    print("========== Saldo ==========")
    print(f"Saldo: R$ {saldo:.2f}")


# Função para excluir uma despesa ou receita do dicionário
def exclusao(dic, tipo):
    try:
        if not dic:
            print(f"Não há {tipo}.")
        else:
            indice = int(input(f"Digite o índice da {tipo} que deseja excluir: "))
            try:
                if indice in dic:
                    print(
                        f"Deseja mesmo excluir a seguinte informação?\n{dic[indice]}")
                    confirma = input("[S - Sim / N - Não]\nR: ").upper()
                    if confirma == 'S':
                        dic.pop(indice)
                        print("Item excluído com sucesso.")
                else:
                    print(f"Índice {indice} não encontrado.")
            finally:
                print("Digite 'S' para SIM e 'N' para NÃO, se você realmente deseja excluir. ")
    except ValueError:
        print("ERRO: É necessário inserir o número da despesa ou receita que deseja excluir.")

# Função para exibir o menu e obter a escolha do usuário
def menu(opcoes):
    try:
        for opcao in opcoes:
            print(f"{opcao} - {opcoes[opcao]}")
        op = int(input("Digite a opção: "))
        return op
    except ValueError:
        print("ERRO: É necessário inserir o número das opções acima.")


# Função menu de despesas
def despesas_menu():
    despesas = {}
    opcoes = {
        1: 'Cadastrar Despesa',
        2: 'Listar Despesas',
        3: 'Valor Total de Despesas',
        4: 'Excluir Despesa',
        5: 'Sair'
    }

    indice_despesas = 1

    op = menu(opcoes)

    while op != 5:
        if op == 1:
            cadastra(despesas)
            indice_despesas += 1
        elif op == 2:
            listar(despesas, 'despesas')
        elif op == 3:
            total_despesas = calcular_total(despesas)
            print(f"Valor Total de Despesas: R$ {total_despesas:.2f}")
        elif op == 4:
            exclusao(despesas, 'despesas')

        op = menu(opcoes)

    return despesas  # Adicionando retorno do dicionário atualizado


# Função menu de receitas
def receitas_menu():
    receitas = {}
    opcoes = {
        1: 'Cadastrar Receita',
        2: 'Listar Receitas',
        3: 'Valor Total de Receitas',
        4: 'Excluir Receita',
        5: 'Sair'
    }

    indice_receitas = 1

    op = menu(opcoes)

    while op != 5:
        if op == 1:
            cadastra(receitas)
            indice_receitas += 1
        elif op == 2:
            listar(receitas, 'receitas')
        elif op == 3:
            total_receitas = calcular_total(receitas)
            print(f"Valor Total de Receitas: R$ {total_receitas:.2f}")
        elif op == 4:
            exclusao(receitas, 'receitas')

        op = menu(opcoes)

    return receitas  # Adicionando retorno do dicionário atualizado


# Principal função que controla o fluxo do programa
def main():
    print("========= MENU ========= ")
    opcoes_principais = {
        1: 'Despesas',
        2: 'Receitas',
        3: 'Relatório',
        4: 'Sair'
    }

    op = menu(opcoes_principais)
    despesas = {}  # Adicionando inicialização dos dicionários
    receitas = {}  # Adicionando inicialização dos dicionários

    while op != 4:
        if op == 1:
            print("Gerenciamento de Despesas")
            despesas = despesas_menu()  # Atribuindo o dicionário atualizado
        elif op == 2:
            print("Gerenciamento de Receitas")
            receitas = receitas_menu()  # Atribuindo o dicionário atualizado
        elif op == 3:
            relatorio(despesas, receitas)

        op = menu(opcoes_principais)


    print("Encerrando o programa.") # Imprimindo para o usuário que o programa foi encerrado.

if __name__ == "__main__":
    main()
