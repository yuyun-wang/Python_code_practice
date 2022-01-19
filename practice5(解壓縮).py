# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 17:56:03 2018

@author: user
"""       
#解壓縮
import zipfile
with zipfile.ZipFile('PYTHON.zip', 'r') as myzip:
    myzip.extract('PYTHON.txt')