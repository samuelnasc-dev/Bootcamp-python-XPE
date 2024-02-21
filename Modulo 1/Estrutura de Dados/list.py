#estrutra de dados em python - listas

#o que é:
#É uma sequencia ORDENADA de valores, que são identificados por um índice. Estes valores, que compoẽm uma lista são chamados de elementos ou itens.

#Uma lista é também mutável e dinâmica. Uma vez que sejam criadas, é possível: Alterar o valor de um ou mais elementos; Os elementos podem ser adicionados, removidos ou substituidos; A ordem dos elementos pode ser alterada.

lista1 = [1,2,3,4]
lista2 = [4,3,2,1]
lista3 = [1,2,3,4]

print(lista1 == lista2)

#lista com valores heterogÊneos

listaHeterogenea = [2, 'a', 5.44, True, None]

#listas com outras listas dentro.(listas aninhadas)

a = [2,7]
listaAninhada = [1, a, 'dois', [4, 5, a], '#']

print(listaAninhada)

#acessos
#igual como todos os outros
lista4 = ['casa', 1, '@samuel', True, 26]

print(lista4[0])
print(lista4[3])
print(lista4[-5])

#acessar por intervalos
print(lista4[1:4])
print(lista4[-2:])
print(lista4[:])

#exercicio da maior idade

idades = [343,10,35,100,67,89,45,33,36,200]
maior_idade = idades[0]

#idade é um apelido dado a cada elemento da lista idades[].
for idade in idades:
    if idade > maior_idade:
        maior_idade = idade

print('Maior idade: ' + str(maior_idade))

#alteração da lista
#adicionando um novo valor a lista com o append()

lista5 = ['amor', 4, 45, 26, True, None]
lista5.append(20/2)
lista5.append(2 == 2*4)
print(lista5)

#adicione o valor 999 a lista 5
lista5.append(999)
print(lista5)

#adicione +1 ao valor do ultimo elemento da lista
lista5[-1] = lista5[-1] + 1
print(lista5)

#remove() remove a primeira ocorrencia do atributo que vc passar.

#operadores de concatenação (+), repetição (*) e filiação (in)

a1 = [10, 30, 88]
a2 = [2, 'a', 5.44, 34]

#concatenação
print(a1 + a2)
#repetição
print(a1 * 2)
#filiação é verificar se um valor esta na lista
print('a' in a2)

#funções uteis
print(len(a1)) #retorna o tamanho da lista
print(sum(a1)) #retorna a soma de todos os elementos
print(max(a1)) #retorna o maior elemento
a1.reverse() #reverte a posição dos elementos de trás para frente
a1.extend([1,2,3,4,5]) #adiciona uma sequencia a lista atual em vez de somente um elemento
a1.sort() #ordena os valores da lista
a1.insert(2, 'novo valor') #adiciona um elemento em um índice especificado
a1.pop() #remove o ultimo elemento da lista
a1.clear() # limpa a lista

#metodos que retornan valores e não alteram os elementos
a1 = [10, 30, 88, 10, 22, 10]
print(a1.index(30)) # retorna o indice do valor 30
print(a1.count(10)) # retorna a quantidade de ocorrencia do valor passado por atributo

#resolvendo o problema das idades:
idades = [343,10,35,100,67,89,45,33,36,200]
print('maior idade:',max(idades))

#criando uma lista de idades usando o range()
idades = list(range(3, 1000))
maior_idade = idades[0]
for idade in idades:
    if idade > maior_idade:
        maior_idade = idade

print('maior idade:',maior_idade)
    