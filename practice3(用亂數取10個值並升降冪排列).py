# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 12:23:38 2017

@author: User
"""

import random

a=[random.randint(1, 999) for _ in range(10)]
print(sorted(a))
print(sorted(a,reverse=True))