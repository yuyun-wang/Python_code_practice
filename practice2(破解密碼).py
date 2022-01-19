# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 12:14:08 2017

@author: User
"""


keyboards = r"`1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./"
#keyboards2 = keyboards.replace(".1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./","234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./")

while(1):
    password=input("請輸入一個密碼[按 空白鍵+ENTER 離開]: ")
    
    
    password.lower()
    ind=keyboards.find(password.lower()) 
    
    print( keyboards[ind-2])
   

    if password==" ":
        break