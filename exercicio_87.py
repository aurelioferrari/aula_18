# fazer uma matriz 3x3
# A) soma de todos os valores pares
# B) soma dos valores da terceira coluna
# C) o maior número da segunda linha

lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
soma3 = 0

for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = (int(input("Digite um número: ")))
        if lista[l][c] % 2 == 0:
            par = par + lista[l][c]
for l in range(0, 3):
    soma3 = soma3 + lista[l][2]
print(f"A soma dos números pares é: {par}")
print(f'A soma dos valores da terceira coluna é: {soma3}')
print(f'O maior valor da segunda linha é: {max(lista[1])}')
