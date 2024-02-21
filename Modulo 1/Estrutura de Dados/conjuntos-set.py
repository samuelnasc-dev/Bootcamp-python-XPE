#Estrutura de dados, conjuntos(set)

#delcaração de conjunto homogeneo
c1 = {3, 0, 1, 4, 3}
print(c1)

#o motivo do 3 não aparecer duas vezes é que em um conjunto não há repetição de elementos. A ordem também não importa.

c2 = {3,1,4,4,0,3}
print(c2 == c1)

#conjunto heterogeneo
c3 = {2, 'a', 'amor', 'Barata', "barata", 5.44, 0, True, None}
print(c3)

#Operações entre conjuntos
a = {1,2,3,4,5}
b = {4,5,6,7,8}

#União (A U B)
print('A U B => ', a|b)
print('a.union(b) =>', a.union(b))

#Interseção (A n B)
print('A & B => ', a & b )
print('A.intersection(b) => ', a.intersection(b))

#Diferença (A - B)
print('A - B => ', a-b)
print('A.difference(B) => ', a.difference(b))
#ou vice-versa

#Criação dos conjuntos A e B
c1 = {1,2,3,4,5}
c2 = {4,5}
c3 = {91, 92, 93}

#.add() Adiciona um elemento ao conjunto
c1.add(6)
print(c1)

#.update ele adiciona novos valores ao conjunto
# c1.update([2,45,67,8,90,23])
print('update: ', c1)

#len(a-b) Pega o tamamnho do conjunto
print(len(a-b))
print(len(a))
print(len(b))
print(len(a&b))

#c1.remove(elemento) remove o elemento indicado do conjunto
c1.remove(5)
print(c1)

#c1.discard(8) descarta o elemento indicado mas se não existir ele não apresent erro como o remove.
c1.discard(8)
print(c1)

#Verificar se os conjuntos não possuem nenhum elemento em comum(disjunto)
c1.add(5)
print(c1)
print(c2)
print(c3)
print(c1.isdisjoint(c2))
print(c1.isdisjoint(c3))

#verifica se o conjunto é subconjunto de outro
print('Conjunto é subconjunto de outro?')
print(c1.issubset(c2))
print(c1.issubset(c3))
print(c2.issubset(c1))

#verifica se o conjunto contém outro conjunto
print('O conjunto contém outro conjunto?')
print(c1.issuperset(c2))

#Exercício
""" Problema 1: Em uma escola de idiomas existem 3 turmas diferentes, uma de Inglês, uma de espanhol e uma de Francês. O diretor que o nome de todos os alunos escritos em pelo menos uma turma da escola sem repetição.

(nós resolvemos esse problema com conjuntos, já que se utilizássemos listas, os nomes iriam repetir na relação geral de alunos) """

ING = {'Lucas', 'Matheus', 'Gabriel', 'Ana', 'Bruna', 'Anitta', 'Lana', 'Kelly', 'Pedro'}
ESP = {'João', 'Miguel', 'Anitta', 'Bruna', 'André', 'Carlos', 'Guilherme', 'Bruno', 'Felipe', 'Geremias'}
FRA = {'Gustavo', 'Anitta', 'Rafael', 'Lucas', 'Leonardo', 'Victor', 'Matheus', 'Ana', 'Alexandre'}

#resolução
# '|' é o operador de união
print('Lista de todos os alunos da turma')
everybody = ING | ESP | FRA
print(everybody)

""" Problema 2: Agora, com a relação de todos os alunos, o diretor decidiu dá um desconto aos alunos que estão matriculados em pelo menos 2 turmas de idiomas independente da escolha. O problema é conseguir essa lista de alunos que estão matriculados em pelo menos 2 turmas diferentes. """

#resolução
#Vamos pegar as intersseções das turmas, assim teremos uma lista com alunos que estão pelo menos em 2 cursos diferentes.
#'&' é o operador de intersseção
print('Lista de alunos que estão em pelo menos 2 turmas de idiomas')
descontList = (ING & ESP) | (ING & FRA) | (ESP & FRA)
print(descontList)