#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 09:27:54 2020

@author: pedro
"""


a = 'isso é uma string'
b = "isso é uma string com aspas duplas"
#é possivel escrever uma string com varias aspas
c= """
isso é uma string com aspas triplas
essa é uma segunda da linha da minha string
"""
a = 'isso é uma string'
a[10]= 'f'
b = a.replace('string', 'longer string')#concatenar a string
a
a = 5.6
s = str(a)
print (s)
type (s)
s = 'python'
list (s)
s[:5]
s = '12\\34'
print (s)
# R significa que quero ler minha string do jeito que ta
s = r'this\haszno\specia\characters'
s
a = 'isso é minha primera linha'
b = 'isso é minha segunda linha'
#junta string
a + b

templade = '{0:.2f} {1:s} are worth US${2:d}'
#{0:.2f} formatar o primeiro argumento como um numero de ponto fluante
#{1:s} significa formata o segundo argumento como string
#{2:d} significa formata o segundo argumento como inteiro


templade.format(4.5560,'Pesso Argentino',1)
val =  "espanõl" 
val
val_utf8 = val.encode('utf8')
type(val_utf8)
val_utf8.decode('utf8')
True and False
False or True
s= '3.14159'
fval = float (s)
