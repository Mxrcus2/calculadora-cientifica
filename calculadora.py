import os

from functions import (
    adicao,
    subtracao,
    divisao,
    multiplicacao,
    expoente,
    raiz_quadrada,
    raiz_cubica,
    fatorial,
    porcentagem,
    obterRadiano,
)

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
    4: "Porcentagem",
    5: "Obter Radiano de angulo",
    6: "Voltar a calculadora",
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
        print("______________________________________")
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
                    print("______________________________________")
                if opcao_raiz == 2:
                    raiz_cubica()
                    print("______________________________________")
                if opcao_raiz == 3:
                    os.system("cls")
            case 3:
                os.system("cls")
                fatorial()
            case 4:
                os.system("cls")
                porcentagem()
                print("______________________________________")
            case 5:
                os.system("cls")
                obterRadiano()
                print("______________________________________")
            case 6:
                os.system("cls")
                calculadora = True
