from random import shuffle
print('Sorteador (somente até 8 grupos/pessoas)...')
numero_de_alunos = int(input('Qual a quantidade de grupos para se sortear?'))
#vairáveis para cada estudante/grupo
#se for 2 
if numero_de_alunos == 2:
    al1 = str(input('Primeiro grupo/estudante: '))# pede o 1° aluno
    al2 = str(input('Segundo grupo/estudante: '))# pede o 2° aluno
    lista = [al1, al2] # lista os dois
    shuffle(lista) # embaralha a lista
    print('A ordem dos grupos/estudantes é: {}'.format(lista)) # mostra a lista embaralhada
#se for 3 
if numero_de_alunos == 3:
    al1 = str(input('Primeiro grupo/estudante: '))# pede o 1° aluno
    al2 = str(input('Segundo grupo/estudante: '))# pede o 2° aluno
    al3 = str(input('Terceiro grupo/estudante: '))
    lista = [al1, al2, al3] # lista os dois
    shuffle(lista) # embaralha a lista
    print('A ordem dos grupos/estudantes é: {}'.format(lista)) # mostra a lista embaralhada
#se for 4
if numero_de_alunos == 4:
    al1 = str(input('Primeiro grupo/estudante: '))# pede o 1° aluno
    al2 = str(input('Segundo grupo/estudante: '))# pede o 2° aluno
    al3 = str(input('Terceiro grupo/estudante: '))
    al4 = str(input('Quarto grupo/estudante: '))
    lista = [al1, al2, al3, al4] # lista os dois
    shuffle(lista) # embaralha a lista
    print('A ordem dos grupos/estudantes é: {}'.format(lista)) # mostra a lista embaralhada
#se for 5
if numero_de_alunos == 5:
    al1 = str(input('Primeiro grupo/estudante: '))# pede o 1° aluno
    al2 = str(input('Segundo grupo/estudante: '))# pede o 2° aluno
    al3 = str(input('Terceiro grupo/estudante: '))
    al4 = str(input('Quarto grupo/estudante: '))
    al5 = str(input('Quinto grupo/estudante: '))
    lista = [al1, al2, al3, al4, al5]
    shuffle(lista)
    print('A ordem dos grupos/estudantes é: {}'.format(lista))
#se for 6
if numero_de_alunos == 6:
    al1 = str(input('Primeiro grupo/estudante: '))# pede o 1° aluno
    al2 = str(input('Segundo grupo/estudante: '))# pede o 2° aluno
    al3 = str(input('Terceiro grupo/estudante: '))
    al4 = str(input('Quarto grupo/estudante: '))
    al5 = str(input('Quinto grupo/estudante: '))
    al6 = str(input('Sexto grupo/estudante: '))
    lista = [al1, al2, al3, al4, al5, al6]
    shuffle(lista)
    print('A ordem dos grupos/estudantes é: {}'.format(lista))
#se for 7
if numero_de_alunos == 7:
    al1 = str(input('Primeiro grupo/estudante: '))# pede o 1° aluno
    al2 = str(input('Segundo grupo/estudante: '))# pede o 2° aluno
    al3 = str(input('Terceiro grupo/estudante: '))
    al4 = str(input('Quarto grupo/estudante: '))
    al5 = str(input('Quinto grupo/estudante: '))
    al6 = str(input('Sexto grupo/estudante: '))
    al7 = str(input('Sétimo grupo/estudante: '))
    lista = [al1, al2, al3, al4, al5, al6, al7]
    shuffle(lista)
    print('A ordem dos grupos/estudantes é: {}'.format(lista))
#se for 8 (último)
if numero_de_alunos == 8:
    al1 = str(input('Primeiro grupo/estudante: '))# pede o 1° aluno
    al2 = str(input('Segundo grupo/estudante: '))# pede o 2° aluno
    al3 = str(input('Terceiro grupo/estudante: '))
    al4 = str(input('Quarto grupo/estudante: '))
    al5 = str(input('Quinto grupo/estudante: '))
    al6 = str(input('Sexto grupo/estudante: '))
    al7 = str(input('Sétimo grupo/estudante: '))
    al8 = str(input('Oitavo grupo/estudante: '))
    lista = [al1, al2, al3, al4, al5, al6, al7, al8]
    shuffle(lista)
    print('A ordem dos grupos/estudantes é: {}'.format(lista))
print('_FIM_')