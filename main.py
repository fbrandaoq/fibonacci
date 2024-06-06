# funcao fibonacci
def calcular_fibonacci(n):
    if n <= 1:
        return n
    else:
        return calcular_fibonacci(n - 1) + calcular_fibonacci(n - 2)

# programa principal
n = int(input('Informe o número de sequências Fibonacci: '))

# exibe a sequência
for x in range(n):
    print(calcular_fibonacci(x))
