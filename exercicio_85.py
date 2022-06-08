# dentro de uma lista, colocar os números pares em uma lista e impares em outra
# ordenar os números em ordem crescente
lista = []
pares = []
impares = []

for c in range(0, 7):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        pares.append(n)
    if n % 2 != 0:
        impares.append(n)
pares.sort()
impares.sort()
lista.append(pares[:])
lista.append(impares[:])
print(pares)
print(impares)
print(lista)