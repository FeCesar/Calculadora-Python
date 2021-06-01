def maiorNumero(n1, n2):

    maiorNumero = [n1, n2]
    return max(maiorNumero)

def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    largest_number = maiorNumero(n1, n2)
    
    if(largest_number == n1):
        return n1 - n2
    
    if(largest_number == n2):
        return n2 - n1

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    largest_number = maiorNumero(n1 ,n2)

    if(largest_number == n1):
        return n1 / n2
    
    if(largest_number == n2):
        return n2 / n1

def calcular(operacao, n1, n2):

    if(operacao == '+'):
        soma(n1 ,n2)

    if(operacao == '-'):
        subtracao(n1, n2)
    
    if(operacao == '*'):
        multiplicacao(n1, n2)

    if(operacao == '/'):
        divisao(n1, n2)

def calculadora():

    repetir = True

    while(repetir):
        n1 = float(input("Digite o primeiro valor: "))

        print("-=-=-=- Selecione a Operação -=-=-=-")
        operacao = str(input("| + | - | * | / | -> "))

        n2 = float(input("Digite o segundo valor: "))

        print(calcular(operacao, n1, n2))

        repetir = str(input("Deseja continuar? S/N: "))
        if(repetir == "S"):
            repetir = True
        
        if(repetir == "N"):
            repetir = False

calculadora()