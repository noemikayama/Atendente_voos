 for num_voo, dados in voos.items():
        if (dados[0].lower() == escala_origem and dados[1].lower() == escala_destino) :
            if (dados[2] < menor) :
                menor = dados[2]
                voo = num_voo
            else:
                if dados[2] == menor:
                    print(f"\n\n O voô de {escala_origem} para {escala_destino} com menor escala é o voô {num_voo} com {menor} escalas")
    
    if voo is not None:
        print(f"\n\n O voô de {escala_origem} para {escala_destino} com menor escala é o voô {voo} com {menor} escalas")
    else:
        print(f"\n => NENHUM VOÔ ENCONTRADO DE {escala_origem} PARA {escala_destino} <= ")