print("Operadores de lista")

lista = [1, 2, 3, 4, 5]
print(lista)
print(lista[2])  # Acessando um elemento da lista pelo indice
print(lista[-2])  # Acessando um elemento da lista pelo indice negativo
print(len(lista))  # Tamanho
print(lista + [6, 7, 8])  # Concatenacao
print(lista * 3)  # Repeticao
print(3 in lista)  # Verifica se um elemento esta na lista
del lista[2]  # Deletando um elemento da lista
print(lista)
lista[2] = 33  # Alterando um elemento da lista
print(lista)
print('=' * 30)

print()
# A diferenca entre uma lista e uma tupla e que a tupla e imutavel (nao pode ser alterada)

print("Tuplas")
tupla = (1, 2, 3, 4, 5)
print(tupla)
print(tupla[2])  # Acessando um elemento da tupla pelo indice
print(tupla[-2])  # Acessando um elemento da tupla pelo indice negativo
print(len(tupla))  # Tamanho
print(tupla + (6, 7, 8))  # Concatenacao
print(tupla * 3)  # Repeticao
print(3 in tupla)  # Verifica se um elemento esta na tupla
print('=' * 30)
