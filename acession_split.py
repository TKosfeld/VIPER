import numpy
import pandas
import pandas as pd
from scipy import stats
import statsmodels.api
trimmed = pandas.read_csv("trimmed_enriched.vcf", header=0, delimiter='\t')
#print(trimmed)

split = trimmed.drop(['#CHROM', 'POS', 'INFO', 'QUAL', 'FILTER', 'FORMAT', 'source', 'type', 'start', 'end', 'score', 'strand', 'phase', 'attributes'], axis=1)
split.columns = split.columns.str.rstrip('.ont.s') 
#print(split)

rna_data = pandas.read_csv("RNA-seq_data.txt", header=0, delimiter='\t')
rna_data['Gene ID'] = [x[:16] for x in rna_data['Gene ID']]
#print(rna_data)


def gene_mann(gene):
  row = rna_data.loc[rna_data['Gene ID'] == gene]
  row.set_index('Gene ID', inplace=True)
  if (row.empty == True):
    return 1;
  if (row.iloc[0].mean() == 0.0):
    return 1;
  row_SV = row.loc[:, ~series.isna()[4:]]
  row_noSV = row.loc[:, series.isna()[4:]]
  #print(len(row_SV.columns))
  if (len(row_SV.columns) < 5 or len(row_noSV.columns) < 5):
    return 1;
  print(row_noSV.iloc[0])
  print(row_SV.iloc[0])
  _, pval = stats.mannwhitneyu(row_noSV.iloc[0], row_SV.iloc[0], use_continuity=False, alternative='two-sided')
  #print(pval)
  return pval

df = pd.DataFrame(columns = ['Gene', 'SV', 'P-Value'])

#for i in range(len(split)):
for i in range(1):
  series = split.iloc[i]
  #print(series)
  gene_list = series['Gene'].split(',')
  agg = 0
  for gene in gene_list:
    agg = gene_mann(gene) + agg
  p = agg/(len(gene_list))
  #print(p)
  df.loc[i] = [series['Gene'], series['ID'], p] 

  #if (p < .05):
  #  print("Gene=" + series['Gene'] + "\t SV=" + series['ID'] + "\t" + str(p) + '\n')
_, p_corrected, _, _ = statsmodels.stats.multitest.multipletests(df['P-Value'], alpha=0.05, method='fdr_bh')
#print(p_corrected.size)
df['Corrected P'] = p_corrected
df = df.loc[df['Corrected P'] < .05]
print(df)
#df.to_csv('SV_Gene_Pairs.tsv', sep = '\t', index = False)
