from time import sleep

while True:
    print('=' * 100)
    print('-' * 100)
    print('Isso é só uma tela interativa aonde voçé pode interagir com diversos programas criados por mim')
    print('-' * 100)
    print('=' * 100)

    sleep(1)

    print('Agora escolha qual programa voçé quer rodar no terminal')
    sleep(1)
    print('1 = sistema de passagns de uma rodoviaria')
    sleep(1)
    print('2 = sistema escolar')
    sleep(1)
    print('3 = calculadora de velocidade média')
    sleep(1)
    print('4 = calculadora simples')
    sleep(1)
    print('-' * 40)
    sleep(1)
    es_sis_prin = input(':')

    if es_sis_prin == '1' or es_sis_prin == 'um':
        while True:
            print('SISTEMA RODOVIARIO')

            print('-' * 40)
            print('Bem vindo a rodoviaria')
            print('-' * 40)
            sleep(1)
            op_sistema_inicial = input('Deseja prossegui com a compra?:').lower()
            if op_sistema_inicial == 'sim' or op_sistema_inicial == '1':
                print('-' * 40)
                sleep(1)
                print('Para qual estado voçé desejar ir?')
                sleep(1)
                print('1 Rio de Janeiro: R$ 250 ')
                sleep(1)
                print('2 São Paulo R$ 150')
                sleep(1)
                print('3 Minas Gerais R$ 300')
                sleep(1)
                print('4 Curitiba R$ 450')
                sleep(1)
                print('-' * 40)
                op_sistema_inicial_2 = input(':')

                if op_sistema_inicial_2 == '1' or op_sistema_inicial_2 == 'um':

                    pass_rio = int(input('Quantas passagem para o Rio de Janerio?:'))
                    conta_da_passagem = pass_rio * 250

                    while True:
                        sleep(1)
                        print('-' * 40)
                        print('O valor total das passagens fica R$ {} '.format(conta_da_passagem))
                        sleep(1)
                        print('Agora escolha a forma de pagamento')
                        sleep(1)
                        print('-' * 40)
                        print('1 Cartão de credito a vista: 20% de desconto')
                        sleep(1)
                        print('2 Cartão de credito parcelado em 2x: 10% de desconto')
                        sleep(1)
                        print('3 Cartão de credito parcelado em 3x: sem desconto no valor total')
                        sleep(1)
                        print('-' * 40)
                        op_cart = input(':')
                        sleep(1)

                        if op_cart == '1' or op_cart == 'um':
                            conta_desconto = (conta_da_passagem * 20) / 100
                            print('Otima escolha, o valor total das passagens com o desconto vai ser de R${}'.format(
                                conta_da_passagem - conta_desconto))
                            sleep(1)
                            print('tenha uma boa viagem')
                            break

                        elif op_cart == '2' or op_cart == 'dois':
                            cont_desconto_2 = conta_da_passagem - ((conta_da_passagem * 10) / 100)
                            print('Otima escolha, o valor total das passagns com desconto ficara R${}'.format(
                                cont_desconto_2))
                            sleep(1)
                            print('tenha uma boa viagem')
                            break

                        elif op_cart == '3' or op_cart == 'tres':
                            print('Não havera desconto na sua viagem, o valor total dela será de R${}'.format(
                                conta_da_passagem))
                            sleep(1)
                            print('tenha uma boa viagem')
                            break

                        else:
                            print('opção invalida')


    elif es_sis_prin == '2' or es_sis_prin == 'dois':

        from time import sleep

        while True:
            print('-' * 40)
            print('''
        Bem vindo ao sistema da escola
        em que área você deseja entrar?
        1 = média dos alunos
        2 = chamada dos alunos
        3 = orçamento 
        4 = sair 
        controles:
        Pode ser escrito 1 ou um no sistema principal
        e o numero 1 e 2 pode ser usado como sim e não''')
            print('-' * 40)

            opção_sistema = input(':')

            if opção_sistema == '4' or opção_sistema == 'quatro':
                print('encerrando')
                sleep(3)
                break

            elif opção_sistema == '3' or opção_sistema == 'três':
                while True:
                    orcamento = 138000
                    print('''
        Esse é o orçamento da escola:''')
                    sleep(1)
                    print(orcamento)

                    op_orcamento = input('Você deseja adicionar uma renda?:')
                    if op_orcamento == 'sim' or op_orcamento == '1':
                        print('quantos Reais você deseja adicionar?')

                        op_orcamento_1 = float(input('R$:'))

                        ops = op_orcamento_1 + orcamento

                        print('o orçamento atual da escola é')
                        sleep(1)
                        print(ops)

                        op_orcamento_final = input('você deseja adicionar mais algum valor?:')

                        if op_orcamento_final == 'sim' or op_orcamento_final == '1':
                            print('vamos lá então')

                        elif op_orcamento_final == 'não' or op_orcamento_final == '2':
                            print('encerrando')
                            sleep(3)
                            break




            elif opção_sistema == '2' or opção_sistema == 'dois':
                while True:
                    chamada = ['Arthur', 'Gabriel', 'Guilherme', 'Lucas', 'espaço vazio']

                    print('''
        Essa é a chamada da turma 1181''')
                    print(chamada)
                    print('-' * 40)
                    sleep(1)
                    ad_cham = input('você deseja adicionar um aluno a chamada?')

                    if ad_cham == 'sim' or ad_cham == '1':
                        print('-' * 40)
                        ad = input('adicione um nome:')
                        print('-' * 40)

                        chamada[4] = ad

                        print(chamada)
                        op_chamada_final = input('Deseja Adicionar um novo nome?')

                        if op_chamada_final == 'sim' or op_chamada_final == '1':
                            print('vamos lá')

                        elif op_chamada_final == 'não' or op_chamada_final == '2':
                            print('encerrando')
                            sleep(3)
                            break

                    elif ad_cham == 'não' or ad_cham == '2':
                        print('encerrando')
                        sleep(3)
                        break

            if opção_sistema == '1' or opção_sistema == 'um':
                while True:
                    médias = [8.5, 9.0, 8.1, 0, 0, 0, 0, 0]

                    print('''
        Bem vindo a media dos alunos
        aqui dentro você verá as médias
        da turma 1181 da FaeTec''')
                    sleep(1)
                    print('''
        médias:''')
                    sleep(1)
                    print(médias)
                    sleep(1)
                    print('''
        opções aceitas:sim ou 1, não ou 2''')

                    opção_médias = input('deseja adicionar mais uma média:')

                    if opção_médias == 'não' or opção_médias == '2':
                        print('encerrando')
                        sleep(3)
                        break

                    elif opção_médias == 'sim' or opção_médias == '1':
                        op_nota = float(input('qual a nota do aluno?'))
                        médias[3] = op_nota

                        print('''
        adicionando a média''')
                        sleep(1)
                        print(médias)

                        op_média_final = input('deseja adicionar uma média nova?:')

                        if op_média_final == 'sim' or op_média_final == '1':
                            print('retornando o programa')

                        elif op_média_final == 'não' or op_média_final == '2':
                            print('programa encerrado')
                            sleep(1)
                            break

    elif es_sis_prin == '3' or es_sis_prin == 'tres':
        print('=' * 40)
        print('-' * 40)
        print('CALCULADORA DE VALOCIDADE MÉDIA:')
        print('-' * 40)
        print('=' * 40)


        sleep(1)
        print('vamos começar, primeiramente me informe a posição final e inicial do seu problema')
        sleep(1)
        si = float(input('Si:'))
        sleep(1)
        sf = float(input('Sf:'))
        sleep(1)
        print('Otimo :) agora me informa do Ti e o Tf')
        ti = int(input('Ti:'))
        tf = int(input('Tf:'))
        sleep(1)
        print('muito obrigado, vou fazer os calculos pra voçé')
        cal_si = sf - si
        cal_tf = tf - ti
        vm = cal_si / cal_tf
        print('Aqui está, a velocidade média da sua operação é de {}km/h'.format(vm))
        print('-' * 40)
        op = input('Deseja saber a sua aceleração?')

        if op == 'sim':
            acl = vm / cal_tf
            print('a sua aceleração é de {}km/h'.format(acl))



    elif es_sis_prin == '4' or es_sis_prin == 'quatro':
        while True:
            print('=' * 40)
            print('-' * 40)
            print('BEM VINDO A CALCULADORA GERAL')
            print('-' * 40)
            print('=' * 40)

            sleep(1)

            print('Escolha a sua operação:')
            print('1 = soma')
            sleep(1)
            print('2 = subtração')
            sleep(1)
            print('3 = divisão')
            sleep(1)
            print('4 = vezes')
            es_cal = input(':')

            if es_cal == '1' or es_cal == 'um':
                while True:
                    soma_1 = float(input('escolha um numero paa somar com o proximo:'))
                    soma_2 = float(input('escolha o proximo numero:'))
                    cal_soma = soma_1 + soma_2
                    print('resultado:{}'.format(cal_soma))

                    soma_nova = input('deseja somar novamente?:')

                    if soma_nova == '1' or soma_nova == 'sim':
                        print('reiniciando o programa')

                    elif soma_nova == '2' or soma_nova == 'não':
                        print('encerrrando o programa')
                        break

                    else:
                        print('opção invalida')


            elif es_cal == '2' or es_cal == 'dois':
                while True:
                    sub_1 = float(input('escolha um numero para a subtração:'))
                    sub_2 = float(input('escolha outro:'))

                    cal_sub = sub_1 - sub_2

                    print('o resultado da operação é de {}'.format(cal_sub))


                    es_sub = input('deseja subtrair novamente?:')

                    if es_sub == 'sim' or es_sub == '1':
                        print('reiniciando o programa')

                    elif es_sub == 'não' or es_sub == '2':
                        print('encerrando o programa')

                    else:
                        print('opção invalida')



            elif es_cal == '3' or es_cal == 'tres':
                while True:
                    div_1 = float(input('escolha um numero para divisão:'))
                    div_2 = float(input('escolha mais um:'))

                    cal_div = div_1 / div_2

                    print('resultado :{]'.format(cal_div))

                    es_div = input('deseja dividir novamente?:')

                    if es_div == 'sim' or es_div == '1':
                        print('reiniciando o programa')

                    elif es_div == 'não' or es_div == '2':
                        print('encerando o programa')
                        break

                    else:
                        print('opção invalida')

            elif es_cal == '4' or es_cal == 'quatro':
                while True:
                    x_1 = float(input('escolha um numero para a multiplicação:'))
                    x_2 = float(input('escolha mais um numero:'))

                    conta_x = x_1 * x_2

                    print('resultado:{}'.format(conta_x))

                    es_x = input('deseja multiplicar novamente:')

                    if es_x == '1' or es_x == 'sim':
                        print('reiniciando o programa')

                    elif es_x == '2' or es_x == 'não':
                        print('encerrando o programa')
                        break

                    else:
                        print('opção invalida')



