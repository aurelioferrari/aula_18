# perguntar ao usuario quantos jogos de mega sena ele quer fazer
# sortear 6 números de 1 a 60  para cada jogo
from time import sleep
import random
jogos = []
numeros = []
jogadas = int(input("Quantos jogos você quer fazer? "))
j = 1
while j <= jogadas:
    for n in range(0, 6):
        n = random.randint(1, 60)
        while n in numeros:
            n = random.randint(1, 60)
        numeros.append(n)
    jogos.append(numeros[:])
    numeros.clear()
    j += 1

for c in range(0, jogadas):
    jogos[c].sort()
    print(f'{c+1}º jogo: {jogos[c]}')
    sleep(0.5)
