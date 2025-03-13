print('Estruturas condicionais')
idade: int = 18

print("if")
if idade >= 18:
    print('Você e maior de idade')
print('=' * 30)

print()

print('If else')
if idade >= 18:
    print('Você e maior de idade')
else:
    print('Você e menor de idade')
print('=' * 30)

print()

print('If elif else')
if idade < 12:
    print('Crianca')
elif idade < 18:
    print('Adolescente')
else:
    print('Adulto')
print('=' * 30)
