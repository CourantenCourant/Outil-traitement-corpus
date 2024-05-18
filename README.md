# Introduction

## General guide
- Here's the general guide of the workflow:
	- Use 
	- Use get_urls.py to get urls of a certain subclass pages on Encyclopédie universalis. The script produces a txt file that contains one url per line. 
		- How to run: python get_urls.py **target_url** **output_file.txt** **-l number_of_urls**
		- Example: python get_urls.py 'https://www.universalis.fr/classification/economie-et-gestion/entreprise/' ../../data/raw/urls.txt -l 100
		- This will give you a txt file of 100+ urls.
	- Use create_dataset.py to produce a parquet file from the urls.txt generated.
		- How to run: python create_dataset.py **url_file.txt** **output_file.parquet**
		- Example: python create_dataset.py ../../data/raw/urls.txt ../../data/raw/dataset.parquet
		
## Detailed guide
- 