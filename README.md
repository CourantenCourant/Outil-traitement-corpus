# Introduction

## General guide

- Use environment.yml to set up your conda environment.
- Use get_urls.py to get urls of a certain subclass page on Encyclopédie universalis. The script produces a txt file that contains one url per line. 
	- How to run on terminal: ```bash python get_urls.py target_url output_file.txt -l number_of_urls```
   	- Example: python get_urls.py 'https://www.universalis.fr/classification/economie-et-gestion/entreprise/' ../../data/raw/urls.txt -l 100
	- This will give you a txt file of 100+ urls.
 	- We prepared a data/raw/urls.txt.
- Use create_dataset.py to produce a parquet file from the urls.txt generated.
	- How to run: python create_dataset.py **url_file.txt** **output_file**
	- Example: python create_dataset.py ../../data/raw/urls.txt ../../data/raw/dataset
	- This will give you a .parquet file.
   	- We didn't prepare any parquet file for copyright reasons.
- Use stat_visualization.ipynb to visualize statistic data of the created dataset.
		
## Detailed guide
- For a more detailed guide, and to understand how this repository answers the course's requirements, see [here](https://github.com/CourantenCourant/Outil-traitement-corpus/blob/doc/rapport.md).
  
