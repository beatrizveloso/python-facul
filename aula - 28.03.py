#  Insira sua média e frequência e ele dá retorno se voce está repprovado por nota, frequência ou aprovado.
media = float(input("Digite a média: "))
frequencia = float(input("Digite o percentual de frequência: "))

if frequencia < 75:
  print("Reprovado por falta ")
elif media < 6.0:
    print("Reprovado por nota ")
else:
    print("Aprovado ")


# Insira a quantidade de diárias, o tipo de hospedagem e ele te dá o valor da estádia.
quantidadedeDiarias = int(input("Digite a quantidade de diárias: "))
tipo = input("Digite o tipo de hospedagem ")
if tipo == "s" or tipo == "S":
  print("Valor da estádia é R$%.2f" % (quantidadedeDiarias * 255.5))
elif tipo == "d" or tipo == "D":
  print("Valor da estádia é R$%.2f." % (quantidadedeDiarias * 305.5))
elif tipo == "t" or tipo == "T":
  print("Valor da estádia é R$%.2f" % (quantidadedeDiarias * 360.5))
else:
  print("Tipo de hospedagem inválida")


# Escreva três números, o programa retornará qual é o maior.
n1 = int(input("Escreva o número 1: "))
n2 = int(input("Escreva o número 2: "))
n3 = int(input("Escreva o número 3: "))

if n1>n2 and n1>n3:
  print("Numéro 1 é o maior")
elif n2>n1 and n2>n3:
  print("Numéro 2 é o maior")
elif n3>n1 and n3>n2:
  print("Numéro 3 é o maior")
  
  
# Insira seu peso e sua altura e ele dará se vc está abaixo da média, na média, etc...
peso = float(input("Qual seu peso em kg? "))
altura = float(input("Qual sua altura em metros? "))
imc = peso / altura ** 2

if imc < 20:
  print("Você está abaixo da média")
elif imc < 25:
  print("Você está na média")
elif imc < 30:
  print("Você está em sobrepeso")
elif imc < 40:
  print("Você está obeso")
else:
  print("Você está em estado de obeso mórbito")


# Esse programa calcula o IMC.
peso = float(input("Qual seu peso em kg? "))
altura = float(input("Qual sua altura em metros? "))
imc = peso / altura ** 2

if imc < 20:
  print("Com IMC = %.1f, você está abaixo do peso." % imc)
elif imc < 25:
  print("Com IMC = %.1f, você está na faixa ideal." % imc)
elif imc < 30:
  print("Com IMC = %.1f, você está com sobrepeso." % imc)
elif imc < 40:
  print("Com IMC = %.1f, você está obeso." % imc)
else:
  print("Com IMC = %.1f, você está em obesidade mórbita." % imc)


# Insira o valor da compra, em quantas parcelas vc quer parcelar e ele dará o retorno do valor de cada parcela.
valorTotal = int(input("Qual o valor total da compra? "))
parcelas = int(input("Quantas parcelas você deseja? "))

if parcelas >= 2:
  valorNovo = valorTotal * 1.03
elif parcelas == 4:
  valorNovo = valorTotal * 1.07
elif parcelas == 6:
  valorNovo = valorTotal * 1.09
elif parcelas == 8:
  valorNovo = valorTotal * 1.12
else:
  parcelas = 0

if parcelas == 0:
  print("Número inválido de parcelas. Tente novamente.")
else:
  print("Serão pagar %d parcelas de R$%.2f." % (parcelas, valorNovo / parcelas))
  
  

# Digite o número da placa do automóvel e ele retornará qual o dia do seu rodízio.
placa = int(input("Digite o número da placa do automóvel: "))
digito = placa % 10

if digito == 1 or digito == 2:
  rodizio = "Segunda-Feira"
elif digito == 3 or digito == 4:
  rodizio = "Terça-Feira"
elif digito == 5 or digito == 6:
  rodizio = "Quarta-Feira"
elif digito == 7 or digito == 8:
  rodizio = "Quinta-Feira"
else:
  rodizio = "Sexta-Feira"

print("Este veículo está em rodízio na %s." % rodizio)
  

