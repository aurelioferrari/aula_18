# ler varios nomes e pesos
# A) numero de pessoas cadastradas
# B) lista com a pessoas mais pesadas >= 100
# C) lista com as pessoas mais leves <= 70

lista = []
pessoas = []
total = 0
pesado = 0
leve = 0

while True:
    pessoas.append(str(input("Qual o seu nome? ")))
    pessoas.append(int(input("Qual o seu peso? ")))
    lista.append(pessoas[:])
    total += 1
    pessoas.clear()
    opcao = str(input("Você deseja continuar? [S/N] ")).strip().upper()[0]
    while opcao not in "SsNn":
        opcao = str(input("Você deseja continuar? [S/N] ")).strip().upper()[0]
    if opcao in "Nn":
        break
for p in lista:
    if p[1] >= 100:
        pesado += 1
    if p[1] <= 70:
        leve += 1
    print(f'{p[0]} tem {p[1]} kilos.')
print(f'Foram registradas {pesado} pessoas com mais de 100 kilos.')
print(f'Foram registradas {leve} pessoas com menos de 70 kilos.')
print(f'Foram registradas um total de {total} pessoas.')


