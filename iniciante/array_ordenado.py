# Crie um array aonde os números ficam ordenados de forma crescente após cada inserção de um novo número

import numpy as np
class ArrayOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')

        else:
            for i in range(self.ultima_posicao + 1):
                print(i, '-', self.valores[i])

    def insere(self, valor):    
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x-= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

array = ArrayOrdenado(10)
array.imprime()
print('---------------------')

array.insere(6)
array.imprime()
print('---------------------')

array.insere(4)
array.imprime()
print('---------------------')
            
array.insere(3)
array.imprime()
print('---------------------')

array.insere(5)
array.imprime()
print('---------------------')

array.insere(1)
array.imprime()
print('---------------------')

array.insere(8)
array.imprime()
print('---------------------')

array.insere(-3)
array.imprime()