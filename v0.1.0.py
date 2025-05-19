print("\n\n\t\t -*- PROGRAMA DE ATENDENTE DE VOÔS -*-")

print("\n\n\t\t\t >> MENU <<")
print("\n 1 - Cadastrar voô")
print("\n 2 - Consultar voô")
print("\n 3 - Informar voô com menor escala")
print("\n 4 - Listar passageiros do voô")
print("\n 5 - Venda de passagem")
print("\n 6 - Cancelamento de passagem")

menu1 = int(input("\n\n Insira qual deseja selecionar (1 a 6): "))

while (menu1 < 1 or menu1 > 6) :
    print("\n => OPÇÃO INVÁLIDA! FAVOR SELECIONAR DE 1 A 6 <=")
    menu1 = int(input("\n\n Insira qual deseja selecionar (1 a 6): "))

while (menu1 >=1 and menu1 <= 6) :
    if (menu1 == 1) :
        print("\n\n\t\t -*- CADASTRAR UM VOÔ -*- ")

        voos = {}

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
            passageiros = []

            voos[num_voo1] = [cidade_origem, cidade_destino, num_escalas, preco, lugares_disponiveis, passageiros]



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
                print(f"\n\n\t\t\t >> VOÔ {num_voo} <<")
                print(f"\n Cidade de origem: {dados[0]}")
                print(f"\n Cidade de destino: {dados[1]}")
                print(f"\n Número de escalas: {dados[2]}")
                print(f"\n Preço: R$ {dados[3]:.2f}")
                print(f"\n Lugares disponíveis: {dados[4]}")
        
        if (menu2 == 2) :
            consulta_origem = input("\n Insira a cidade de origem que deseja pesquisar: ")
            consulta_origem = consulta_origem.lower()

            for num_voo, dados in voos.items() :
                if (consulta_origem == dados[0].lower()) :
                    print(f"\n\n\t\t\t >> VOÔ {num_voo} <<")
                    print(f"\n Cidade de destino: {dados[1]}")
                    print(f"\n Preço: R$ {dados[3]:.2f}")

        if (menu2 == 3) :
            consulta_destino = input("\n Insira a cidade de destino que deseja pesquisar: ")
            consulta_destino = consulta_destino.lower()

            for num_voo, dados in voos.items() :
                if (consulta_destino == dados[1].lower()) :
                    print(f"\n\n\t\t\t >> VOÔ {num_voo} <<")
                    print(f"\n Cidade de origem: {dados[0]}")
                    print(f"\n Preço: R$ {dados[3]:.2f}")


    if (menu1 == 3) :
        print("\n\n\t\t -*- INFORMAR VOÔ COM MENOR ESCALA -*- ")

        escala_origem = input("\n\n Insira a cidade de origem: ")
        escala_origem = escala_origem.lower()
        escala_destino = input("\n Insira a cidade de destino: ")
        escala_destino = escala_destino.lower()

        for num_voo, dados in voos.items():
            if (dados[0].lower() == escala_origem and dados[1].lower() == escala_destino) :
                menor = 100
                if (dados[2] <= menor) :
                    menor = dados[2]
                    voo = num_voo
        
        print(f"\n\n O voô de {escala_origem} para {escala_destino} com menor escala é o voô {voo} com {menor} escalas")

    if (menu1 == 4) :
        print("\n\n\t\t -*- LISTAR PASSAGEIROS E LUGARES DE UM VOÔ -*-")

        consulta_voo = int(input("\n\n Insira o código do voô: "))
        while (consulta_voo not in voos.keys()) :
            print("\n => VOÔ NÃO CADASTRADO, TENTE NOVAMENTE <=")
            consulta_voo = int(input("\n\n Insira o código do voô: "))
        
        for num_voo, dados in voos.items() :
            if (consulta_voo == num_voo) :
                for r in range(len(dados[5])) :
                    print(f"\n Passageiro(a) {r+1}: {dados[5][r]}")
                print(f"\n O voô {num_voo} possui {dados[4]} lugares disponíveis")


    if (menu1 == 5) :
        print("\n\n\t\t -*- VENDA DE PASSAGEM -*-")

        passageiros = {}
        
        cpf = input("\n\n Insira o CPF do passageiro no modelo xxx.xxx.xxx-xx: ")
        while (len(cpf) < 14 or len(cpf) > 14) :
                print("\n => CPF INVÁLIDO! TENTE NOVAMENTE NO FORMATO XXX.XXX.XXX-XX <=")
                cpf = input("\n\n Insira o CPF do passageiro no modelo xxx.xxx.xxx-xx: ")

        if (cpf in passageiros.keys()) :
            num_voo2 = int(input("\n Insira o número do voô: "))
            # inserir o voo na lista [passagens] dentro de {passageiros}

        else:
            qt_voos = int(input("\n Quantos voôs deseja comprar: "))

            for n in range(qt_voos) :
                nome = input("\n Insira o nome completo do passageiro(a): ")
                num_voo3 = int(input("\n Insira o número do voô: "))
                while (num_voo3 < 100 or num_voo3 > 99999):
                    print("\n => NÚMERO DE VOÔ INVÁLIDO! INSIRA UM NÚMERO DE 100 A 9999 <= ")
                    num_voo3 = int(input("\n\n Insira o número do voô: "))
                if (n == 0) :
                    passageiros[cpf] = [nome, [num_voo3]]
                else :
                    passageiros[cpf][2][n + 1] = num_voo3

        # inserir redução de lugares disponíveis
        

    print("\n\n\t\t -*- PROGRAMA DE ATENDENTE DE VOÔS -*-")

    print("\n\n\t\t\t >> MENU <<")
    print("\n 1 - Cadastrar voô")
    print("\n 2 - Consultar voô")
    print("\n 3 - Informar voô com menor escala")
    print("\n 4 - Listar passageiros do voô")
    print("\n 5 - Venda de passagem")
    print("\n 6 - Cancelamento de passagem")

    menu1 = int(input("\n\n Insira qual deseja selecionar (1 a 6) - Zero para sair do programa: "))
        
        
