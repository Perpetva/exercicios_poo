# Crie um sistema simples de gerenciamento de biblioteca. 
# O sistema deve permitir o cadastro de livros, a visualização dos livros cadastrados e a realização de empréstimos de livros.

class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print()
            return True
        return False

    def devolver(self):
        self.disponivel = True
        print()

    def exibir_informacoes(self):
        disponivel_str = 'Disponível' if self.disponivel else 'Indisponível'
        return f'Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano_publicacao}, Status: {disponivel_str}'

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def exibir_livros(self):
        for livro in self.livros:
            print(livro.exibir_informacoes())
        
    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo and livro.disponivel:
                livro.emprestar()
                return f'O livro "{titulo}" foi emprestado com sucesso.\n'
        return f'O livro "{titulo}" não está disponível para empréstimo.\n'

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo and not livro.disponivel:
                livro.devolver()
                return f'O livro "{titulo}" foi devolvido com sucesso.\n'
        return f'O livro "{titulo}" não foi encontrado ou já está disponível.\n'

l1 = Livro('1984', 'George Orwell', 1949)
l2 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954)
l3 = Livro('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 1943)

b = Biblioteca()

b.adicionar_livro(l1)
b.adicionar_livro(l2)
b.adicionar_livro(l3)

print("Livros na biblioteca:")
b.exibir_livros()

print(b.emprestar_livro('1984'))

print("Livros na biblioteca após empréstimo:")
b.exibir_livros()

print(b.devolver_livro('1984'))

print("Livros na biblioteca após devolução:")
b.exibir_livros()