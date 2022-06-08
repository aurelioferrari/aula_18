# criar uma matriz de ordem 3

lista = [[], [], []]
num = []
for c in range(1, 4):
    n = (int(input("Digite um número: ")))
    lista[0].append(n)
for c in range(1, 4):
    n = (int(input("Digite um número: ")))
    lista[1].append(n)
for c in range(1, 4):
    n = (int(input("Digite um número: ")))
    lista[2].append(n)

print(f'[{lista[0][0]}  {lista[0][1]}  {lista[0][2]}]')
print(f'|{lista[1][0]}  {lista[1][1]}  {lista[1][2]}|')
print(f'[{lista[2][0]}  {lista[2][1]}  {lista[2][2]}]')