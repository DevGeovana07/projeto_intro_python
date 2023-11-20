from os import path

despesas = {}  # Adicionando inicialização dos dicionários
receitas = {}  # Adicionando inicialização dos dicionários

# Função para cadastrar uma despesa ou receita no dicionário


def cadastra(dic):
    try:
        info = []
        data = []
        nome = input("Descrição: ")
        valor = float(input("Valor: "))
        print("Agora informe a data.")
        data.append(int(input("Dia: ")))
        data.append(int(input("Mês: ")))
        data.append(int(input("Ano: ")))
        info.extend([nome, valor, data])
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
            print(f"Data: {dados[2][0]}/{dados[2][1]}/{dados[2][2]}\n")


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
                    print(f"{tipo.capitalize()} #{indice}")
                    print(f"Descrição: {dic[indice][0]}")
                    print(f"Valor: R$ {dic[indice][1]:.2f}")
                    print(
                        f"Data: {dic[indice][2][0]}/{dic[indice][2][1]}/{dic[indice][2][2]}\n")
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
            with open('Historico despesas.txt', 'wt') as arquivo:
                for indice, dados in dic.items():
                    arquivo.write(f"{tipo.capitalize()} #{indice}\n")
                    arquivo.write(f"Descrição: {dados[0]}\n")
                    arquivo.write(f"Valor: R$ {dados[1]:.2f}\n")
                    arquivo.write(
                        f"Data: {dados[2][0]}/{dados[2][1]}/{dados[2][2]}\n")
            print('Arquivo de despesas salvo com sucesso.')

    elif tipo == 'receitas':
        if len(receitas) == 0:
            print('Não há dados para serem salvos em receita.')
            return
        else:
            with open('Historico receita.txt', 'wt') as arquivo:
                for indice, dados in dic.items():
                    arquivo.write(f"{tipo.capitalize()} #{indice}\n")
                    arquivo.write(f"Descrição: {dados[0]}\n")
                    arquivo.write(f"Valor: R$ {dados[1]:.2f}\n")
                    arquivo.write(
                        f"Data: {dados[2][0]}/{dados[2][1]}/{dados[2][2]}\n")
            print('Arquivo de receita salvo com sucesso.')


def carregarDados(tipo):
    info = {'Descrição': '', 'Valor': 0.0, 'Data': []}
    if tipo == 'despesas':
        indice = len(despesas)
        print(f'Indice: {indice}')
        arquivo_existe = path.exists('Historico despesas.txt')
        if arquivo_existe:
            with open('Historico despesas.txt', 'rt') as arquivo:
                dados = arquivo.readlines()
                for item in dados:
                    if 'Descrição' in item:
                        info['Descrição'] = item[11:-1]
                    elif 'Valor' in item:
                        # indice começando do '10' pois é quando se inicia o valor em float para conversão
                        info['Valor'] = float(item[10:])
                    elif 'Data' in item:
                        # ele recebe uma string, sendo q esperava tres int
                        info['Data'] = item[6:8], item[9:11], item[12:-1]
                        aux = info.values()
                        despesas.update({indice+1: list(aux).copy()})
                        indice += 1
            print('Dados carregados com sucesso')
            print(despesas)

        else:
            print('Não há dados para serem carregados.')
    else:
        indice = len(receitas)
        arquivo_existe = path.exists('Historico receita.txt')
        if arquivo_existe:
            with open('Historico receita.txt', 'rt') as arquivo:
                dados = arquivo.readlines()
                for item in dados:
                    if 'Descrição' in item:
                        info['Descrição'] = item[11:-1]
                    elif 'Valor' in item:
                        # indice começando do '10' pois é quando se inicia o valor em float para conversão
                        info['Valor'] = float(item[10:])
                    elif 'Data' in item:
                        # ele recebe uma string, sendo q esperava tres int
                        info['Data'] = item[6:8], item[9:11], item[12:-1]
                        aux = info.values()
                        receitas.update({indice+1: list(aux).copy()})
                        indice += 1
            print('Dados carregados com sucesso')
            print(receitas)

        else:
            print('Não há dados para serem carregados.')

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
        6: 'Carregar arquivo',
        7: 'Sair'
    }

    indice_despesas = 1

    op = menu(opcoes)

    while op != 7:
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
        elif op == 6:
            carregarDados('despesas')

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
        6: 'Carregar arquivo',
        7: 'Sair'
    }

    indice_receitas = 1

    op = menu(opcoes)

    while op != 7:
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
        elif op == 6:
            carregarDados('receitas')

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