from os import path
import os
import copy

despesas = {}  # Adicionando inicialização dos dicionários
receitas = {}  # Adicionando inicialização dos dicionários


def limpaTela():
    os.system('cls')

# retorna a quantidade de dias que cada mês possui


def quantDias(mes):
    if mes == 1:
        return 31
    elif mes == 2:
        return 28
    elif mes == 3:
        return 31
    elif mes == 4:
        return 30
    elif mes == 5:
        return 31
    elif mes == 6:
        return 30
    elif mes == 7:
        return 31
    elif mes == 8:
        return 31
    elif mes == 9:
        return 30
    elif mes == 10:
        return 31
    elif mes == 11:
        return 30
    elif mes == 12:
        return 31

# Função para cadastrar uma despesa ou receita no dicionário


def cadastra(dic):
    try:
        info = []
        data = []
        nome = input("Descrição: ")
        while nome == '':
            print('Descrição vazia, digite novamente.')
            nome = input("Descrição: ")

        valor = float(input("Valor: "))
        print("Agora informe a data.")
        mes = int(input('Mês: '))
        while (mes < 1 or mes > 12):
            print('Mês inválido, digite novamente.')
            mes = int(input('Mês: '))

        dia = int(input('Dia: '))
        while dia > quantDias(mes) or dia < 1:
            print('Dia inválido, digite novamente.')
            dia = int(input('Dia: '))

        ano = int(input('Ano: '))
        while ano < 1:
            print('Ano inválido, digite novamente.')
            ano = int(input('Ano: '))

        # formatando com '0' a esquerda para funcionamento do método 'ordenar'
        dia = f"{dia:02}"
        mes = f"{mes:02}"
        ano = f"{ano:04}"
        data.append(dia)
        data.append(mes)
        data.append(ano)
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
                        print("Operação cancelada.")
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
            with open('Historico despesas.txt', 'wt', encoding='utf-8') as arquivo:
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
            with open('Historico receita.txt', 'wt', encoding='utf-8') as arquivo:
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
        arquivo_existe = path.exists('Historico despesas.txt')
        if arquivo_existe:
            with open('Historico despesas.txt', 'rt', encoding='utf-8') as arquivo:
                dados = arquivo.readlines()
                for item in dados:
                    if 'Descrição' in item:
                        info['Descrição'] = item[11:-1]
                    elif 'Valor' in item:
                        # indice começando do '10' pois é quando se inicia o valor em float para conversão
                        info['Valor'] = float(item[10:])
                    elif 'Data' in item:
                        # indices fixos para capturar de maneira adequada os dados de 'Data'
                        info['Data'] = item[6:8], item[9:11], item[12:-1]
                        aux = info.values()
                        despesas.update({indice+1: list(aux).copy()})
                        indice += 1
            print('Dados carregados com sucesso')

        else:
            print('Não há dados para serem carregados.')
    else:
        indice = len(receitas)
        arquivo_existe = path.exists('Historico receita.txt')
        if arquivo_existe:
            with open('Historico receita.txt', 'rt', encoding='utf-8') as arquivo:
                dados = arquivo.readlines()
                for item in dados:
                    if 'Descrição' in item:
                        info['Descrição'] = item[11:-1]
                    elif 'Valor' in item:
                        # indice começando do '10' pois é quando se inicia o valor em float para conversão
                        info['Valor'] = float(item[10:])
                    elif 'Data' in item:
                        # indices fixos para capturar de maneira adequada os dados de 'Data'
                        info['Data'] = item[6:8], item[9:11], item[12:-1]
                        aux = info.values()
                        receitas.update({indice+1: list(aux).copy()})
                        indice += 1
            print('Dados carregados com sucesso')

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

    op = menu(opcoes)

    while op != 7:
        if op == 1:
            cadastra(despesas)
            input('Pressione ENTER para continuar.')
            limpaTela()
        elif op == 2:
            listar(despesas, 'despesas')
            input('Pressione ENTER para continuar.')
            limpaTela()
        elif op == 3:
            total_despesas = calcular_total(despesas)
            print(f"Valor Total de Despesas: R$ {total_despesas:.2f}")
            input('Pressione ENTER para continuar.')
            limpaTela()
        elif op == 4:
            exclusao(despesas, 'despesas')
            input('Pressione ENTER para continuar.')
            limpaTela()
        elif op == 5:
            salvarTxt(despesas, 'despesas')
            input('Pressione ENTER para continuar.')
            limpaTela()
        elif op == 6:
            carregarDados('despesas')
            input('Pressione ENTER para continuar.')
            limpaTela()

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

    op = menu(opcoes)

    while op != 7:
        if op == 1:
            cadastra(receitas)
            input('Pressione ENTER para continuar.')
            limpaTela()
        elif op == 2:
            listar(receitas, 'receitas')
            input('Pressione ENTER para continuar.')
            limpaTela()
        elif op == 3:
            total_receitas = calcular_total(receitas)
            print(f"Valor Total de Receitas: R$ {total_receitas:.2f}")
            input('Pressione ENTER para continuar.')
            limpaTela()
        elif op == 4:
            exclusao(receitas, 'receitas')
            input('Pressione ENTER para continuar.')
            limpaTela()
        elif op == 5:
            salvarTxt(receitas, 'receitas')
            input('Pressione ENTER para continuar.')
            limpaTela()
        elif op == 6:
            carregarDados('receitas')
            input('Pressione ENTER para continuar.')
            limpaTela()

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
            input('Pressione ENTER para continuar.')
            limpaTela()
            despesas_menu()
        elif op == 2:
            print("Gerenciamento de Receitas")
            input('Pressione ENTER para continuar.')
            limpaTela()
            receitas_menu()
        elif op == 3:
            relatorio()
            input('Pressione ENTER para continuar.')
            limpaTela()

        op = menu(opcoes_principais)

    # Imprimindo para o usuário que o programa foi encerrado.
    limpaTela()
    print("Programa encerrado.")


if __name__ == "__main__":
    main()
