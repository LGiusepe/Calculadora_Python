import operacaoMat

# Opção e cálculo
def opcao (i, numero1, numero2):
    if i == "soma":
        resultado = operacaoMat.soma(numero1, numero2)
        print(f"Resultado da soma: {resultado}")
    elif i == "subt":
        resultado = operacaoMat.subt(numero1, numero2)
        print(f"Resultado da subtração: {resultado}")
    elif i == "multip":
        resultado = operacaoMat.multip(numero1, numero2)
        print(f"Resultado da multiplicação: {resultado}")
    elif i == "div":
        if numero2 == 0:
            print("Erro! Divisão por zero não é permitida.")
        else:
            resultado = operacaoMat.div(numero1, numero2)
        print(f"Resultado da divisão: {resultado}")