import os
import math


def adicao():
    try:
        numero1_adic = int(input("Digite um numero: "))
        numero2_adc = int(input("Digite outro numero: "))
    except ValueError:
        print("Digite apenas numeros!")
        return None
    resultado = numero1_adic + numero2_adc
    print(f"Sua adicao: {resultado}!")
    print("______________________________________")
    return resultado


def subtracao():
    try:
        numero1_sub = int(input("Digite um numero: "))
        numero2_sub = int(input("Digite outro numero: "))
    except ValueError:
        print("Digite apenas numeros!")
        return None
    resultado = numero1_sub - numero2_sub
    print(f"Sua subtracao: {resultado}!")
    print("______________________________________")
    return resultado


def divisao():
    try:
        numero1_div = float(input("Digite um numero: "))
        numero2_div = float(input("Digite outro numero: "))
        if numero1_div and numero2_div == 0:
            print("O numero 0 nao é permitido!")
            print("______________________________________")
            return None
    except ValueError:
        print("Digite apenas numeros!")
        print("______________________________________")
        return None
    resultado = numero1_div / numero2_div
    print(f"Sua divisao: {resultado:.2f}!")
    print("______________________________________")
    return resultado


def multiplicacao():
    try:
        numero1_mult = int(input("Digite um numero: "))
        numero2_mult = int(input("Digite outro numero: "))
    except ValueError:
        print("Digite apenas numeros!")
        return None
    resultado = numero1_mult * numero2_mult
    print(f"Sua multiplicacao: {resultado}!")
    print("______________________________________")
    return resultado


def expoente():
    try:
        base = int(input("Digite um numero base: "))
        expoente = int(input("Digite um numero expoente: "))
    except ValueError:
        print("Digite apenas numeros!")
        return None
    resultado = base**expoente
    print(f"Sua potencia: {resultado}!")
    print("______________________________________")
    return resultado


def raiz_quadrada():
    try:
        numero = int(input("Digite um numero: "))
    except ValueError:
        print("Digite apenas numeros!")
        return None
    raiz_quadrada = math.sqrt(numero)
    resultado = raiz_quadrada
    print(f"A raiz quadrada de {numero} é: {resultado}")
    return resultado


def raiz_cubica():
    try:
        numero = int(input("Digite um numero: "))
    except ValueError:
        print("Digite apenas numeros!")
        return None
    raiz_cubica = math.cbrt(numero)
    resultado = raiz_cubica
    print(f"A raiz cubica de {numero} é: {resultado}")
    return resultado


def fatorial():
    try:
        numero = float(input("Digite um numero: "))
    except ValueError:
        print("Digite apenas numeros!")
        return None
    fatorial = math.factorial(int(numero))
    resultado = fatorial
    if len(str(fatorial)) <= 10:
        print(f"O fatorial do seu numero: {numero}, é: {resultado}!")
        print("______________________________________")
    else:
        resultado_limitado = math.trunc(fatorial * 10**10) / 10**10
        print(f"O fatorial do seu numero {numero}, é muito grande")
        print(f"Esse é o resultado compactado: {resultado_limitado}!")
        print("______________________________________")
    return resultado
