# Calcule e exiba a conversão deste número para a base 2.
numero = int(input("Digite um número inteiro na base 10: "))

# Verificando se o número é negativo
sinal = 1
if numero < 0:
    sinal = -1
    numero = -numero

# Lidando com o caso especial de zero
if numero == 0:
    resultado_base2 = '0'
else:
    resultado_base2 = ''

# Calculando a conversão para a base 2
while numero != 0:
    resultado_base2 = str(numero % 2) + resultado_base2
    numero //= 2

# Adicionando o sinal de negativo, se necessário
if sinal == -1:
    resultado_base2 = '-' + resultado_base2

print("O número na base 2 é:", resultado_base2)



# Calcule e exiba a conversão deste número para a base 8;
numero = int(input("Digite um número inteiro na base 10: "))

# Verificando se o número é negativo
sinal = 1
if numero < 0:
    sinal = -1
    numero = -numero

# Lidando com o caso especial de zero
if numero == 0:
    resultado_base8 = '0'
else:
    resultado_base8 = ''

# Calculando a conversão para a base 8
while numero != 0:
    resultado_base8 = str(numero % 8) + resultado_base8
    numero //= 8

# Adicionando o sinal de negativo, se necessário
if sinal == -1:
    resultado_base8 = '-' + resultado_base8

print("O número na base 8 é:", resultado_base8)




# Calcule e exiba a conversão deste número para a base 16;
numero = int(input("Digite um número inteiro na base 10: "))

# Verificando se o número é negativo
sinal = 1
if numero < 0:
    sinal = -1
    numero = -numero

# Lidando com o caso especial de zero
if numero == 0:
    resultado_base16 = '0'
else:
    resultado_base16 = ''

# Calculando a conversão para a base 16
while numero != 0:
    resultado_base16 = str(numero % 16) + resultado_base16
    numero //= 16

# Adicionando o sinal de negativo, se necessário
if sinal == -1:
    resultado_base16 = '-' + resultado_base16

print("O número na base 8 é:", resultado_base16)

