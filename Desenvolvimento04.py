class NumeroComplexo:
    def __init__(self, real, imagem):
        self.real = real
        self.imagem= imagem

    def geraNumero(self):
        return complex(self.real, self.imagem)


lista = []
print("------------------------------------------------")
print("Digite os valores do primeiro numero complexo- ")
real = int(input("Digite o numero real: "))
imagem = int(input("Digite a imagem: "))

c1 = NumeroComplexo(real,imagem)
numero1 = c1.geraNumero()
print(F'O primeiro Numero Complexo é: {numero1}')
lista.append(numero1)

print("------------------------------------------------")
print("Digite os valores do segundo numero complexo- ")
real = int(input("Digite o numero real: "))
imagem = int(input("Digite a imagem: "))

c2 = NumeroComplexo(real,imagem)
numero2 = c2.geraNumero()
print(F'O segundo Numero Complexo é: {numero2}')
lista.append(numero2)

print("------------------------------------------------")
print("Digite os valores do terceiro numero complexo:- ")
real = int(input("Digite o numero real: "))
imagem = int(input("Digite a imagem: "))

c3 = NumeroComplexo(real,imagem)
numero3 = c3.geraNumero()
print(F'O terceiro Numero Complexo é: {numero3}')
lista.append(numero3)

print(f'Os dumeros Digitados Foram: {lista}')

class Operacoes:
    def __init__(self, lista):
        self.lista = lista

    def soma(self,lista):
        for soma in lista:
            soma += soma
        return soma

    def subtracao(self,lista):
        sub1 = lista[0] - lista[1]
        sub = sub1 - lista[2]
        return sub

    def multiplicacao(self,lista):
        for mult in lista:
            mult *= mult
        return mult

    def divisao(self,lista):
        div1 = lista [0] / lista[1]
        div2 = div1 / lista[2]
        return div2



op = Operacoes(lista)
print("------------------------------------------------")
print(f'Operacoes na lista {op.lista}')
n1 = op.soma(lista)
print(f'O resultado da soma dos numeros e: {n1}')
n2 = op.subtracao(lista)
print(f'O resultado da subtracao dos numeros e: {n2}')
n3 = op.multiplicacao(lista)
print(f'O resultado da multiplicacao dos numeros e: {n3}')
n4 = op.divisao(lista)
print(f'O resultado da divisao dos numeros e: {n4}')

lista2 =[n1,n2,n3,n4]
lista3 = lista + lista2

print("-----------------------------------------")
print("Impressao das Partes dos Numeros")
print(" ")
for numero in lista3:
    print(f'Numero Complexo: {numero}')
    print(f'Parte Real: {numero.real}')
    print(f'Parte Imaginaria: {numero.imag}')
    print(" ")