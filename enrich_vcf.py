import pandas
import pandas as pd

data2 = pandas.read_csv("RNA-Seq/auto_clean/exp_raw_count_normalized.txt", header=0, delimiter='\t')
column_list = list(data2.columns)
trimmed_list = []
name_list = []
for name in column_list:
  if ("R2" in name):
    #print(name[13:-4])
    trimmed_list.append(name)
data2 = data2.drop(trimmed_list, axis = 1)
for name in column_list:
  if (name == 'Gene ID'):
    continue
  if ("R2" not in name):
    data2[name[13:-4]] = data2[name]
    name_list.append(name)
data2 = data2.drop(name_list, axis = 1)

names = list(data2.columns)
tag = []
for name in names:
  if (name == 'Gene ID'):
    continue
  tag.append(int(name.split('-')[0][1:]))

data2 = data2.T

data2.columns = data2.iloc[0]
data2 = data2[1:]

data2 = data2.apply(pd.to_numeric)

data2['GeneID'] = tag

data2 = data2.groupby('GeneID').mean()

data2 = data2.T

data2.reset_index(level=0, inplace=True)

data1 = pandas.read_csv("Enriched_Accessions.csv", header=2, delimiter=',')

line_name = list(data1['Line'])
plant_id = list(data1['Plant ID'])
len(line_name)
old_col = list(data2.columns)[1:]
len(old_col)

i = 0
for number in old_col:
  data2[line_name[i]] = data2[number]
  i = i+1
data2 = data2.drop(old_col, axis=1)
data2.to_csv("RNA-seq_data.txt", index = False, sep = '\t')


trimmed = pandas.read_csv("trimmed_merged.vcf", header=62, delimiter='\t')

genes = []
for i in range(5471):
  genes.append(trimmed['INFO'][i].split(';')[-1][6:])
genes

trimmed.insert(3, "Genes", genes)
trimmed.to_csv("trimmed_enriched.vcf", index = False, sep = '\t')
