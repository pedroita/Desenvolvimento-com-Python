# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:24:12 2020

@author: Enterprise
"""


#estruturas de  dados e sequências

#TUPLA
tum = 1,4,6,9

nested_tup = (4,5,6),(7,8)
nested_tup
tuple([4,0,2])
#converter uma sequencia em lista
tup = (tuple('string'))
tup[0]
# Depois de criado a lista nao podera ser mudar 
tup = tuple(['foo',[1,2],True])
tup[2] = False
# Se o obejeto for mutavel
#adicionei 3 a lista na posicao 1 
tup[1].append(3)
# Agora a lista esta assim ('foo',[1,2,3],True)
# concatenar tuplas usando o operador+
(4,None,'foo')+(6,0)+('bar',)
#mutiplicar uma tupla
('foo','bar')*4
#desempacotar uma tupla

tup =(4,5,6)

a,b,c = tup
b
tup = 4,5,(6,7)
a,b,(c,d)=tup
d
a,b =1,2
a
b,a= a,b

# outras funcionalidades
seq = [(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in seq:
    print ('a={0},b={1},c={2}'.format(a,b,c))
# arancar algum elemento da tupla
values = 1,2,3,4,5
a,b,*rest = values
a,b
rest
#geralmente programadores usam apenas (_)

a,b, *_= values
_
#metodos e tuplas
#count cont ao numero de ocorencia de algo na lista ou tupla
a = (1,2,3,9,4,2,2,4,2)
a.count(2)
a.count(1)
a.count(3)
#lista seu conteudo pode ser modificado
#None e variavel do tipo null em python se uma função não tiver um valores ela ira retonar none
a_list = [2,3,7,None]
tum = ('foo', 'bar', 'baz')
b_list = list (tum)
b_list
b_list [1]= 'peekaboo'
b_list

gen = range(10)
gen
list(gen)
#adicionando elementos

b_list.append('dwarf')
#indico qual posicao eu quero e coloco minha string
b_list.insert(1,'red')
#remover pop
b_list.pop(2)
b_list.append('foof')
b_list.remove('foo')
'foof' in b_list

#concatenando lista
x = [4,None,'foo']
x.extend([7,8,(2,3)])
x
#ordenando
#sort ordena a lista
a = [7,2,5,1,3]
a.sort()
#sort key= len é uma chave de ordenação segundaria
b = ['campos','silva','pedro','italo','vinte']
b.sort(key=len)
b
