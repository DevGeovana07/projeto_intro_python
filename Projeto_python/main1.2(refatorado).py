
despesas = {}  # Adicionando inicialização dos dicionários
receitas = {}  # Adicionando inicialização dos dicionários

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
def relatorio():
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
            indice = int(
                input(f"Digite o índice da {tipo} que deseja excluir: "))
            try:
                if indice in dic:
                    print("Deseja mesmo excluir a seguinte informação?")
                    print(f"Descrição: {dic[indice][0]}")
                    print(f"Valor: R$ {dic[indice][1]:.2f}")
                    print(
                        f"Data: {dic[indice][2]}/{dic[indice][3]}/{dic[indice][4]}\n")
                    confirma = int(input("[1 - Sim | 2 - Não]\nR: "))
                    if confirma == 1:
                        dic.pop(indice)
                        print("Item excluído com sucesso.")
                    if confirma == 2:
                        print(f"Operação cancelada.")
            except ValueError:
                print(
                    "ERRO: Digite '1' para SIM e '2' para NÃO, se você deseja excluir ou não. ")
    except ValueError:
        print(
            "ERRO: É necessário inserir o número da despesa ou receita que deseja excluir.")

# Função para salvar os dados em um arquivo 'txt'


def salvarTxt(dic, tipo):
    if tipo == 'despesas':
        if len(despesas) == 0:
            print('Não há dados para serem salvos em despesas.')
            return
        else:
            with open('Historico despesas', 'wt') as arquivo:
                for indice, dados in dic.items():
                    arquivo.write(f"{tipo.capitalize()} #{indice}\n")
                    arquivo.write(f"Descrição: {dados[0]}\n")
                    arquivo.write(f"Valor: R$ {dados[1]:.2f}\n")
                    arquivo.write(f"Data: {dados[2]}/{dados[3]}/{dados[4]}\n")
            print('Arquivo de despesas salvo com sucesso.')

    elif tipo == 'receitas':
        if len(receitas) == 0:
            print('Não há dados para serem salvos em receita.')
            return
        else:
            with open('Historico receita', 'wt') as arquivo:
                for indice, dados in dic.items():
                    arquivo.write(f"{tipo.capitalize()} #{indice}\n")
                    arquivo.write(f"Descrição: {dados[0]}\n")
                    arquivo.write(f"Valor: R$ {dados[1]:.2f}\n")
                    arquivo.write(f"Data: {dados[2]}/{dados[3]}/{dados[4]}\n")
            print('Arquivo de receita salvo com sucesso.')


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
    opcoes = {
        1: 'Cadastrar Despesa',
        2: 'Listar Despesas',
        3: 'Valor Total de Despesas',
        4: 'Excluir Despesa',
        5: 'Salvar em arquivo',
        6: 'Sair'
    }

    indice_despesas = 1

    op = menu(opcoes)

    while op != 6:
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
        elif op == 5:
            salvarTxt(despesas, 'despesas')

        op = menu(opcoes)

    return despesas

# Função menu de receitas


def receitas_menu():
    opcoes = {
        1: 'Cadastrar Receita',
        2: 'Listar Receitas',
        3: 'Valor Total de Receitas',
        4: 'Excluir Receita',
        5: 'Salvar em arquivo',
        6: 'Sair'
    }

    indice_receitas = 1

    op = menu(opcoes)

    while op != 6:
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
        elif op == 5:
            salvarTxt(receitas, 'receitas')

        op = menu(opcoes)

    return receitas

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

    while op != 4:
        if op == 1:
            print("Gerenciamento de Despesas")
            despesas = despesas_menu()
        elif op == 2:
            print("Gerenciamento de Receitas")
            receitas = receitas_menu()
        elif op == 3:
            relatorio()

        op = menu(opcoes_principais)

    # Imprimindo para o usuário que o programa foi encerrado.
    print("Encerrando o programa.")


if __name__ == "__main__":
    main()
