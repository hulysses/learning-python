"""
    Inicio do estudo de logica de programaçao com python

    Logica de programcao e o estudo da estrutura da linguagem das maquinas. Computadores sao extremamente literais, e precisam de
    instrucoes claras e precisas para executar tarefas. Essas instrucoes sao escritas atraves de algoritmos, que sao sequencias de
    passos que descrevem como realizar uma tarefa.

    Variaveis e constantes
      Sao espacos de memoria que armazenam valores. As variaveis podem ser alteradas durante a execucao do programa.
      Constantes sao valores que nao podem ser alterados durante a execucao do programa.

    Operadores
     Sao simbolos que representam uma operacao matematica ou logica. Os operadores basicos sao:
          Aritmeticos: +, -, *, /, %, **
          Comparacao: ==, !=, <, >, <=, >=
          Logicos: and, or, not
          Atribuicao: =, +=, -=, *=, /=, %=, **=

    Estruturas de controle de fluxo
     Sao utilizadas para alterar o fluxo de execucao de um programa. As estruturas de controle de fluxo mais comuns sao:
          Condicionais: if, elif, else

    Estrutura de repeticao
     Sao utilizadas para repetir um bloco de codigo, enquanto uma condicao for verdadeira. As estruturas de repeticao mais comuns sao:
          Repeticao: for, while
"""

# Primeiro script em Python:
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

# Conversao de tipos
print('Conversao de tipos')
print(int('1'))
print(float('1'))
print(str(1))
print(bool(''))
print(bool(' '))
print(bool(0))
print(bool(1))
print('=' * 30)

# Operaçoes matematicas
print('Operaçoes matematicas')
print(1 + 2)  # Soma
print(1 - 2)  # Subtracao
print(1 * 2)  # Multiplicacao
print(1 / 2)  # Divisao
print(5 // 2)  # Divisao inteira
print(1 % 2)  # Resto da divisao
print(2 ** 3)  # Potenciacao
print('=' * 30)

# Operaçoes com strings
print('Operacoes com strings')
print('a' + 'b')  # Concatenacao
print('a' * 3)  # Repeticao
print(len('Ola'))  # Tamanho da string
print('=' * 30)

# Variaveis
print('Variaveis')
a: int = 1  # Declaracao de variavel tipada
b: float = 2
print(a + b)
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

#  Operadores de comparacao
print('Operadores de comparacao')
print(1 == 1)  # Igualdade
print(1 != 1)  # Diferenca
print(1 < 2)  # Menor que
print(1 > 2)  # Maior que
print(1 <= 2)  # Menor ou igual
print(1 >= 2)  # Maior ou igual
print('=' * 30)

# Operadores logicos
print('Operadores logicos')
print(True and True)
print(True and False)
print(True or False)
print(not True)
print('=' * 30)
