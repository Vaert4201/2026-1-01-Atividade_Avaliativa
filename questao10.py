num1 = int(input('Digite o seu primeiro número:'))
num2 = int(input('Digite o seu segundo número:'))
num3 = int(input('Digite o seu terceiro número:'))
num4 = int(input('Digite o seu quarto número:'))
media = (num1 + num2 + num3 + num4) / 4
print(f'A média é: {media}')
if media >= 6:
  print('Aprovado!')
elif media < 6:
 print('Reprovado!')
  
