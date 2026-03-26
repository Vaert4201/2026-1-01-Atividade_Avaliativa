num1 = float(input('Digite o seu primeiro número:'))
num2 = float(input('Digite o seu segundo número:'))
num3 = float(input('Digite o seu terceiro número:'))
num4 = float(input('Digite o seu quarto número:'))
minnum = min(num1, num2, num3, num4)
maxnum = max(num1, num2, num3, num4)
media = (num1 + num2 + num3 + num4) / 4
diferença = maxnum - minnum
print(f'A média aritmética é: {media}')
print(f'A diferença entre o maior e o menor valor é: {diferença}')