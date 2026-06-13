num1 = float(input("Digite um número "))
op = str(input("Digite a operação"))
num2 = float(input("Digite outro número "))

if op == "+":           # SOMA
    print(f"Resultado é igual a: {num1 + num2}")

elif op == "-":         # SUBTRAÇÃO
    print(f"Resultado é igula a: {num1 - num2}")

elif op == "*":         # MULTIPLICAÇÃO
    print(f"Resultado é igual a: {num1 * num2}")

elif op == "/":         # DIVISÃO
    if num2 == 0:       # NÃO DIVISIVEL POR 0
        print("Não é possivel dividir por 0")
    else:
        print(f"Resultado é igual a: {num1 / num2}")

elif op == "**":        # POTENCIA
    print(f"Resultado é igual a: {num1 ** num2}")

elif op == "%":         # RESTO DA DIVISÃO
    print(f"Resultado é igual a: {num1 % num2}")