# Introduction

## General guide

- Use `conda env create -f requirements.yml` to set up your conda environment. This will give you a conda environment called 'outil_corpus'.
- All scripts are in `scripts/process/`.
- Use `get_urls.py` to get urls of a certain class' pages on Encyclopédie universalis. The script produces a txt file that contains one url per line. 
	- Run on terminal: `python get_urls.py -h` to see usage of the script.
   	- Example: ```python get_urls.py 'https://www.universalis.fr/classification/economie-et-gestion/entreprise/' ../../data/raw/urls.txt -l 100```
	- This will give you a `urls.txt` of 100+ urls.
 	- We prepared a `urls.txt` in `data/raw/`.
- Use `create_dataset.py` to produce a parquet file from the `urls.txt` of the last step.
	- Run on terminal: `python create_dataset.py -h` to see usage the script.
	- Example: `python create_dataset.py ../../data/raw/urls.txt ../../data/raw/dataset`
	- This will give you a `dataset.parquet` in `data/raw/`.
   	- We didn't prepare any `dataset.parquet` for copyright reasons.
   	- There is an option of create train/dev/test datasets.
- Use `stat_visualization.ipynb` with jupyter notebook to visualize statistic data of the created dataset.
		
## Detailed guide
- For a more detailed guide, and to understand how this repository answers the course's requirements, see [here](https://github.com/CourantenCourant/Outil-traitement-corpus/blob/doc/rapport.md).
  
