# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
#num1 = int(input("Insira o primeiro número: "))
#num2 = int(input("Insira o segundo número: "))

#result1 = num1 + num2

#print(f"O resultado é {result1}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
#num = int(input("Insira um número: "))
#result2 = num % 5
#print(f"O resto da divisão de {num} por 5 é: {result2}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
#num1 = int(input("Informe o primeiro número: "))
#num2 = int(input("Informe o segundo número: "))

#result3 = num1 * num2

#print(f"A multiplicação entre eles é: {result3}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
#num1 = int(input("Informe o primeiro número inteiro: "))
#num2 = int(input("Informe o primeiro segundo inteiro: "))

#result4 = num1 // num2

#print(f"O resultado da divisão inteira é: {result4}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
#num = int(input("Informe um número inteiro: "))

#result5 = num ** 2

#print(f"O quadrado do número é: {result5}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
#num1 = float(input("Insira o primeiro número: "))
#num2 = float(input("Insira o segundo número: "))

#result6 = num1 + num2

#print(f"O resultado é {result6}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
#num1 = float(input("Insira o primeiro número: "))
#num2 = float(input("Insira o segundo número: "))

#result7 = (num1 + num2) / 2

#print(f"O resultado é {result7}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
#num1 = float(input("Insira o primeiro número (base): "))
#num2 = float(input("Insira o segundo número (expoente): "))

#result8 = num1 ** num2

#print(f"O resultado é {result8}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
#var = float(input("Insira o a temperatura em celsius: "))

#fahrenheit = (var * 1.8) + 32 

#print(f"{var} em fahrenheit fica: {fahrenheit}")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
#raio_do_circulo = float(input("Digite o raio: "))

#area_do_circulo = math.pi * raio_do_circulo ** 2
# area_do_circulo_formatada = "{:.2f}".format(area_do_circulo)
#print(f"{area_do_circulo:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
#var = input("Digite uma palavra: ")
#result11 = var.upper()
#print(result11)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
#var = input("Digite seu nome completo: ")
#result12 = var.lower()
#print(result12)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, 
# em seguida, imprima esta frase sem espaços em branco no início e no final.
#var = input("Digite uma frase: ")
#result13 = var.strip()
#print(result13)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, 
# em seguida, imprima o dia, o mês e o ano separadamente.
#var = input("Digite uma data 'dd/mm/aaaa': ")

#result14 = var.split("/")

#print(result14[0])
#print(result14[1])
#print(result14[2])

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
#var1 = input("Escreva uma palavra ou frase: ")
#var2 = input("Escreva outra palavra ou frase: ")

#result14 = var1 + " " + var2

#print(result14)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
var1 = input("Digite a primeira expressão booleana (True ou False): ")
var2 = input("Digite a segunda expressão booleana (True ou False): ")

r_var1 = var1.lower() == 'true'
r_var2 = var2.lower() == 'true'

result = r_var1 and r_var2

print(result)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 23: Calculadora Simples
# 22: Verificador de Palíndromo
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação