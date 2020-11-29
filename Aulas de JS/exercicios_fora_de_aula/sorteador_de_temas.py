from random import shuffle
sim_ou_nao = str(input('Vamos juntar os temas com os grupos?')).strip().upper()
if sim_ou_nao == 'SIM':
    print('Vamos lá!')
    quantidade_de_alunos = int(input('Quantos alunos serão sorteados?'))
    quantidade_de_temas = int(input('E os temas?'))
    if quantidade_de_alunos == quantidade_de_temas:
        if quantidade_de_alunos == 2:
            # alunos
            al1 = str(input('Primeiro grupo/estudante: ')).strip().capitalize() # pede o 1° aluno
            al2 = str(input('Segundo grupo/estudante: ')).strip().capitalize() # pede o 2° aluno
            print('----------------------')
            #temas
            tema1 = str(input('Primeiro tema: ')).strip().capitalize() # pede os temas
            tema2 = str(input('Segundo tema: ')).strip().capitalize()
            print('----------------------')
            # listas
            lista_alunos = [al1, al2] # lista os alunos
            lista_temas = [tema1, tema2] # lista os temas
            shuffle(lista_temas) # embaralha os temas
            print('Legal! Já temos uma ordem!\nEla é...')
            # indica a ordem sorteada...
            print('{} ficou com {}'.format(lista_alunos[0], lista_temas[0]))
            print('{} ficou com {}'.format(lista_alunos[1], lista_temas[1]))
        if quantidade_de_alunos == 3:
            # alunos
            al1 = str(input('Primeiro grupo/estudante: ')).strip().capitalize() # pede o 1° aluno
            al2 = str(input('Segundo grupo/estudante: ')).strip().capitalize() # pede o 2° aluno
            al3 = str(input('Terceiro grupo/estudante: ')).strip().capitalize()
            print('----------------------')
            # temas
            tema1 = str(input('Primeiro tema: ')).strip().capitalize() # pede os temas
            tema2 = str(input('Segundo tema: ')).strip().capitalize()
            tema3 = str(input('Terceiro tema: ')).strip().capitalize()
            print('----------------------')
            # listas
            lista_alunos = [al1, al2, al3] # lista os alunos
            lista_temas = [tema1, tema2, tema3] # lista os temas
            shuffle(lista_temas) # embaralha os alunos
            print('Legal! Já temos uma ordem!\nEla é...')
            # indica a ordem sorteada...
            print('{} ficou com {}'.format(lista_alunos[0], lista_temas[0]))
            print('{} ficou com {}'.format(lista_alunos[1], lista_temas[1]))
            print('{} ficou com {}'.format(lista_alunos[2], lista_temas[2]))
        if quantidade_de_alunos == 4:
            # alunos
            al1 = str(input('Primeiro grupo/estudante: ')).strip().capitalize() # pede o 1° aluno
            al2 = str(input('Segundo grupo/estudante: ')).strip().capitalize() # pede o 2° aluno
            al3 = str(input('Terceiro grupo/estudante: ')).strip().capitalize()
            al4 = str(input('Quarto grupo/estudante: ')).strip().capitalize()
            print('----------------------')
            # temas
            tema1 = str(input('Primeiro tema: ')).strip().capitalize() # pede os temas
            tema2 = str(input('Segundo tema: ')).strip().capitalize()
            tema3 = str(input('Terceiro tema: ')).strip().capitalize()
            tema4 = str(input('Quarto tema: ')).strip().capitalize()
            print('----------------------')
            #listas
            lista_alunos = [al1, al2, al3, al4] # lista os alunos
            lista_temas = [tema1, tema2, tema3, tema4] # lista os temas
            shuffle(lista_temas) # embaralha os alunos
            print('Legal! Já temos uma ordem!\nEla é...')
            # indica a ordem sorteada...
            print('{} ficou com {}'.format(lista_alunos[0], lista_temas[0]))
            print('{} ficou com {}'.format(lista_alunos[1], lista_temas[1]))
            print('{} ficou com {}'.format(lista_alunos[2], lista_temas[2]))
            print('{} ficou com {}'.format(lista_alunos[3], lista_temas[3]))
        if quantidade_de_alunos == 5:
            # alunos
            al1 = str(input('Primeiro grupo/estudante: ')).strip().capitalize() # pede o 1° aluno
            al2 = str(input('Segundo grupo/estudante: ')).strip().capitalize() # pede o 2° aluno
            al3 = str(input('Terceiro grupo/estudante: ')).strip().capitalize()
            al4 = str(input('Quarto grupo/estudante: ')).strip().capitalize()
            al5 = str(input('Quinto grupo/estudante: ')).strip().capitalize()
            print('----------------------')
            # temas
            tema1 = str(input('Primeiro tema: ')).strip().capitalize() # pede os temas
            tema2 = str(input('Segundo tema: ')).strip().capitalize()
            tema3 = str(input('Terceiro tema: ')).strip().capitalize()
            tema4 = str(input('Quarto tema: ')).strip().capitalize()
            tema5 = str(input('Quarto tema: ')).strip().capitalize()
            print('----------------------')
            #listas
            lista_alunos = [al1, al2, al3, al4, al5] # lista os alunos
            lista_temas = [tema1, tema2, tema3, tema4, tema5] # lista os temas
            shuffle(lista_temas) # embaralha os alunos
            print('Legal! Já temos uma ordem!\nEla é...')
            # indica a ordem sorteada...
            print('{} ficou com {}'.format(lista_alunos[0], lista_temas[0]))
            print('{} ficou com {}'.format(lista_alunos[1], lista_temas[1]))
            print('{} ficou com {}'.format(lista_alunos[2], lista_temas[2]))
            print('{} ficou com {}'.format(lista_alunos[3], lista_temas[3]))
            print('{} ficou com {}'.format(lista_alunos[4], lista_temas[4]))
        if quantidade_de_alunos >= 6:
            print('há muitos alunos, reinicie...')
    else:
        print('A quantidade de alunos é diferente da quantidade de temas...')
        print('Reinicie o sorteio...')

print('_FIM_')