import operacaoMat

# Opção e cálculo
def opcao(operacao, num1, num2):
    if operacao == "soma":
        resultado = num1 + num2
    elif operacao == "subt":
        resultado = num1 - num2
    elif operacao == "div":
        resultado = num1 / num2
    elif operacao == "multip":
        resultado = num1 * num2
    else:
        print("Operação inválida!")
        return

    print(f"O resultado da operação {operacao} é: {resultado}")
