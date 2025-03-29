import selecaoOpcao
import validacaoEntrada

# Apresentação
print('Bem-vindo à minha calculadora Python!')
print('Vamos selecionar a opção desejada!')

op_valida = False  # Variável de controle do loop

while not op_valida: # Enquanto a operação não for válida, continua pedindo
    operacao = input("Escolha seu método de operação (soma, subt, div, multip): ").strip().lower()
    
    # Lista de operações válidas
    if operacao in ["soma", "subt", "div", "multip"]:
        op_valida = True # Sai do loop
    else:
        print("Operação inválida. Tente novamente.")

# Solicitação de números
numero1 = validacaoEntrada.valida_numero("Digite o primeiro número: ")
numero2 = validacaoEntrada.validaDiv(operacao)

# Chama a função que executa a operação
selecaoOpcao.opcao(operacao, numero1, numero2)