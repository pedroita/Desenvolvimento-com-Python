# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 22:18:40 2020

@author: Enterprise
"""
some_list=['foo','bar','baz']
mapping={}
# esse laço de repetição vai enumerar os valores da lista.
#o I sera o meu contador e meu V irá armazena os index da lista
for i, v in enumerate(some_list):
    mapping[v]=i

#sorted trabalha ordenando os valores.
sorted([7,1,2,6,0,3,2])

sorted('pedro')
#criar uma lista de tupla
seq1= ['pedro','italo','campos']
seq2= ['kelle','cordeiro','barreto']
zipped=zip(seq1,seq2)
list(zipped)
#remeveter numeros
list(reversed(range(100)))
