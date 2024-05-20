# Faça um programa em Python que solicite um número binário, faça a conversão e exiba o número digitado na base decimal
binario = input("Digite um número binário: ")
potencia = len(binario) - 1
decimal = 0
for digito in binario:
  decimal = decimal + int(digito) * 2 ** potencia
  potencia = potencia - 1
print("A conversão do binário %s para decimal e %d." % (binario, decimal))



# Faça um algoritmo que calcula e mostra a média entre duas notas de 10 alunos;
contador = 1
while contador <= 10:
  nota1= float(input("Digite a primeira nota do aluno %d: " % contador))
  nota2= float(input("Digite a segunda nota do aluno %d: " % contador))
  media = (nota1 + nota2) / 2
  print("A média do aluno é %d é %.1f." % (contador, media))
  contador += 1
  
  
  

# Faça um algoritmo que calcula e mostra a média entre duas notas de 10 alunos;
contador = 1
mediaDaSala = 0
while contador <= 10:
  nota1= float(input("Digite a primeira nota do aluno %d: " % contador))
  nota2= float(input("Digite a segunda nota do aluno %d: " % contador))
  media = (nota1 + nota2) / 2
  mediaDaSala += media
  print("A média do aluno é %d é %.1f." % (contador, media))
  contador += 1
mediaDaSala /= contador - 1
print("A média da sala é %.1f." % mediaDaSala)




# Faça um algoritmo que calcula e mostra a média dos números dígitados
contador = 0
soma = 0
resp = "s"
while resp =="s" or resp =="S":
  numero = float(input("Digite um número: "))
  soma += numero
  contador += 1
  resp = input("Deseja continuar (S/N)? ")
media = soma / contador
print("A média dos números digitados é %f." % media)

#Exemplo prof
contador = 0
soma = 0
numero = 0
while numero != -1:
  numero = float(input("Digite um número: (-1 para terminar) "))
  if numero != -1:
    soma += numero
    contador += 1
media = soma / contador
print("A média dos números digitados é %f. " % media)




## Exercícios

# Imprimindo com aspas simples, duplas e triplas;
print('Imprimindo com aspas simples')
print("Imprimindo com aspas duplas")
print("""Imprimindo com aspas
Assim eu posso
pular linhas,
várias linhas!""")
print("Com aspas duplas ou simples podemos usar o barra-n \n para pular linha.")
fruta = 'banana'
letra = fruta[1]
print('O caractere na posição 1 de banana é ', letra)
#O zero é a posição 1 - referente ao B


# Exemplo 1
texto = input("Digite um número inteiro: ")
tamanho = len(texto)
print("O número informado em %d dígitos" % tamanho)

numero = int(texto)
tamanho = len(str(numero))
print("O número informado em %d dígitos" % tamanho)
  
  
# Exemplo 2 - leia uma string e imprima a inversa dela
texto = input("Digite um texto: ")
invertida = ""
for letra in texto:
  invertida = letra + invertida
print(invertida)


# Exemplo 3
s = "ALE"
b = "LU"
print(s + b + "IA")
idade = 18
print("João tem %d anos de idade " % idade)
print("João tem %5d anos de idade " % idade)
# O número antes do "d" significa o espaçamento
numero = 12.34
print("%f" % numero)
print("%.3f" % numero)
print("%8.3f" % numero)
print("%08.3f" % numero)


# Exemplo 4
nome = "Wagner Moura"
idade = 47
print("%s tem %d anos de idade " % (nome , idade))
print(f"{nome} tem {idade} anos de idade.")
print("{} tem {} anos de idade".format(nome, idade))


# Exemplo 5
valor = float(input("Qual o valor do produto em reais? "))
percentual = float(input("Qual o percentual de acréscimo? "))
valorNovo = valor * (1 + percentual / 100)
print("O valor total da compra é R$%.2f com acréscimo de %.1f%% é R$%.2f" % (valor , percentual, valorNovo))
print(f"O valor R${valor:.2f} com acréscimo de {percentual:.1f}% é R${valorNovo:.2f}")
print("O valor R${:.2f} com acréscimo de {:.1f}%% é R${:.2f}".format(valor , percentual, valorNovo))
  
  
# Exemplo 6 
numero = input("Digite algo: ")
print(numero[::-1])


# Exemplo 7
a = "Fizeram a atividade? "
print(a.replace("atividade","exercício"))
print(a)
a = a.replace("atividade", "tarefa")
print(a)
print(a.lower()) #tudo minúsculo
print(a.upper()) #tudo maíusculo


# Exemplo 8
texto = input("Digite uma frase: ")
lista = texto.split()
print(lista)
print("A frase tem %d palavras." % len(lista))
