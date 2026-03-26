num1 = float(input('Digite seu primeiro número:'))
num2 = float(input('Digite seu segundo número:'))
num3 = float(input('Digite seu terceiro número:'))
num4 = float(input('Digite seu quarto número:'))
produto = num1 * num2 * num3 * num4
print(f'O produto dos 4 números é: {produto}')
if produto > 0:
  print('O produto é positivo')
elif produto < 0:
  print('O produto não é positivo')