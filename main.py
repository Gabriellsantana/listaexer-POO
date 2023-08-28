#1. Classe Bola: Crie uma classe que modele uma bola:
#a. Atributos: Cor, circunferência, material
#b. Métodos: trocaCor e mostraCor

class Ball:
    def __init__(self, color="unknown", circunf=0, material="unknown"):
        self.color = color
        self.circunf = circunf
        self.material = material

    def trocaCor(self):
        troca = input("Deseja mudar a cor atual {}? [s/n]".format(self.color))

        troca = troca[0].lower()

        if troca == "s":
            nova_cor = input("\n> Nova Cor: ")
            self.color = nova_cor
        else:
            print("Ok a cor continua {}".format(self.color))

    def mostraCor(self):
        print("\nA cor atual é {}".format(self.color))


def main():
    bola01 = Ball("azul", 5, "metal")

    while True:
        bola01.mostraCor()
        bola01.trocaCor()

        continuar = input("Continuar? [s/n]")
        continuar = continuar[0].lower()
        if continuar == "n":
            break

    bola01.mostraCor()


main()


#2. Classe Quadrado: Crie uma classe que modele um quadrado:
#a. Atributos: Tamanho do lado
#b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudar_lado(self, novo_lado):
        self.lado = novo_lado

    def retornar_lado(self):
        return self.lado

    def calcular_area(self):
        return self.lado ** 2

lado_usuario = float(input("Informe o tamanho do lado do quadrado: "))
quadrado1 = Quadrado(lado_usuario)

print("Lado do quadrado:", quadrado1.retornar_lado())
print("Área do quadrado:", quadrado1.calcular_area())

novo_lado_usuario = float(input("Informe o novo tamanho do lado do quadrado: "))
quadrado1.mudar_lado(novo_lado_usuario)

print("Novo lado do quadrado:", quadrado1.retornar_lado())
print("Nova área do quadrado:", quadrado1.calcular_area())

#3. Classe Retângulo: Crie uma classe que modele um retângulo:
class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudar_lados(self, novo_lado_a, novo_lado_b):
        self.lado_a = novo_lado_a
        self.lado_b = novo_lado_b

    def retornar_lados(self):
        return self.lado_a, self.lado_b

    def calcular_area(self):
        return self.lado_a * self.lado_b

    def calcular_perimetro(self):
        return 2 * (self.lado_a + self.lado_b)

lado_a_usuario = float(input("Informe o valor do lado A do retângulo: "))
lado_b_usuario = float(input("Informe o valor do lado B do retângulo: "))
retangulo1 = Retangulo(lado_a_usuario, lado_b_usuario)

print("Lados do retângulo:", retangulo1.retornar_lados())
print("Área do retângulo:", retangulo1.calcular_area())
print("Perímetro do retângulo:", retangulo1.calcular_perimetro())

tamanho_piso = float(input("Informe o tamanho do piso: "))
tamanho_rodape = float(input("Informe o tamanho do rodapé: "))

area_total = retangulo1.calcular_area()
perimetro_total = retangulo1.calcular_perimetro()

quantidade_pisos = area_total / tamanho_piso
quantidade_rodapes = perimetro_total / tamanho_rodape

print("Quantidade de pisos necessários:", quantidade_pisos)
print("Quantidade de rodapés necessários:", quantidade_rodapes)

#4. Classe Pessoa: Crie uma classe que modele uma pessoa:
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.crescer(0.5)

    def engordar(self, aumento_peso):
        self.peso += aumento_peso

    def emagrecer(self, reducao_peso):
        self.peso -= reducao_peso

    def crescer(self, aumento_altura):
        self.altura += aumento_altura

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso}, Altura: {self.altura}")

nome_usuario = input("Digite o nome da pessoa: ")
idade_usuario = int(input("Digite a idade da pessoa: "))
peso_usuario = float(input("Digite o peso da pessoa: "))
altura_usuario = float(input("Digite a altura da pessoa: "))

pessoa1 = Pessoa(nome_usuario, idade_usuario, peso_usuario, altura_usuario)

pessoa1.mostrar_informacoes()

anos_a_envelhecer = int(input("Digite quantos anos deseja envelhecer a pessoa: "))
pessoa1.envelhecer()
pessoa1.engordar(2)
pessoa1.emagrecer(1)
pessoa1.crescer(0.8)

pessoa1.mostrar_informacoes()

#5Classe Conta Corrente: Crie uma classe para implementar uma conta
#corrente. A classe deve possuir os seguintes atributos: número da conta, nome
#do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e
#saque; No construtor, saldo é opcional, com valor default zero e os demais
#atributos são obrigatórios.

class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def mostrarInformacoes(self):
        print(f"Número da Conta: {self.numero_conta}")
        print(f"Nome do Correntista: {self.nome_correntista}")
        print(f"Saldo: {self.saldo}")

numero_conta_usuario = input("Digite o número da conta: ")
nome_correntista_usuario = input("Digite o nome do correntista: ")

conta1 = ContaCorrente(numero_conta_usuario, nome_correntista_usuario)

conta1.mostrarInformacoes()

valor_deposito = float(input("Digite o valor para depósito: "))
conta1.deposito(valor_deposito)

valor_saque = float(input("Digite o valor para saque: "))
conta1.saque(valor_saque)

conta1.mostrarInformacoes()



