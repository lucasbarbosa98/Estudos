#Calculadora Python
print ('Bem vindo a calculado ')
def add(x, y):
    return x + y 

def substract(x, y):
    return x - y

def multiplicacao (x,y):
    return x * y

def divisao (x,y):
    return x / y

print ('Selecione o numéro da opção desejada')
print ('1 = Soma')
print ('2 = Subtração')
print ('3 = Multiplicação')
print ('4 - divisão')

escolha = input ('Digite sua opção 1/2/3/4:')

num1 = int(input('Digite o numero'))
num2 = int(input('Digite o numero'))

if escolha == '1'
print()
print(num1, '+', num2, '=', add(num1, num2) )
print()

elif escolha == '2'
print()
print(num1, '-', num2, '=', substract(nume1, num2))
print()

elif escolha == '3'
print()
print(num1, '*', num2, '=', multiplicacao(num1,num2))
print()

elif escolha == '4'
print()
print(num1, '/', num2, '=', divisao(num1, num2))
print()

else:
    print('Opção invalida') 