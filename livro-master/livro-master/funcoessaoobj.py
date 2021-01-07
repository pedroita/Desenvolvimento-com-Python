# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 23:17:01 2020

@author: Enterprise
"""
""" funçoes sao objeto"""
a = None
def bind_a_variable():
    global a
    a=[]
    bind_a_variable()
print (a)


def f():
    a=5
    b=6
    c=7
    return a,b,c

a,b,c= f()

state = ['Alabama','Georgia!','Gergia','georgia','FlOrIda','carolina  sul##','Oeste virginia?']

import re

def clear_string(strings):
    result=[]
    for value in strings:
        value = value.strip()
        value = re.sub('!#?','',value)
        value=value.title()
        result.append(value)
    return result

clear_string(state)

def remover_putuacao(value):
    return re.sub('[!#?]','',value)
clean_ops=[str.strip,remover_putuacao,str.title]
def clear_string(strings,ops):
    result=[]
    for value in strings:
        for funtion in ops:
            value=funtion(value)
        result.append(value)
    return result
clear_string(state,clean_ops)    

for x in map(remover_putuacao,state):
    print (x)
