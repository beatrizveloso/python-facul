# Crie um programa em Python que solicite ao usuário a sua idade e mostre se ele podeter CHN .
idade = int(input("Qual é a sua idade?"))
if idade >= 18:
  print("Parábens! Você já pode tirar sua CNH!")


# Escreva um programa em Python que solicite um número inteiro ao usuário e mostre caso o mesmo seja par.
num = int(input("Digite um número inteiro "))
if num % 2 == 0:
  print("O número %d é par. " % num)


# Crie um programa em Python que solicite ao usuário três valores inteiros (A,B E C) e verifica se o valor armazenado em B é o menor.
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if a > b and c > b:
  print("O menor valor é o b")
  
  
# Crie um programa em Python que solicite ao usuário a sua idade e mostre se ele pode ter CHN .
idade = int(input("Qual é a sua idade?"))
if idade >= 18:
  print("Parábens! Você já pode tirar sua CNH!")


# Crie um programa em Python que solicite ao usuário um número o mesmo é par ou ímpar
num =int(input("Digite com um número inteiro "))
if num % 2 == 0:
  print("O número %d é par. " % num)
else:
  print("O número %d é impar." % num)


# Crie um programa em Python que solicite duas notas de um aluno ao usuário, calculea média e mostre se o mesmo está aprovado (média >=6.0) ou reprovado caso contrário.
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
media = (n1 + n2)/2
if media >= 6.0:
  print(f"Aprovado com média {media}")
else:
    print(f"Reprovado com média {media}")
  
  

# Faça um programa que solicite ao usuário um número inteiro, calcule e mostre a raizquadrada desse número. O programa deverá verificar antes se o número digitado épositivo, exibindo uma mensagem de alerta, caso seja negativo.
import math
num = float(input("Digite um número: "))
if num >= 0:
  r = math.sqrt(num)
  print("A raiz quadrada de %f é %f." % (num))
else:
  print("Não é possível calcular raiz quadrada real de números negativos.")
  

