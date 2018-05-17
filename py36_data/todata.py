import pandas as pd

def data(file):
    return pd.read_excel(file)

def alter(file,old_str,new_str):
   file_data = ""
   with open(file, "r", encoding="utf-8") as f:
         for line in f:
          if old_str in line:
             line = line.replace(old_str,new_str)
             file_data += line
          else: file_data += line
   with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)
# alter('123.txt','张鑫','江森辉')

a=data('123.xlsx')
for i in a.values:
     # print(i[0]+'-------'+i[1])
    alter('123.txt',i[1],i[0])
print('OK')
