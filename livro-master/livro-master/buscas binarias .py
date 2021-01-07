# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 17:42:45 2020

@author: Enterprise
"""


#busca binaria
import bisect
c = [1,2,2,2,3,4,7]
#fala onde deve ser inserido
bisect.bisect(c,2)
bisect.bisect(c,5)
#colocar ordenado o valor na lista
bisect.insort(c,6)
bisect.insort(c,2)
#fatimamento
seq = [7,2,3,7,5,6,0,1]
seq[1:5]
seq[3:4]= [6,3]
seq[:5]
seq[3:]
seq[-4:]
seq[-6:-2]
#realizar um salto
seq[::2]
#inverte a lista
seq[::-1]