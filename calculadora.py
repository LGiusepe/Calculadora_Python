#Operações Matemáticas 
def soma(a, b):
    return a + b
def subt(a,b):
    return a - b
def div(a,b):
    return a / b
def multip(a,b):
    return a * b

#Validação de entrada de dados
def valida_numero(numero):
    while True:
        try:
            return float(input(numero))
        except ValueError: #caso ocorra erro de valor, loop continua solicitando a entrada de dados
            print("Entrada inválida! Digite um número válido.")


#Apresentação
print('Bem Vindo a minha calculadora python')
print('Vamos selecionar a opção desejada!!')

op_valida = False  # Variável de controle do loop

while not op_valida:  # Enquanto a operação não for válida, continua pedindo
    i = input("Escolha seu método de operação (soma, subt, div, multip): ").strip().lower()
    
     # Lista de operações válidas
    operacoes_validas = ["soma", "subt", "div", "multip"]

    if i in operacoes_validas:
        op_valida = True  # Sai do loop
    else:
        print("Operação inválida. Tente novamente.")

numero1 = valida_numero("Digite o primeiro número: ")
numero2 = valida_numero("Digite o segundo número: ")


#Validação de Opção
if i == "soma":
    resultado = soma(numero1, numero2)
    print(f"Resultado da soma: {resultado}")
elif i == 'subt':
    resultado = subt(numero1, numero2)
    print(f'Resultado da subtração: {resultado}')
elif i == 'subt':
    resultado = subt(numero1, numero2)
    print(f'Resultado da subtração: {resultado}')
elif i == 'subt':
    resultado = subt(numero1, numero2)
    print(f'Resultado da subtração: {resultado}')

    


   
