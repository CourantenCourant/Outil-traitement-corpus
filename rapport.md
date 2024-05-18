# Outil-traitement-corpus

Tâche : Fill mask
Corpus : Le plus connu est peut-être wikipedia : https://huggingface.co/datasets/wikipedia . Sinon j'ai trouvé un corpus en chinois qui est très relou : https://huggingface.co/datasets/liwu/MNBVC .
À quel type de prédiction : classification
À quel modèle il a servi : google bert, distilbert, CasualLM
Observations sur ce corpus : Sur la page du corpus il y a une présentation sympa. Le corpus est constitué des dump-texts des pages de wikipédia dans toutes les langues imaginables. Il y a des milliers de modèles qui sont entraînés sur ce corpus. Il est écrit que ce dataset est souvent utilisé pour "Language modeling" même si je ne connais pas sa définition exacte. Mais c'est aussi écrit que c'est pour text generation et fill-mask.

# Detailed guide
- The guide is organized by TP. Each section explains how to use the scripts to anwser the specific TP's demand.
- Not every demand of every TP is satisfied as some of them get repeated in the following or previous TP.

## TP 1

## TP 2
### Demands:
- Initialiser les dossiers de votre repo.
- Mettez en place un script python pour récupérer automatiquement des données depuis le web (quelques éléments suffiront)

### What we did
- Initialized repository following MIT standard.
- We used get_urls.py and create_dataset.py to finish the task.

### Explanation
- We choose Encyclopédie Universalis (EU from here) to create our dataset.
- On EU, there is a [classification page](https://www.universalis.fr/classification/).

## TP3

#### How to construct your corpus?

