# Faça um programa em Python que solicite um número decimal, faça a conversão e exiba o número digitado na base binária. use a estrutura de repetição while.
decimal = int(input("Digite um número inteiro em base decimal: "))
binario = ""
while decimal != 0: #! = diferente de
  resto = decimal % 2
  binario = str(resto) + binario
  decimal = decimal // 2
print("A conversão para binário é %s." % binario)


# Adivinhe meu número: Crie um jogo onde o computador escolhe um número inteiro aleatório entre 0 e 100.
import random
numero = random.randint(0, 100)
chute = -1
contador = 0
while chute != numero:
  chute = int(input("Digite um inteiro entre 0 e 100: "))
  contador = contador + 1
  if numero == chute:
    print("Parabéns! Tu acertou em %d tentativas." % contador)
  elif numero > chute:
    print("O número é maior ")
  else:
    print("O número é menor ")




# Conversão de binário, pra decimal;
binario = input("Digite um número binário: ")
potencia = len(binario) - 1
decimal = 0
for digito in binario:
  decimal = decimal + int(digito) * 2 ** potencia
  potencia = potencia - 1
print("A conversão do binário %s para decimal e %d." % (binario, decimal))