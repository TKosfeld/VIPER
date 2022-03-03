import multiprocessing
from multiprocessing import Manager, Pool
import pandas
import pandas as pd
import numpy as np
manager = Manager()
info_list = manager.list()

with open("merged.ont.v1.0.vcf") as myfile:
  head = [next(myfile) for x in range(62)]
myfile.close()
with open('trimmed_merged.vcf', 'w') as f:
  for item in head:
    f.write("%s" % item)
f.close()
data = pandas.read_csv("merged.ont.v1.0.vcf", header=62, delimiter='\t')

def check_info(info):
  global info_list
  if ("genes" in info):
    #print('hello')
    info_list.append(int(list_info.index(info)))
    

list_info = list(data['INFO'])
pool = Pool(20)
pool.map(check_info, list_info)
pool.close()
pool.join()

num = info_list[0]
#print(list_info[num].split(';'))
true_list = list(info_list)
for item in true_list:
  if (type(item) == int):
    continue
  print(item)
#print(info_list)

trimmed_data = data.iloc[true_list]
print(trimmed_data)

data1 = pandas.read_csv("Enriched_Accessions.csv", header=2, delimiter=',')
acc_list = list(data1['Line'])
acc_list = ['{0}.ont.s'.format(element) for element in acc_list]
columns = list(trimmed_data.columns)
columns = columns[0:9]
columns.extend(acc_list) 
trimmed_data = trimmed_data[columns]
trimmed_data = trimmed_data.replace('./.:NA:NA', np.nan)
trimmed_data = trimmed_data.dropna(thresh = 15)
#print(trimmed_data)
insertions = pandas.read_csv("insertions_Dec6_run_REPET_annotation.gff3", header=None, delimiter='\t')
insertions2 = pandas.read_csv("deletions_Dec6_run_REPET_annotation.gff3", header=None, delimiter='\t')
insertions = insertions.append(insertions2)
insertions['ID'] = insertions[0]
insertions['source'] = insertions[1]
insertions['type'] = insertions[2]
insertions['start'] = insertions[3]
insertions['end'] = insertions[4]
insertions['score'] = insertions[5]
insertions['strand'] = insertions[6]
insertions['phase'] = insertions[7]
insertions['attributes'] = insertions[8]
insertions = insertions.drop(range(0,9), axis=1)
trimmed_data = pd.merge(trimmed_data, insertions, on=['ID', 'ID'], how = 'left')
trimmed_data = trimmed_data.drop_duplicates(subset=['ID'])
print(trimmed_data)
trimmed_data.to_csv("trimmed_merged.vcf", index = False, sep = '\t', mode = 'a')
