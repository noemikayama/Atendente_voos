def exibir_menu():
    """Exibe o menu principal do programa de atendimento de voôs e retorna a opção escolhida."""
    print("\n\n\t\t -*- PROGRAMA DE ATENDENTE DE VOÔS -*-")
    print("\n\n\t\t\t >> MENU <<")
    print("\n 1 - Cadastrar voô")
    print("\n 2 - Consultar voô")
    print("\n 3 - Informar voô com menor escala")
    print("\n 4 - Listar passageiros do voô")
    print("\n 5 - Venda de passagem")
    print("\n 6 - Cancelamento de passagem")

    menu_opcao = int(input("\n\n Insira qual deseja selecionar (1 a 6) - Zero para sair do programa: "))

    while (menu_opcao < 0 or menu_opcao > 6):
        print("\n => OPÇÃO INVÁLIDA! FAVOR SELECIONAR DE 1 A 6 OU 0 PARA SAIR <=")
        menu_opcao = int(input("\n\n Insira qual deseja selecionar (1 a 6) - Zero para sair do programa: "))
    
    return menu_opcao

voos = {}
passageiros = {} 

menu1 = exibir_menu() 

while (menu1 >=1 and menu1 <= 6) :
    if (menu1 == 1) :
        print("\n\n\t\t -*- CADASTRAR UM VOÔ -*- ")

        num1 = int(input("\n\n Insira quantos voôs deseja cadastrar: "))
                        
        for i in range(num1) :
            num_voo1 = int(input("\n\n Insira o número do voô: "))
            while (num_voo1 in voos.keys()) :
                print("\n => VOÔ JÁ EXISTENTE, TENTE NOVAMENTE <= ")
                num_voo1 = int(input("\n\n Insira o número do voô: "))
            while (num_voo1 < 100 or num_voo1 > 99999):
                print("\n => NÚMERO DE VOÔ INVÁLIDO! INSIRA UM NÚMERO DE 100 A 9999 <= ")
                num_voo1 = int(input("\n\n Insira o número do voô: "))
            cidade_origem = input("\n Cidade de origem: ")
            cidade_destino = input("\n Cidade de destino: ")
            num_escalas = int(input("\n Insira o número de escalas: "))
            preco = float(input("\n Insira o valor: R$"))
            lugares_disponiveis = int(input("\n Insira o número de lugares disponíveis: "))
            passagens = []

            voos[num_voo1] = [cidade_origem, cidade_destino, num_escalas, preco, lugares_disponiveis, passagens]



    if (menu1 == 2) :
        print("\n\n\t\t -*- CONSULTAR VOÔ -*- ")
        print("\n\n\t Como deseja consultar o voô? ")
        print("\n 1 - Pelo número do voô")
        print("\n 2 - Cidade de origem")
        print("\n 3 - Cidade de destino")

        menu2 = int(input("\n\n Insira de 1 a 3 qual opção deseja selecionar: "))
        while (menu2 < 1 or menu2 > 3):
            print("\n => OPÇÃO INVÁLIDA! FAVOR SELECIONAR DE 1 A 3 <=")
            menu2 = int(input("\n\n Insira de 1 a 3 qual opção deseja selecionar: "))

        if (menu2 == 1) :
            consulta_num = int(input("\n\n Qual voô deseja consultar?"))
            while (consulta_num not in voos.keys()) :
                print("\n => VOÔ NÃO CADASTRADO, TENTE NOVAMENTE <=")
                consulta_num = int(input("\n\n Qual voô deseja consultar?"))

            for num_voo, dados in voos.items() :
                if consulta_num == num_voo:
                    print(f"\n\n\t\t\t >> VOÔ {num_voo} <<")
                    print(f"\n Cidade de origem: {dados[0]}")
                    print(f"\n Cidade de destino: {dados[1]}")
                    print(f"\n Número de escalas: {dados[2]}")
                    print(f"\n Preço: R$ {dados[3]:.2f}")
                    print(f"\n Lugares disponíveis: {dados[4]}")
                
        if (menu2 == 2) :
            consulta_origem = input("\n Insira a cidade de origem que deseja pesquisar: ")
            consulta_origem = consulta_origem.lower()
            
            encontrado = False
            for num_voo, dados in voos.items() :
                if (consulta_origem == dados[0].lower()) :
                    print(f"\n\n\t\t\t >> VOÔ {num_voo} <<")
                    print(f"\n Cidade de destino: {dados[1]}")
                    print(f"\n Preço: R$ {dados[3]:.2f}")
                    encontrado = True
            if not encontrado:
                print("\n => NENHUM VOÔ ENCONTRADO PARA ESTA CIDADE DE ORIGEM <=")

        if (menu2 == 3) :
            consulta_destino = input("\n Insira a cidade de destino que deseja pesquisar: ")
            consulta_destino = consulta_destino.lower()
            
            encontrado = False
            for num_voo, dados in voos.items() :
                if (consulta_destino == dados[1].lower()) :
                    print(f"\n\n\t\t\t >> VOÔ {num_voo} <<")
                    print(f"\n Cidade de origem: {dados[0]}")
                    print(f"\n Preço: R$ {dados[3]:.2f}")
                    encontrado = True
            if not encontrado:
                print("\n => NENHUM VOÔ ENCONTRADO PARA ESTA CIDADE DE DESTINO <=")


    if (menu1 == 3) :
        print("\n\n\t\t -*- INFORMAR VOÔ COM MENOR ESCALA -*- ")

        escala_origem = input("\n\n Insira a cidade de origem: ")
        escala_origem = escala_origem.lower()
        escala_destino = input("\n Insira a cidade de destino: ")
        escala_destino = escala_destino.lower()

        menor = 100
        voo = None

        for num_voo, dados in voos.items():
            if (dados[0].lower() == escala_origem and dados[1].lower() == escala_destino) :
                if (dados[2] <= menor) :
                    menor = dados[2]
                    voo = num_voo
        
        if voo is not None:
            print(f"\n\n O voô de {escala_origem} para {escala_destino} com menor escala é o voô {voo} com {menor} escalas")
        else:
            print(f"\n => NENHUM VOÔ ENCONTRADO DE {escala_origem} PARA {escala_destino} <= ")


    if (menu1 == 4) :
        print("\n\n\t\t -*- LISTAR PASSAGEIROS E LUGARES DE UM VOÔ -*-")

        consulta_voo = int(input("\n\n Insira o código do voô: "))
        while (consulta_voo not in voos.keys()) :
            print("\n => VOÔ NÃO CADASTRADO, TENTE NOVAMENTE <=")
            consulta_voo = int(input("\n\n Insira o código do voô: "))
        
        for num_voo, dados in voos.items() :
            if (consulta_voo == num_voo) :
                if len(dados[5]) > 0:
                    for r in range(len(dados[5])) :
                        print(f"\n\t Passageiro(a) {r+1}: {dados[5][r]}")
                else:
                    print(f"\n\t Não há passageiros cadastrados para o voô {consulta_voo}.")
                print(f"\n\t O voô {num_voo} possui {dados[4]} lugares disponíveis")


    if (menu1 == 5) :
        print("\n\n\t\t -*- VENDA DE PASSAGEM -*-")

        
        cpf = input("\n\n Insira o CPF do passageiro no modelo xxx.xxx.xxx-xx: ")
        while (len(cpf) < 14 or len(cpf) > 14 or not cpf[3] == '.' or not cpf[7] == '.' or not cpf[11] == '-') :
                print("\n => CPF INVÁLIDO! TENTE NOVAMENTE NO FORMATO XXX.XXX.XXX-XX <=")
                cpf = input("\n\n Insira o CPF do passageiro no modelo xxx.xxx.xxx-xx: ")

        if (cpf in passageiros.keys()) :
            num_voo2 = int(input("\n Insira o número do voô: "))
            if (num_voo2 in passageiros[cpf][1]): 
                print(f"\n => VOÔ JÁ FOI COMPRADO! INSIRA OUTRO CÓDIGO, POR FAVOR <=")
            else:
                if num_voo2 in voos.keys():
                    if voos[num_voo2][4] > 0:
                        voos[num_voo2][4] -= 1
                        voos[num_voo2][5].append(passageiros[cpf][0]) 
                        passageiros[cpf][1].append(num_voo2)
                        print(f"\n => PASSAGEM PARA O VOÔ {num_voo2} VENDIDA COM SUCESSO! <= ")
                    else:
                        print("\n => NÃO HÁ LUGARES DISPONÍVEIS NESTE VOÔ <=")
                else:
                    print("\n => VOÔ NÃO CADASTRADO <=")
                
        else:
            nome = input("\n Insira o nome completo do passageiro(a): ")
            qt_voos = int(input("\n Quantos voôs deseja comprar: "))

            passagens_compradas = [] 
            for n in range(qt_voos) :
                num_voo3 = int(input(f"\n Insira o código do {n+1}º voô: "))
                while (num_voo3 < 100 or num_voo3 > 99999):
                    print("\n => NÚMERO DE VOÔ INVÁLIDO! INSIRA UM NÚMERO DE 100 A 99999 <= ")
                    num_voo3 = int(input(f"\n Insira o código do {n+1}º voô: "))
                while (num_voo3 not in voos.keys()) :
                    print("\n => VOÔ NÃO CADASTRADO, TENTE NOVAMENTE <=")
                    num_voo3 = int(input(f"\n Insira o código do {n+1}º voô: "))

                if num_voo3 in voos.keys():
                    if voos[num_voo3][4] > 0:
                        voos[num_voo3][4] -= 1
                        voos[num_voo3][5].append(nome)
                        passagens_compradas.append(num_voo3)
                        print(f"\n => PASSAGEM PARA O VOÔ {num_voo3} VENDIDA COM SUCESSO PARA {nome}! <= ")
                    else:
                        print(f"\n => NÃO HÁ LUGARES DISPONÍVEIS NO VOÔ {num_voo3} <=")
            
            if passagens_compradas:
                passageiros[cpf] = [nome, passagens_compradas]
            else:
                print("\n => NENHUMA PASSAGEM FOI COMPRADA PARA ESTE CPF <=")

    if (menu1 == 6) :
        print("\n\n\t\t -*- CANCELAMENTO DE PASSAGEM -*-")

        cpf_cancelamento = input("\n\n Insira o CPF do passageiro para cancelamento no modelo xxx.xxx.xxx-xx: ")
        while (len(cpf_cancelamento) != 14 or not cpf_cancelamento[3] == '.' or not cpf_cancelamento[7] == '.' or not cpf_cancelamento[11] == '-'):
            print("\n => CPF INVÁLIDO! TENTE NOVAMENTE NO FORMATO XXX.XXX.XXX-XX <=")
            cpf_cancelamento = input("\n\n Insira o CPF do passageiro para o cancelamento no modelo xxx.xxx.xxx-xx: ")

        if cpf_cancelamento in passageiros.keys():
            voo_cancelar = int(input("\n Insira o número do voô que deseja cancelar: "))
            
            if voo_cancelar in passageiros[cpf_cancelamento][1]:
                nome_passageiro_cancelar = passageiros[cpf_cancelamento][0]
                passageiros[cpf_cancelamento][1].remove(voo_cancelar)
                
                if voo_cancelar in voos.keys():
                    voos[voo_cancelar][4] += 1
                    if nome_passageiro_cancelar in voos[voo_cancelar][5]:
                        voos[voo_cancelar][5].remove(nome_passageiro_cancelar)
                print(f"\n => PASSAGEM DO VOÔ {voo_cancelar} PARA {nome_passageiro_cancelar} CANCELADA COM SUCESSO! <= ")
                
                if not passageiros[cpf_cancelamento][1]: 
                    del passageiros[cpf_cancelamento]
            else:
                print(f"\n => O PASSAGEIRO COM CPF {cpf_cancelamento} NÃO POSSUI PASSAGEM PARA O VOÔ {voo_cancelar} <= ")
        else:
            print("\n => CPF NÃO ENCONTRADO NO CADASTRO DE PASSAGEIROS <= ")


    menu1 = exibir_menu() 
        
print("\n\n\t\t -*- PROGRAMA ENCERRADO -*-")