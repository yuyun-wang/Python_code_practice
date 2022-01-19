# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 09:38:50 2017

@author: User
"""
Sentence = """Avoid finding yourself alone with a congressman or senator in elevators, 
            late-night meetings or events where alcohol is flowing. And think twice  
            before speaking out about sexual harassment from a boss."""
letters = [chr(i+97) for i in range(26)]
counter = [0 for i in range(26)]

for s in Sentence:
    if ord('A')<=ord(s)<=ord('Z'):
        num=ord(s)-ord('A')
        counter[num] += 1
    elif ord('a')<=ord(s)<=ord('z'):
        num=ord(s)-ord('a')
        counter[num]+=1

zipper=zip(letters,counter)
print (list(zipper))