# Desenvolva um programa em Python que solicite ao usuário os valores dos lados de um retângulo. A seguir, calcule e mostre os valores de seu perímetro e de sua área. Crie um programa em Python que solicite ao usuário a sua idade e mostre se ele podeter CHN .
lado1 = float(input("Digite o valor do lado A do retângulo: "))
lado2 = float(input("Digite o valor do lado B do retângulo: "))
perimetro = 2 * (lado1 + lado2)
area = lado1 * lado2
print("O perímetro do retângulo é:", perimetro)
print("A área do retângulo é:", area)


# Escreva um programa em Python que solicite ao usuário o salário atual e mostre o salário acrescido de 5% comissão.
salarioatual = float(input("Digite o salário atual: "))
salariocomcomissao = salarioatual * 1.05
print("O salário com acréscimo de 5% de comissão é:", salariocomcomissao)


# Escreva um programa em Python que solicite ao usuário a distância entre duas cidades e o tempo de viagem. O programa deverá calcular e exibir a velocidade média de um carro que vai de uma cidade para outra. Lembre-se de que: v com m subscrito igual a numerador d i s t â n c i a sobre denominador t e m p o fim da fração.
distancia = float(input("Digite a distância entre as cidades (em quilômetros): "))
tempo = float(input("Digite o tempo de viagem (em horas): "))
velocidademedia = distancia / tempo
print("A velocidade média do carro é:", velocidademedia, "km/h")
  
  
# Escreva um programa em Python que calcule as duas raízes de uma equação de 2º grau ax²+bx+c, recebendo os valores dos coeficientes da mesma (a, b, c). Suponha que as raízes são reais. Lebre-se de que para calcular as duas raízes usamos a Fórmula de Báskara: x com 1 vírgula 2 subscrito fim do subscrito igual a numerador menos b mais ou menos raiz quadrada de incremento sobre denominador 2 a fim da fração com incremento igual a b ao quadrado menos 4 a c.
import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c

raiz1 = (-b + math.sqrt(delta)) / (2*a)
raiz2 = (-b - math.sqrt(delta)) / (2*a)

print("As raízes da equação são:", raiz1, "e", raiz2)


# Escreva um programa em Python que leia a cotação do dólar (taxa de conversão), leia um valor em dólares e converta e mostre o valor equivalente em Reais.
cotacaodolar = float(input("Digite a cotação do dólar (em reais): "))

valordolar = float(input("Digite o valor em dólares: "))

valorreais = valordolar * cotacaodolar

print("O valor equivalente em reais é:", valorreais, "R$")


# Escreva um programa em Python que leia um valor representando o gasto realizado por um cliente do restaurante Coma Bem e visualize o valor total a ser pago, considerando os 10% do garçom.
valorgasto = float(input("Digite o valor do gasto realizado: "))

taxagarcom = valorgasto * 0.10

totalapagar = valorgasto + taxagarcom

print("O valor total a ser pago, incluindo os 10% do garçom, é:", totalapagar)
  
  

# Escreva um programa em Python que obtenha uma temperatura em graus Celsius, calcule e mostre a respectiva temperatura nas escalas Fahrenheit e Kelvin. Utilize as fórmulas abaixo:
celsius = float(input("Digite a temperatura em graus Celsius: "))

fahrenheit = (celsius * 9/5) + 32

kelvin = celsius + 273.15

print("A temperatura em Fahrenheit é:", fahrenheit, "°F")
print("A temperatura em Kelvin é:", kelvin, "K")



## Exercícios 


# Exercício 1:  Faça um programa em Python que calcule e mostre o valor do volume do tronco de uma pirâmide, para isso o programa deve solicitar ao usuário os valores da altura do tronco da pirâmide (h), o valor da base menor (Bmenor) e o da base maior (Bmaior) e calcular a seguinte expressão: volume =h/3(Bmaior*2 + Bmenor2 + (Bmaior2 * Bmenor2)0.5)

h = float(input("Digite a altura do tronco da pirâmide: "))

bmenor = float(input("Digite o valor da base menor da pirâmide: "))

bmaior = float(input("Digite o valor da base maior da pirâmide: "))

volume = h/3 * (bmaior*2 + bmenor*2 + (bmaior*2 * bmenor*2)*0.5)

print(f"O volume do tronco da pirâmide é: {volume:.2f}")
  
  
# Exercício 2: Crie um programa em Python que solicite o valor em horas para o usuário, calcule e mostre o valor em minutos, sabendo que 1 hora tem 60 minutos.
import math

horas = int(input("Digite o valor em horas: "))

min = 60*horas

print(f"{horas} horas equivale a {min} minutos.")


# Exercício 3: Crie um programa em Python que solicite ao usuário a sua idade expressa em anos, meses e dias (variáveis separadas). Calcule e mostre a idade expressa apenas em dias. Para isso considere 1 ano = 365 dias, 1 mês = 30 dias.
import math

a = int(input("Digite a quantidade de anos: "))

m = int(input("Digite a quantidade de meses: "))

d = int(input("Digite a quantidade de dias: "))

d1 = a*365

d2 = m*30

s = d+d1+d2

print(f"Você possui um total de {s} dias.")


# Exercício 4: Escreva um programa em Python para calcular o valor de uma prestação em atraso (prestacao). Para isso, obtenha o valor da prestação (valorPrestacao), a porcentagem de multa pelo atraso (multa) e a quantidade de dias de atraso (qtdeDias). Calcular e mostrar o valor da prestação atualizado, sabendo que:

valorPrestacao = int(input("Digite o valor da prestação: "))

multa = int(input("Digite o valor da multa a ser cobrada: "))

dias = int(input("Digite a quantidade de dias de atraso: "))

prestacao = valorPrestacao + (valorPrestacao * (multa/100) * dias)

print(f"Nossa nova prestação deverá ser de {prestacao} reais.")
  
  

# Exercício 5: Faça uma programa em Python que peça do usuário um valor em graus para um ângulo. Converta-o para radianos e, usando funções da biblioteca math, imprima o seno, cosseno e tangente deste ângulo.
import math

graus = float(input("Valor em graus: "))

r = math.radians(graus)

s = math.sin(r)

c = math.cos(r)

t = math.tan(r)

print(f"Para o ângulo {graus}°:")

print(f"O seno é {s}.")

print(f"O cosseno é {c}.")

print(f"A tangente é {t}.")

