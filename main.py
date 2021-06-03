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
        valor = float(input("Digite o %dº número: " %(i)))
        valores.append(valor)

    resultado = np.sum(valores)

    print(resultado)

def subtracao(n1, n2):
    maior_numero = maiorNumero(n1, n2)
    
    if(maior_numero == n1):
        return n1 - n2
    
    if(maior_numero == n2):
        return n2 - n1

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    maior_numero = maiorNumero(n1 ,n2)

    if(maior_numero == n1):
        return n1 / n2
    
    if(maior_numero == n2):
        return n2 / n1

def calcular(operacao):

    if(operacao == '+'):
        qtd_numero_soma = int(input("Quantos números deseja somar: "))
        soma(qtd_parcelas)

    if(operacao == '-'):
        return subtracao()
    
    if(operacao == '*'):
        return multiplicacao()

    if(operacao == '/'):
        return divisao()

def calculadora():

    repetir = True

    while(repetir):    

        print("-=-=-=- Selecione a Operação -=-=-=-")
        operacao = str(input("| + | - | * | / | -> "))        

        calcular(operacao)

        repetir = str(input("Deseja continuar? S/N: "))
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
                repetir = str(input("Deseja continuar? S/N: "))
                repetir = repetir.upper()

calculadora()