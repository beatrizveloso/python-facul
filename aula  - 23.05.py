# Insira os valores do salário de cada mês:
mes = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]

for i in range(12):
  salario = float(input("Digite o salário de %s R$" % mes[i]))
  
  
  
# Faça um programa em Python que liste 3 nomes:
nome = ['Harry', 'Rony', 'Hermione' ]
for i in range(3):
  print(nome[i])
 
 
  
# Faça um programa em Python que calcule a média de um aluno apartir de cinco notas :

notas = [5, 6, 7, 8.7, 4.5]
qtde = len(notas)



# Iterando sobre a lista usando indices
soma = 0
for i in range(5):
  soma = soma + notas[i]
media = soma / 5
print("A média é %f." % media)

# Iterando sobre os elementos da lista
soma = 0
for nota in notas:
  soma += nota
media = soma / 5
print("A média é %f." % media)



# Solicita nomes e os coloca em outra ordem

nomes = []

for i in range(5):
  n = input("Digite o nome %d: " % (i + 1))
  nomes.insert(5, n)

for nome in nomes:
  print(nome, end=" ")
  
  
# Outra forma ...

nomes = []

for i in range(5):
  n = input("Digite o nome %d: " % (i + 1))
  nomes.append(n)

for nome in nomes:
  print(nome, end=" ")

i = int(input("Qual o índice do nome que deseja imprimir? "))
print(nomes[i])



# Exemplo média de uma quantidade indeterminada de números

numeros = []
soma = 0

resp = 1.0
while resp != 0:
  resp = float(input("Digite um número, 0 para terminar: "))