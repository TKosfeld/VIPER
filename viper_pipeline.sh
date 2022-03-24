#!/usr/bin/env bash
python3 enrich_vcf.py
python3 vcf_parse.py
python3 accession_split.py
mkdir split_ranks
python3 gene_rank.py