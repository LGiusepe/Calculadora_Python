def valida_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError: #caso ocorra erro de valor, loop continua solicitando a entrada de dados
            print("Entrada inválida! Digite um número válido.")
            
def validaDiv(i):
    numero2 = valida_numero("Digite o segundo número: ")
    if i == 'div':  # Se for divisão, garantir que número2 não seja zero
        while numero2 == 0:  
            print('Desculpe, operação de divisão por zero não disponível.')
            numero2 = valida_numero("Digite um número diferente de zero: ")
    return numero2
