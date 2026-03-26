num1 = int(input('Digite seu primeiro número:'))
num2 = int(input('Digite seu segundo número:'))
num3 = int(input('Digite seu terceiro número:'))
num4 = int(input('Digite seu quarto número:'))
soma = num1 + num2 + num3 + num4
print(f'A soma dos 4 números é: {soma}')
if soma > 100:
    print('A soma é maior que 100')
elif soma == 100:
    print('A soma é igual a 100')
elif soma < 100:
    print('A soma não é maior que 100')


