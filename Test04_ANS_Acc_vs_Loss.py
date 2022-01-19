# Utils_Acc_vs_Loss.py
# Purpose: Extracting values in columns of loss, acc, val_loss, and val_acc

# Epoch 1/75
# 312/312 [==============================] - 944s - loss: 3.5901 - acc: 0.5760 
#                                         - val_loss: 2.7088 - val_acc: 0.6470 
import json
import pandas as pd

fileName   = "Test04_Acc_vs_Loss"
inputName  = fileName + ".txt"
outputJSON = fileName + ".json"
outputCSV  = fileName + ".csv"

rows       = open(inputName).read().strip().split("\n")
rows       = [rows[i+1] for i in range(0, len(rows), 2)]
values     = [r[r.find("l"):].split(" ") for r in rows]

lst      = ([],[],[],[])
buffer   = {'loss':[], 'acc':[], 'val_loss':[], 'val_acc':[]}
for i in range(len(values)):
	lst[0].append(values[i][1])
	lst[1].append(values[i][4])
	lst[2].append(values[i][7])
	lst[3].append(values[i][10])

# update dictionary
buffer.update({'loss' : lst[0]})
buffer.update({'acc' : lst[1]})
buffer.update({'val_loss' : lst[2]})
buffer.update({'val_acc' : lst[3]})

# write results into a json file
f = open(outputJSON, "w")
f.write(json.dumps(buffer))
f.close()

# write results into a csv file
pd.DataFrame.from_dict(data=buffer, orient='columns').to_csv   \
	(outputCSV, columns=['loss', 'acc', 'val_loss', 'val_acc'], \
    header=['loss', 'acc', 'val_loss', 'val_acc'])
