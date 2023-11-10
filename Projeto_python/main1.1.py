
def cadastra(dic, id):
    info = []
    nome = input("Descrição: ")
    valor = float(input("Valor: "))
    print("Agora informe a data.")
    dia = int(input("Dia: "))
    mes = int(input("Mês: "))
    ano = int(input("Ano: "))
    info.append(nome)
    info.append(valor)
    info.append(dia)
    info.append(mes)
    info.append(ano)
    # add a despesa
    dic[id] = info


def listar(dic, flag):
    # verifica se há dados para ser exibidos
    if len(dic) == 0:
        print('Não há dados.')
        return
    # para exibir as informações na sequência q foram cadastradas
    if flag == 'despesas':
        for indice, dados in dic.items():  # 'dados' é composta pelos seguintes dados: descrição, valor, dia, mes, ano
            print(f"""Despesa #{indice+1}
Descrição: {dados[0]}
Valor: R$ {dados[1]:.2f}
Data: {dados[2]}/{dados[3]}/{dados[4]} 
            """)
    else:
        for indice, dados in dic.items():  # 'dados' é composta pelos seguintes dados: descrição, valor, dia, mes, ano
            print(f"""Receita #{indice+1}
Descrição: {dados[0]}
Valor: R$ {dados[1]:.2f}
Data: {dados[2]}/{dados[3]}/{dados[4]} 
            """)

# Função que calcula o valor total das despesas e das receitas.


def valorTotal(dic):
    total = 0
    for dados in dic.values():
        total += dados[1]
    return total


def relatorio(dic1, dic2):
    saldo = valorTotal(dic2) - valorTotal(dic1)
    print("========== Extrato ==========")
    if len(dic1) == 0 and len(dic2) == 0:
        print('========== Saldo ==========')
        print(f'Saldo: {saldo:.2f}')
        return

    if len(dic1) > 0:
        print("========== Despesas ==========")
        for indice, dados in dic1.items():  # 'dados' é composta pelos seguintes dados: descrição, valor, dia, mes, ano
            print(f"""Despesa #{indice+1}
Descrição: {dados[0]}
Valor: R$ {dados[1]:.2f}
Data: {dados[2]}/{dados[3]}/{dados[4]} 
                """)

    if len(dic2) > 0:
        print("========== Receita ==========")
        for indice, dados in dic2.items():  # 'dados' é composta pelos seguintes dados: descrição, valor, dia, mes, ano
            print(f"""Receita #{indice+1}
Descrição: {dados[0]}
Valor: R$ {dados[1]:.2f}
Data: {dados[2]}/{dados[3]}/{dados[4]} 
            """)

    print('========== Saldo ==========')
    print(f'Saldo: {saldo:.2f}')


def exclusao(dic, flag):
    if flag == 'despesas':
        excluir = int(
            input('Digite o indice da despesas que você deseja excluir: '))
    else:
        excluir = int(
            input('Digite o indice da receita que você deseja excluir: '))

    print(f'Deseja mesmo excluir a seguinte informação?\n{dic[excluir-1]}')
    conf = input('[S - Sim / N - Não]\nR: ').upper()
    if conf == 'N':
        return

    dic.pop(excluir-1)
    print('Item excluído com sucesso.')


def menu1():
    print('''------ Menu ------
    1 - Despesas
    2 - Receita
    3 - Relatório
    4 - Sair''')


def menu2():
    print('''------ Menu ------
    1 - Cadastra
    2 - Listar
    3 - Valor total
    4 - Exclusão
    5 - Sair''')


# inicio código 'main'
menu1()
despesas = {}
receita = {}

# indice - usado para controlar e referenciar as dispesas e receita
indice_depesas = 0
indice_receita = 0

op = int(input("Digite a opção: "))

while op:
    if op == 1:
        print("Entrando em despesas!")
        menu2()
        op = int(input("Digite a opção: "))

        while op:
            # despesas
            if op == 1:
                cadastra(despesas, indice_depesas)
                indice_depesas += 1
            elif op == 2:
                listar(despesas, 'despesas')
            elif op == 3:
                totalDespesas = valorTotal(despesas)
                print(f"Valor Total de Despesas: R${totalDespesas:.2f}")
            elif op == 4:
                exclusao(despesas, 'despesas')
            elif op == 5:
                break

            menu2()
            op = int(input("Digite a opção: "))
    elif op == 2:
        print("Entrando em receita!")
        menu2()
        op = int(input("Digite a opção: "))

        while op:
            # receita
            if op == 1:
                cadastra(receita, indice_receita)
                indice_receita += 1
            elif op == 2:
                listar(receita, 'receita')
            elif op == 3:
                totalReceita = valorTotal(receita)
                print(f"Valor Total da Receita: R${totalReceita:.2f}")
            elif op == 4:
                exclusao(receita, 'receita')
            elif op == 5:
                break

            menu2()
            op = int(input("Digite a opção: "))
    elif op == 3:
        relatorio(despesas, receita)
    elif op == 4:
        break
    menu1()
    op = int(input("Digite a opção: "))
