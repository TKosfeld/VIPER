# VIPER

Structural variants (SV) are recognized as a prominent source of genetic variation, with single variants manifesting significant influence over phenotypic expression. However, their effects remain poorly understood due to computational limitations and a continued focus on SNPs. Addressing this need, we introduce the Variant Identification Pipeline with Expression Realization (VIPER), a robust computational pipeline created to identify and annotate structural variants with significant impact on gene expression. Using a publicly available structural variant collection as reference (Alonge et al., 2020), VIPER accepts processed RNA sequence data and constructs a list of SV-gene pairs based on genetic position. These SV-gene pairs are then evaluated by their differential expression values, with pairs expressing significant RPKM differentials concatenated to form a library of high-impact SV-gene pairs. Finally, the library is enriched by annotating genes for function, allowing for the identification and selection of candidate variants with desirable phenotypic influences.
To evaluate the efficacy of VIPER, we constructed a causal genomic library from a collection of 108 tomato leaf samples. A candidate insertion from this library, which we labelled GUNGIR, affirmed VIPER by expressing a  significant influence over leaflet morphology as quantified by a fivefold principal component system. 

<p align="center">
  <img width="1200" src="https://cdn.discordapp.com/attachments/215581700556718080/948988952948396032/Viper_1.png" alt="Figure 1">
</p>

<p align="center">
  <img width="1200" src="https://cdn.discordapp.com/attachments/215581700556718080/948988952361189477/Viper_2.png" alt="Figure 2">
</p>

<p align="center">
  <img width="1200" src="https://cdn.discordapp.com/attachments/215581700556718080/948988952621232179/Viper_3.png" alt="Figure 3">
</p>

<p align="center">
  <img width="1200" src="https://cdn.discordapp.com/attachments/215581700556718080/948988952084373574/Viper_4.png" alt="Figure 4">
</p>

<p align="center">
  <img width="1200" src="https://cdn.discordapp.com/attachments/215581700556718080/948988951790755890/Viper_5.png" alt="Figure 5">
</p>

<p align="center">
  <img width="1200" src="https://cdn.discordapp.com/attachments/215581700556718080/948988951534927872/Viper_6.png" alt="Figure 6">
</p>

<p align="center">
  <img width="1200" src="https://cdn.discordapp.com/attachments/215581700556718080/948988951245500476/Viper_7.png" alt="Figure 7">
</p>

<p align="center">
  <img width="1200" src="https://cdn.discordapp.com/attachments/215581700556718080/948988950628950016/Viper_8.png" alt="Figure 8">
</p>









