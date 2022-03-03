from multiprocessing import Pool
import csv
from multiprocessing import Process, Manager
import pandas

trimmed = pandas.read_csv("trimmed_enriched.vcf", header=0, delimiter='\t')
data2 = pandas.read_csv("RNA-seq_data.txt", header=0, delimiter='\t')

data2['Gene ID'] = [x[:16] for x in data2['Gene ID']]

from scipy import stats

split = trimmed.drop(['#CHROM', 'POS', 'INFO', 'QUAL', 'FILTER', 'FORMAT', 'source', 'type', 'start', 'end', 'score', 'strand', 'phase', 'attributes'], axis=1)
split.columns = split.columns.str.rstrip('.ont.s') 

def gene_mann(gene):
  row = data2.loc[data2['Gene ID'] == gene]
  row.set_index('Gene ID', inplace=True)
  if (row.empty == True):
    return 1;
  if (row.iloc[0].mean() == 0.0):
    return 1;
  row_SV = row.loc[:, ~series.isna()[4:]]
  row_noSV = row.loc[:, series.isna()[4:]]
  #print(row_noSV.iloc[0])
  #print(row_SV.iloc[0])
  if (row_SV.empty == True):
    return 1;
  if (row_noSV.empty == True):
    return 1;
  try:
    _, pval = stats.mannwhitneyu(row_noSV.iloc[0], row_SV.iloc[0], alternative='two-sided')
  except ValueError as e:
    print(row_noSV.iloc[0])
    print(row_SV.iloc[0])
  #print(pval)
  return pval

#f = open('SV_Gene_Pairs.tsv', 'w')
def map_dict(gene):
  p_dict.setdefault(gene, gene_mann(gene))

manager = Manager()
rank_list = []

for i in range(200, len(split)):
  series = split.iloc[i]
  gene_list = list(data2['Gene ID'])
  #print(gene_list)
  pos_gene = series['Gene']
  print(i)
  if (pos_gene not in gene_list):
    continue
  print("Processing p-values for " + pos_gene)
  p_dict = manager.dict()
  pool = Pool(20)
  pool.map(map_dict, gene_list)
  pool.close()
  pool.join
  #for gene in gene_list:
  #  p_dict.setdefault(gene, gene_mann(gene))
  #print(p_dict)
  p_dict = {k: v for k, v in sorted(p_dict.items(), key=lambda item: item[1])}
  print('Writing to split_ranks/'+pos_gene)
  with open('split_ranks/'+pos_gene+'.tsv', 'w') as f:
    f.write(pos_gene + '\t' +str(list(p_dict.keys()).index(pos_gene)) + '\n')
    f.write('Gene\tP-Value\tBinary\n')
    rank_list.append(pos_gene + '\t' +str(list(p_dict.keys()).index(pos_gene)) + '\t' + str(p_dict[pos_gene]) + '\n')
    for key in p_dict.keys():
      if (key == pos_gene):
        f.write("%s\t%s\t1\n"%(key,p_dict[key]))
      else:
        f.write("%s\t%s\t0\n"%(key,p_dict[key]))
with open('gene_ranks.tsv', 'w') as filehandle:
    for listitem in rank_list:
        filehandle.write('%s' % listitem)
