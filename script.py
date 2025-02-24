# Primeiro script em Python
print('Hello world!')
print('=' * 30)

#  Tipos de dados
print('Tipos de dados')
print(type(1))  # Inteiro
print(type(1.1))  # Float
print(type('1'))  # String
print(type(True))  # Boolean
print(type([]))  # Lista
print('=' * 30)

# Conversão de tipos
print('Conversão de tipos')
print(int('1'))
print(float('1'))
print(str(1))
print(bool(''))
print(bool(' '))
print(bool(0))
print(bool(1))
print('=' * 30)

print('Operações matemáticas')
# Operações matemáticas
print(1 + 2)  # Soma
print(1 - 2)  # Subtração
print(1 * 2)  # Multiplicação
print(1 / 2)  # Divisão
print(5 // 2)  # Divisão inteira
print(1 % 2)  # Resto da divisão
print(2 ** 3)  # Potenciação
print('=' * 30)

# Operações com strings
print('Operações com strings')
print('a' + 'b')  # Concatenação
print('a' * 3)  # Repetição
print(len('Ola'))  # Tamanho da string
print('=' * 30)

# Variáveis
print('Variaveis')
a: int = 1  # Declaração de variável tipada
b: float = 2
print(a + b)
print('=' * 30)

# Recebendo dados do usuário
print('Recebendo dados do usuário')
nome = input('Digite seu nome: ')
idade: int = int(input('Digite sua idade: '))
print('=' * 30)

# Formatação de strings
print('Formatação de strings')
print(f'Olá, {nome}!')
print(f'Você tem {idade} anos')
print('=' * 30)

# Estruturas condicionais
print('Estruturas condicionais')
print('If else')
if idade >= 18:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')
print('=' * 30)

print('If elif else')
if idade < 12:
    print('Criança')
elif idade < 18:
    print('Adolescente')
else:
    print('Adulto')
print('=' * 30)


