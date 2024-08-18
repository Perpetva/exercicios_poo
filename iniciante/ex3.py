# Crie um sistema simples para gerenciar reservas de quartos em um hotel. 
# O sistema deve permitir o cadastro de quartos, a visualização dos quartos disponíveis, e a realização de reservas de quartos.

class Quarto:
    def __init__(self, numero, tipo, preco):
        self.numero = numero
        self.tipo = tipo
        self.preco = preco
        self.disponivel = True

    def reservar(self):
        self.disponivel = False

    def cancelar_reserva(self):
        self.disponivel =  True

    def exibir_informacoes(self):
        return f'Número: {self.numero}\nTipo: {self.tipo}\nPreço: ${self.preco}\nDisponivel!'
        
class Hotel:
    def __init__(self):
        self.quartos = []
    
    def adiciona_quarto(self, quarto):
        self.quartos.append(quarto)
    
    def exibir_quartos_disponiveis(self):
        for quarto in self.quartos:
            if quarto.disponivel:
                print(quarto.exibir_informacoes())
                print()

    def realizar_reserva(self, numero):
        for quarto in self.quartos:
            if numero == quarto.numero and quarto.disponivel == True:
                quarto.reservar()
                print(f'O quarto de número {numero} foi reservado')
        
    def cancelar_reserva(self, numero):
        for quarto in self.quartos:
            if numero == quarto.numero and quarto.disponivel == False:
                quarto.cancelar_reserva()
                print(f'Cancelamos a reserva do quarto {numero}')
        
q1 = Quarto(1, 'Suite', 1300)
q2 = Quarto(2, 'Double', 1700)

h = Hotel()

h.adiciona_quarto(q1)
h.adiciona_quarto(q2)

h.exibir_quartos_disponiveis()
print('--------------------------')

h.realizar_reserva(q1.numero)
h.exibir_quartos_disponiveis()
print('--------------------------')

h.cancelar_reserva(q1.numero)
h.exibir_quartos_disponiveis()