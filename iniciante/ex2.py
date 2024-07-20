# Crie um sistema simples para gerenciar alunos em uma escola. 
# O sistema deve permitir o cadastro de alunos, a visualização das informações dos alunos cadastrados, e a atualização das notas dos alunos.
import random

class Aluno:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        media = 0
        for nota in self.notas:
            media += nota
        media = format(media / len(self.notas), '.2f')
        return media

    def exibir_informacoes(self):
        exibe = f'Aluno: {self.nome}\nIdade: {self.idade}\nMatricula: {self.matricula}\nMedia: {self.calcular_media()}'
        return exibe

class Escola:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno (self, aluno):
        self.alunos.append(aluno)

    def exibir_alunos (self):
        for aluno in self.alunos:
            print(aluno.exibir_informações())
            print()
        
    def atualizar_notas (self, matricula, nota):
        for aluno in self.alunos:
            if matricula == aluno.matricula:
                aluno.adicionar_nota(nota)
                return print(f'O aluno com matricula {matricula} recebeu a nota {nota} com sucesso\n')
            return print(f'Aluno com matrícula {matricula} não encontrado.')
                
a1 = Aluno('Felipe', 15, 50)
a2 = Aluno('Amanda', 12, 60)
a3 = Aluno('Carlos', 14, 70)

lista_alunos = [a1, a2, a3]

e = Escola()

a1.adicionar_nota(10)

# for aluno in lista_alunos:
#     e.adicionar_aluno(aluno)
#     for _ in range(3):
#         aluno.adicionar_nota(random.randint(0, 10))

e.adicionar_aluno(a1)

e.exibir_alunos()
e.atualizar_notas(a1.matricula, 0)
e.exibir_alunos()