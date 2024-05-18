# Outil-traitement-corpus

- Tâche : Fill mask
- Corpus : Le plus connu est peut-être wikipedia : https://huggingface.co/datasets/wikipedia . Sinon j'ai trouvé un corpus en chinois qui est très relou : https://huggingface.co/datasets/liwu/MNBVC .
- À quel type de prédiction : classification
- À quel modèle il a servi : google bert, distilbert, CasualLM
- Observations sur ce corpus : Sur la page du corpus il y a une présentation sympa. Le corpus est constitué des dump-texts des pages de wikipédia dans toutes les langues imaginables. Il y a des milliers de modèles qui sont entraînés sur ce corpus. Il est écrit que ce dataset est souvent utilisé pour "Language modeling" même si je ne connais pas sa définition exacte. Mais c'est aussi écrit que c'est pour text generation et fill-mask.

# Detailed guide
- The guide is organized by TP. Each section explains how to use the scripts to anwser the specific TP's demand.
- Not every demand of every TP is systemacially satisfied as some of them get repeated in the following or previous TPs.
- (Not every demand of every TP is systemacially satisfied as I failed to do some...)
- I think all my code, at least those in the .py files, follow PEP8, as PyCharm validates my scripts.

## TP 1
- We chosse to scrap on [Encyclopaedie Universalis](https://www.universalis.fr/) to create a datset similar to [wikipedia dataset](https://huggingface.co/datasets/wikipedia).
- All files in script/process/test/, or prefixed with "test_", are testing files, or building blocks to construct the official scripts.

## TP 2
### Demands
- Initialiser les dossiers de votre repo.
- Mettez en place un script python pour récupérer automatiquement des données depuis le web (quelques éléments suffiront).
- On veut obtenir les même colonnes que votre corpus de référence.

### What we did
- Initialize repository following MIT standard.
- We use get_urls.py and create_dataset.py to web scrap.
- See test_create_dataset.ipynb for the third point.

### Explanation
- We choose Encyclopédie Universalis (EU from here) to create our dataset.
- On EU, there is a [classification page](https://www.universalis.fr/classification/).
- There are three types classification page: [pages with classes](https://www.universalis.fr/classification/arts/cinema/), , [pages with articles](https://www.universalis.fr/classification/arts/cinema/acteurs-et-actrices-cinema/acteurs-et-actrices-du-cinema-muet/), and [pages with classes and articles](https://www.universalis.fr/classification/arts/cinema/acteurs-et-actrices-cinema/).
- get_urls.py allows to do the following:
  - On pages with classes: get all the articles' url contained in the subclasses.
  - On pages with articles: get all the articles' url.
  - On pages with classes and articles: get all the articles' url of the current page, and those of the subclasses.
- Use 'python get_urls.py -h' to see how to launch the script.
- Note that the '-l', or the url's limit number, is not meant to be precise. Suppose that we have '-l 100' and the script already had 96 urls, if the next class to scrap have 20 urls, it will return 116 urls.
- We then use create_dataset.py to visit these url and to get the introduction section of each article.
  - More explanation of create_dataset.py in the following sections.

## TP3

### Demands:
- Ouvrir son corpus avec pandas
- Convertir son corpus au format Dataset

### What we did
- We choose not to use pandas as our dataset is already in .parquet format.
- We use create_dataset.py to create a dataset.

### Explanation
- After scrapping from EU, create_dataset.py creates a Dataset object with the following structure:
  - {'idx': int, 'url': str, 'title': str, 'intro': str}
- It then stores it to a parquet file.

## TP4

### Demands
- Trouvez les statistiques qui ont été effectuées pour prouver la qualité du corpus
- Les implémenter et les calculer pour votre corpus

### What we did
- We use stat_visualization.ipynb to calculate statictics and visualize data.

### Explanation
- stat_visualization.ipynb shows the length distribution of our corpus and compare it to the normal distribution.
- It shows the 20 most frequent words (without punctuation) and compare it to the ziph's law.

## TP5

### Demands
- Splitter son corpus en test et train

### What we did
- create_dataset.py allows to split dataset into train, dev and test.

### Explanation
- Use 'python create_dataset.py -h' to see how to split dataset.

## TP6

### Demands
- Split son corpus en train, dev, test
- Faire la carte de son Dataset
- Optionnel : si vous pensez que votre corpus est intéressant → Le publier sur huggingFace

### What we did
- For splits, see TP5.
- I'm still studying HuggingFace to see how to create dataset card and publish dataset...
- But I will consider running my scripts on [all classes](https://www.universalis.fr/classification/) to obtain the complete dataset, and publish it on HuggingFace.
- I have to work out a bunch of legal and licence issues which is really a pain in the ass...




