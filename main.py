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

