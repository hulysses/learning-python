# Primeiro script em Python:
print('Hello world!')
print('=' * 30)

# Recebendo dados do usuario
print('Recebendo dados do usuario')
nome = input('Digite seu nome: ')
idade: int = int(input('Digite sua idade: '))
print('=' * 30)

# Formatacao de strings
print('Formatacao de strings')
print(f'Ola, {nome}!')
print(f'Você tem {idade} anos')
print('=' * 30)

# Estruturas condicionais
print('Estruturas condicionais')
print('If else')
if idade >= 18:
    print('Você e maior de idade')
else:
    print('Você e menor de idade')
print('=' * 30)

print('If elif else')
if idade < 12:
    print('Crianca')
elif idade < 18:
    print('Adolescente')
else:
    print('Adulto')
print('=' * 30)

