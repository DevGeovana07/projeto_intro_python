# indice - usado para controlar e referenciar as dispesas e receita
indice = 0

# descrição, valor, data
despesas = {}
receita = {}

def cadastra(dic, id):
    info = []
    nome = input("Títluo: ")
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
    despesas[id] = info


def menu1():
    print('''------ Menu ------
    1 - Despesas
    2 - Receita
    3 - Relatório
    4 - Sair''')

def menu2():
    print('''------ Menu ------
    1 - Cadastra
    2 - Lista
    3 - Valor total
    4 - Exclusão
    5 - Sair''')

menu1()
op = int(input("Digite a opção: "))

while op:
    if op == 1:
        print("Entrando em despesas!") 
        menu2()
        op = int(input("Digite a opção: "))

        while op:
            # despesas
            if op == 1:
                cadastra(despesas, indice)
                indice += 1
            if op == 5:
                break

            menu2()
            op = int(input("Digite a opção: "))
    elif op == 2:
        print("Entrando em receitas!") 
        menu2()
        op = int(input("Digite a opção: "))

        while op:
            # despesas
            if op == 1:
                cadastra(receita)
            if op == 5:
                break

            menu2()
            op = int(input("Digite a opção: "))
    elif op == 4:
        break
    menu1()
    op = int(input("Digite a opção: "))

print(despesas)