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


Interface = {
    1: "Adição",
    2: "Subtração",
    3: "Divisão",
    4: "Multiplicação",
    5: "Modo científico",
}

Interface_Cientifica = {
    1: "Expoente",
    2: "Raiz quadrada e cubica",
    3: "Fatorial",
    4: "Voltar a calculadora",
}

calculadora = True

while True:
    if calculadora == True:
        print("Bem vindo a calculadora do Markin 🤓☝")
        print("______________________________________")
        print(Interface)
        print("______________________________________")
        escolha = int(input("Digite o numero do operador que deseja: "))
        match escolha:
            case 1:
                os.system("cls")
                adicao()
            case 2:
                os.system("cls")
                subtracao()
            case 3:
                os.system("cls")
                divisao()
            case 4:
                os.system("cls")
                multiplicacao()
            case 5:
                os.system("cls")
                calculadora = False
    else:
        print("Calculadora cientifica do Markin🤓☝")
        print("____________________________________")
        print(Interface_Cientifica)
        print("______________________________________")
        escolha_cientifica = int(input("Digite um operador cientifico que deseja: "))
        match escolha_cientifica:
            case 1:
                os.system("cls")
                expoente()
            case 2:
                os.system("cls")
                opcao_raiz = int(
                    input(
                        "Se deseja raiz quadrada, digite 1| \nSe deseja raiz cubica, digite 2| \nSe deseja sair, digite 3: "
                    )
                )
                if opcao_raiz == 1:
                    raiz_quadrada()
                if opcao_raiz == 2:
                    raiz_cubica()
                if opcao_raiz == 3:
                    os.system("cls")
            case 3:
                os.system("cls")
                fatorial()
            case 4:
                os.system("cls")
                calculadora = True
