# criar uma lista com nomes dos alunos e notas
# imprimir um boletim com as médias de cada aluno
# usuario pode procurar as notas de um aluno

boletim = []
aluno = []
notas = []
media = 0
counta = 0
countb = 0
while True:
    aluno.append(str(input("Qual o seu nome? "))) # aluno recebe nome
    nota1 = float(input("Qual a primeira nota? "))
    nota2 = float(input("Qual a segunda nota? "))
    notas.append(nota1)
    notas.append(nota2)
    aluno.append(notas[:]) # aluno recebe notas
    media = (nota1 + nota2) / 2
    aluno.append(media)
    boletim.append(aluno[:])
    aluno.clear()
    notas.clear()
    counta += 1
    opcao = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    while opcao not in "SsNn":
        opcao = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    if opcao in "Nn":
        break
print('=' * 30)
print(f'{"Nº"} {"Nome":<10} {"Média":>5}')
print('_' * 30)
while countb < counta:
    print(f'{countb} {boletim[countb][0]:<10} {boletim[countb][2]:>5}')
    countb += 1
while True:
    pesquisa = int(input("Digite o código do aluno para saber suas notas ou 999 para sair: "))
    if pesquisa == 999:
        break
    else:
        print(f'As notas do aluno {boletim[pesquisa][0]} foram {boletim[pesquisa][1][0]} e {boletim[pesquisa][1][1]}.')