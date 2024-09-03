

## Features

- **Organism Selection**: Identify and select organisms of interest from a list.
- **Sequence Filtering**: Filter sequences based on length and the presence of methionine (M) at the start of the sequence.
- **Automated Processing**: Use shell scripts to automate the filtering process across multiple datasets.

## Requirements

- Python 3.x
- `argparse` and `re` libraries
- `orthofinder` https://github.com/davidemms/OrthoFinder


### 1. Selecting Organisms of Interest

The `my_orgs.txt` file contains the list of organisms of interest. Modify this list to include any organism names present in `allorgs.txt`.

### 2. Filtering Sequences

Use the `filter.py` script to filter sequences in a FASTA file based on your criteria:

```bash
python filter.py -i input.fasta -l 100 -m
```
* i : Specify the input FASTA file.
* l : Set the minimum sequence length (e.g., 100 base pairs).
* m : Include this flag to filter sequences starting with methionine (M).

### 3. Automated Filtering

To filter sequences for all organisms listed in allorgs.txt, use the filterall.sh script:

bash
```
bash filterall.sh
```

## Outputs
The results directory contains key outputs from a comparative genomics analysis, including information on gene duplication events (Gene_Duplication_Events), phylogenetic trees of individual genes (Gene_Trees), and orthologous groups (Orthogroups). It also identifies genes that are phylogenetically misplaced (Phylogenetically_Misplaced_Genes) and provides sequences of single-copy orthologues, crucial for species tree reconstruction (Single_Copy_Orthologue_Sequences). A compressed version of the gene duplication data is also included (Gene_Duplication_Events.zip) for easier storage and sharing. These outputs collectively offer insights into gene evolution and relationships across species.



