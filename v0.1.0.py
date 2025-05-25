# -----*----- ATENDENTE DE VOOS -----*-----

def exibir_menu():
    print("\n\n\t\t -*- PROGRAMA DE ATENDENTE DE VOOS -*-")
    print("\n\n\t\t\t >> MENU <<")
    print("\n 1 - Cadastrar voo")
    print("\n 2 - Consultar voo")
    print("\n 3 - Informar voos com menor escala")
    print("\n 4 - Listar passageiros do voo")
    print("\n 5 - Venda de passagem")
    print("\n 6 - Cancelamento de passagem")
    print("\n 7 - Sair do programa")

    menu_principal = opcao_menu(1, 7)
    
    return menu_principal


def cadastro_voo():
    print("\n\n\t\t -*- CADASTRAR UM VOOS -*- ")

    num1 = int(input("\n\n Insira quantos voos deseja cadastrar: "))

    for i in range(num1):
        num_voo1 = verificar_voo()

        cidade_origem = input("\n Cidade de origem: ")
        cidade_destino = input("\n Cidade de destino: ")
        num_escalas = int(input("\n Insira o número de escalas: "))
        while (num_escalas < 0):
            print("\n => NÚMERO INVÁLIDO DE ESCALAS! DIGITE UM NÚMERO MAIOR OU IGUAL A ZERO <=")
            num_escalas = int(input("\n Insira o número de escalas: "))
        preco = float(input("\n Insira o valor: R$"))
        while (preco < 0):
            print("\n => PREÇO INVÁLIDO! DIGITE UM NÚMERO MAIOR OU IGUAL A ZERO <=")
            preco = float(input("\n Insira o valor: R$"))
        lugares_disponiveis = int(input("\n Insira o número de lugares disponíveis: "))
        while (lugares_disponiveis < 0):
            print("\n => NÚMERO INVÁLIDO DE LUGARES! DIGITE UM NÚMERO MAIOR OU IGUAL A ZERO <=")
            lugares_disponiveis = int(input("\n Insira o número de lugares disponíveis: "))
        passagens_vendidas = []

        voos[num_voo1] = [cidade_origem, cidade_destino, num_escalas, preco, lugares_disponiveis, passagens_vendidas]

        lista_voos.append([num_voo1, cidade_origem, cidade_destino, num_escalas, preco, lugares_disponiveis])


def mostrar_voos_disponiveis():
    print("\n\n\t\t -*- VOOS DISPONÍVEIS -*-")
    if not voos:
        print("\n => NENHUM VOOS CADASTRADO NO SISTEMA <= ")
    else:
        for i in range (len(lista_voos)) :
            if lista_voos[i][5] > 0 :
                print(f"\n >> Voo: {lista_voos[i][0]} | Origem: {lista_voos[i][1]} | Destino: {lista_voos[i][2]} | Escalas: {lista_voos[i][3]} | Preço: R$ {lista_voos[i][4]:.2f} | Lugares disponíveis: {lista_voos[i][5]}")


def menu_consulta():
    print("\n\n\t\t -*- CONSULTAR VOOS -*- ")
    print("\n\n\t Como deseja consultar o voo? ")
    print("\n 1 - Pelo número do voo")
    print("\n 2 - Cidade de origem")
    print("\n 3 - Cidade de destino")

    menu_consulta = opcao_menu(1, 3)
    return menu_consulta


def pesquisa_voo():
    consulta_num = int(input("\n\n Qual voo deseja consultar?"))
    while (consulta_num not in voos.keys()):
        print("\n => VOOS NÃO CADASTRADO, TENTE NOVAMENTE <=")
        consulta_num = int(input("\n\n Qual voo deseja consultar?"))

    for num_voo, dados in voos.items():
        if consulta_num == num_voo:
            print(f"\n\n\t\t\t >> VOO {num_voo} <<")
            print(f"\n Cidade de origem: {dados[0]}")
            print(f"\n Cidade de destino: {dados[1]}")
            print(f"\n Número de escalas: {dados[2]}")
            print(f"\n Preço: R$ {dados[3]:.2f}")
            print(f"\n Lugares disponíveis: {dados[4]}")


def cidade_origem():
    consulta_origem = input("\n Insira a cidade de origem que deseja pesquisar: ").lower()
    
    encontrado = False
    for num_voo, dados in voos.items():
        if (consulta_origem == dados[0].lower()):
            print(f"\n\n\t\t\t >> VOO {num_voo} <<")
            print(f"\n Cidade de destino: {dados[1]}")
            print(f"\n Preço: R$ {dados[3]:.2f}")
            encontrado = True
    if not encontrado:
        print("\n => NENHUM VOO ENCONTRADO PARA ESTA CIDADE DE ORIGEM <=")


def cidade_destino():
    consulta_destino = input("\n Insira a cidade de destino que deseja pesquisar: ").lower()
    
    encontrado = False
    for num_voo, dados in voos.items():
        if (consulta_destino == dados[1].lower()):
            print(f"\n\n\t\t\t >> VOO {num_voo} <<")
            print(f"\n Cidade de origem: {dados[0]}")
            print(f"\n Preço: R$ {dados[3]:.2f}")
            encontrado = True
    if not encontrado:
        print("\n => NENHUM VOO ENCONTRADO PARA ESTA CIDADE DE DESTINO <=")


def menor_escala():
    print("\n\n\t\t -*- INFORMAR VOOS COM MENOR ESCALA -*- ")

    escala_origem = input("\n\n Insira a cidade de origem: ").lower()
    escala_destino = input("\n Insira a cidade de destino: ").lower()

    menor = 100
    voo = None

    for num_voo, dados in voos.items():
        if (dados[0].lower() == escala_origem and dados[1].lower() == escala_destino) :
            if (dados[2] < menor) :
                menor = dados[2]
                voo = num_voo
            else:
                if dados[2] == menor:
                    print(f"\n\n O voo de {escala_origem.upper()} para {escala_destino.upper()} com menor escala é o voo {num_voo} com {menor} escalas")
    
    if voo is not None:
        print(f"\n\n O voo de {escala_origem.upper()} para {escala_destino.upper()} com menor escala é o voo {voo} com {menor} escalas")
    else:
        print(f"\n => NENHUM VOO ENCONTRADO DE {escala_origem.upper()} PARA {escala_destino.upper()} <= ")
    

def listar_passageiros():
    print("\n\n\t\t -*- LISTAR PASSAGEIROS E LUGARES DE UM VOO -*-")

    consulta_voo = verificar_voo_compra()
    
    for num_voo, dados in voos.items():
        if (consulta_voo == num_voo):
            if len(dados[5]) > 0:
                for r in range(len(dados[5])):
                    print(f"\n\t Passageiro(a) {r+1}: {dados[5][r]}")
            else:
                print(f"\n\t Não há passageiros cadastrados para o voo {consulta_voo}.")
            print(f"\n\t O voo {num_voo} possui {dados[4]} lugares disponíveis")


def venda_passagem():
    print("\n\n\t\t -*- VENDA DE PASSAGEM -*-")
        
    cpf_venda = verificar_cpf()
    nome = input("\n Insira o nome completo do passageiro(a): ")
    fone = verificar_telefone()

    if (cpf_venda in passageiros.keys()):
        mostrar_voos_disponiveis()
        num_voo2 = verificar_voo_compra()

        if (num_voo2 in passageiros[cpf_venda][2]):
            print(f"\n => VOO JÁ FOI COMPRADO! INSIRA OUTRO CÓDIGO, POR FAVOR <=")
        else:
            if num_voo2 in voos.keys():
                if (voos[num_voo2][4] > 0):
                    voos[num_voo2][4] -= 1
                    voos[num_voo2][5].append(passageiros[cpf_venda][0]) 
                    passageiros[cpf_venda][2].append(num_voo2)
                    print(f"\n => PASSAGEM PARA O VOO {num_voo2} VENDIDA COM SUCESSO! <= ")
                else:
                    print("\n => NÃO HÁ LUGARES DISPONÍVEIS NESTE VOO <=")
            
    else:
        qt_voos = int(input("\n Quantos voos deseja comprar: "))

        passagens_compradas = [] 
        for n in range(qt_voos):
            mostrar_voos_disponiveis()
            num_voo3 = int(input("\n\n Insira o número do voo: "))

            if num_voo3 in voos.keys():
                if voos[num_voo3][4] > 0:
                    voos[num_voo3][4] -= 1
                    for i in range (len(lista_voos)) :
                        if (lista_voos[i][0] == num_voo3):
                            antes = lista_voos[i][5]
                            depois = antes - 1
                            lista_voos[i][5] = depois
                    voos[num_voo3][5].append(nome)
                    passagens_compradas.append(num_voo3)
                    passageiros[cpf_venda][2].append(passagens_compradas)
                    print(f"\n => PASSAGEM PARA O VOO {num_voo3} VENDIDA COM SUCESSO PARA {nome}! <= ")
                else:
                    print(f"\n => NÃO HÁ LUGARES DISPONÍVEIS NO VOO {num_voo3} <=")
        
        if (len(passagens_compradas) > 0):
            passageiros[cpf_venda] = [nome, fone, passagens_compradas]
        else:
            print("\n => NENHUMA PASSAGEM FOI COMPRADA PARA ESTE CPF <=")


def cancelar_passagem():
    print("\n\n\t\t -*- CANCELAMENTO DE PASSAGEM -*-")
    
    cpf_cancelamento = verificar_cpf()

    if cpf_cancelamento in passageiros.keys():
        voo_cancelar = verificar_voo_compra()
        
        if voo_cancelar in passageiros[cpf_cancelamento][2]:
            nome_passageiro_cancelar = passageiros[cpf_cancelamento][0]
            resposta = confirmar()
            if (resposta == 1) :
                passageiros[cpf_cancelamento][2].remove(voo_cancelar)
                
                if voo_cancelar in voos.keys():
                    voos[voo_cancelar][4] += 1
                    if nome_passageiro_cancelar in voos[voo_cancelar][5]:
                        voos[voo_cancelar][5].remove(nome_passageiro_cancelar)
                    print(f"\n => PASSAGEM DO VOO {voo_cancelar} PARA {nome_passageiro_cancelar} CANCELADA COM SUCESSO! <= ")
                
                if not passageiros[cpf_cancelamento][2]: 
                    del passageiros[cpf_cancelamento]
                    print(f"\n => O PASSAGEIRO COM CPF {cpf_cancelamento} NÃO POSSUI PASSAGEM PARA O VOO {voo_cancelar} <= ")
            else :
                print("\n => PASSAGEM NÃO CANCELADA! VOCÊ SERÁ DIRECIONADO PARA O MENU PRINCIPAL <=")
    else:
        print("\n => CPF NÃO ENCONTRADO NO CADASTRO DE PASSAGEIROS <= ")


def opcao_menu(i, f):
    menu = int(input(f"\n\n Insira de {i} a {f} qual opção deseja selecionar: "))
    while (menu < i or menu > f):
        print(f"\n => OPÇÃO INVÁLIDA! FAVOR SELECIONAR DE {i} A {f} <=")
        menu = int(input(f"\n\n Insira de {i} a {f} qual opção deseja selecionar: "))
    return menu


def verificar_cpf():
    cpf = input("\n\n Insira o CPF do passageiro para cancelamento no modelo xxx.xxx.xxx-xx: ")
    
    while (len(cpf) != 14 or not cpf[3] == '.' or not cpf[7] == '.' or not cpf[11] == '-'):
        print("\n => CPF INVÁLIDO! TENTE NOVAMENTE NO FORMATO XXX.XXX.XXX-XX <=")
        cpf = input("\n\n Insira o CPF do passageiro para o cancelamento no modelo xxx.xxx.xxx-xx: ")

    return cpf


def verificar_voo():
    num_voo = int(input("\n\n Insira o número do voo: "))
    while (num_voo in voos.keys()):
        print("\n => VOO JÁ EXISTENTE, TENTE NOVAMENTE <= ")
        num_voo = int(input("\n\n Insira o número do voo: "))
    while (num_voo < 100 or num_voo > 99999):
        print("\n => NÚMERO DE VOO INVÁLIDO! INSIRA UM NÚMERO DE 100 A 99999 <= ")
        num_voo = int(input("\n\n Insira o número do voo: "))

    return num_voo


def menu_telefone():
    print("\n\n Qual tipo de telefone deseja cadastrar?")
    print("\n 1 - Fixo")
    print("\n 2 - Celular")

    menu_telefone = opcao_menu(1, 2)
    return menu_telefone


def verificar_telefone():
    opcao_telefone = menu_telefone()

    if(opcao_telefone == 1):
        telefone = input("\n\n Insira o número de telefone no modelo (XX) XXXX-XXXX : ")
        while (telefone[0] != '(' or telefone[3] != ')' or telefone[4] != ' ' or telefone[9] != '-' or len(telefone) != 14):
            print("\n => TELEFONE FIXO INVÁLIDO! INSIRA NO FORMATO (XX) XXXX-XXXX <=")
            telefone = input("\n\n Insira o número de telefone no modelo (XX) XXXX-XXXX : ")
    else:
        telefone = input("\n\n Insira o número de telefone no modelo (XX) XXXXX-XXXX : ")
        while (telefone[0] != '(' or telefone[3] != ')' or telefone[4] != ' ' or telefone[10] != '-' or len(telefone) != 15):
            print("\n => TELEFONE CELULAR INVÁLIDO! INSIRA NO FORMATO (XX) XXXXX-XXXX <=")
            telefone = input("\n\n Insira o número de telefone no modelo (XX) XXXXX-XXXX : ")

    return telefone


def verificar_voo_compra():
    num_voo = int(input("\n\n Insira o número do voo: "))
    while (num_voo not in voos.keys()):
        print("\n => VOO NÃO EXISTENTE, TENTE NOVAMENTE <= ")
        num_voo = int(input("\n\n Insira o número do voo: "))
    
    return num_voo


def confirmar() :
    confirmar = int(input("\n Deseja mesmo cancelar a passagem? Digite 1 para 'SIM' e 2 para 'NÃO' : "))
    while (confirmar < 1 or confirmar > 2):
        print(f"\n => OPÇÃO INVÁLIDA! FAVOR SELECIONAR DE 1 OU 2 <=")
        confirmar = int(input("\n Deseja mesmo cancelar a passagem? Digite 1 para 'SIM' e 2 para 'NÃO' : "))
    return confirmar


voos = {}
lista_voos = []
passageiros = {}

menu1 = exibir_menu()

while (menu1 >=1 and menu1 <= 6):
    if (menu1 == 1):
        cadastro_voo()
        
    if (menu1 == 2):
        menu2 = menu_consulta()

        if (menu2 == 1):
            pesquisa_voo()
                
        if (menu2 == 2):
            cidade_origem()

        if (menu2 == 3):
            cidade_destino()

    if (menu1 == 3):
        menor_escala()

    if (menu1 == 4):
        listar_passageiros()

    if (menu1 == 5):
        venda_passagem()

    if (menu1 == 6):
        cancelar_passagem()

    if (menu1 == 7):
        break

    menu1 = exibir_menu()
        
print("\n\n\t\t -*- PROGRAMA ENCERRADO -*-")
