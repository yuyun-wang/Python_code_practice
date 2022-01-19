# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
# mypath = "D:/python"
mypath = "D:\\pyImageSearch"

for root, dirs, files in os.walk(mypath):
  print("路徑：", root)
  print("  目錄：", dirs)
  print("  檔案：", files)
  
