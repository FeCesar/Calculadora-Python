import numpy as np

def maiorNumero(n1, n2):

    maiorNumero = [n1, n2]
    return max(maiorNumero)

def soma(qtd_parcelas):
    
    valores = []
    if(qtd_parcelas < 2):
        print("Para realizar uma soma são necessários pelo menos dois números!")
        return
    
    for i in range(qtd_parcelas):
        valor = float(input("Digite o %dº número: " %(i + 1)))
        valores.append(valor)

    resultado = np.sum(valores)

    print(resultado)
    return

def subtracao():

    minuendo = float(input("Digite o minuendo: ")) 
    subtraendo = float(input("Digite o subtraendo: "))  

    resultado = minuendo - subtraendo

    print(resultado)
    return

def multiplicacao():

    fator1 = float(input("Digite um fator: ")) 
    fator2 = float(input("Digite o outro fator: ")) 

    produto = fator1 * fator2

    print(produto)
    return

def divisao():
    
    dividendo = float(input("Digite o dividendo: "))
    divisor = float(input("Digite o divisor: "))

    quociente = dividendo / divisor

    print(quociente)
    return

def calcular(operacao):

    if(operacao == '+'):
        qtd_numero_soma = int(input("Quantos números deseja somar: "))
        soma(qtd_numero_soma)
    elif(operacao == '-'):
        subtracao()
    elif(operacao == '*'):
        multiplicacao()
    elif(operacao == '/'):
        divisao()
    else:
        print("Operação Inválida!\n")
        return

def calculadora():

    repetir = True

    while(repetir):    

        print("-=-=-=- Selecione a Operação -=-=-=-")
        operacao = (input("| + | - | * | / | -> "))

        calcular(operacao)

        repetir = input("Deseja continuar? S/N: ")
        repetir = repetir.upper()

        finalizar = False
        while(finalizar == False):
            if(repetir == "S"):
                repetir = True
                finalizar = True
            elif(repetir == "N"):
                repetir = False
                finalizar = True
            else:
                finalizar = False                
                repetir = input("Deseja continuar? S/N: ")
                repetir = repetir.upper()

calculadora()