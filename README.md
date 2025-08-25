![GitHub contributors](https://img.shields.io/github/contributors/raphaelmakaryan/python_cnita?color=0d0&style=for-the-badge)
![GitHub release](https://img.shields.io/github/v/release/raphaelmakaryan/python_cnita?style=for-the-badge)
![GitHub watchers](https://img.shields.io/github/watchers/raphaelmakaryan/python_cnita?style=for-the-badge)
![GitHub Repo stars](https://img.shields.io/github/stars/raphaelmakaryan/python_cnita?color=%23fa0&style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/raphaelmakaryan/python_cnita?style=for-the-badge)

<br />
<div align="center">
  <img src="./github/logo.png" alt="Logo" height="250" >

<h3 align="center">python_cnita</h3>
  <p align="center">
   Initiation au Python !
  </p>
</div>


# À propos du projet
Ce repo(sitory) est créé dans le but du cours de Python au Campus Numérique in The Alps.

Ci-dessous se trouveront les informations importantes des dossiers/fichiers.

<br>

# bottle_venv
Le dossier `bottle_venv` contient les fichiers necessaires de l'exercice demandé afin de "host" un site internet en python grace au framework Bottle. 

<br>

# llm
Le dossier `llm` contient, comme son nom l'indique, un LLM en local, exercice bonus donnée par le formateur. 

Lien du site de l'exercice : https://machinelearningmastery.com/your-first-local-llm-api-project-in-python-step-by-step/?ref=dailydev


<br>

# tests
Le dossier `tests` contient, comme son nom l'indique, des essais, des tests pour comprendre et utiliser Python.
<br>

# 1.1
Le fichier `1.1.py` contient le code de l'exercice demandé de "créer un programme qui demande à l'utilisateur de saisir son nom et qui affiche Hello suivi du nom de l'utilisateur".

# 1.2
Le fichier `1.2.py` contient le code de l'exercice demandé de "découvrir l'écriture des tests automatiques avec Pytest et ensuite, mettre en valeur la pratique, en réalisant des exercices comme le FizzBuzz, LeapYears et Diamond".

# 1.3
Le fichier `1.3.py` contient le code de l'exercice demandé "pour expérimenter les dataclasses, créer une structure de type répertoire téléphonique".

# 1.4
L'exercice `1.4` est le dossier `bottle_venv`.

## Recommendation
Pour lancer les différents fichiers Python, il faudra télécharger quelques dépendances avec ces commandes (si vous êtes sur Linux) :
- `sudo apt install python3-venv`
- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `pip install requests`
- `pip install -U pytest`
- `sudo apt-get install python3-pytest`

<br>

Pour lancer Bottle, il faudra suivre le site ici pour l'installation (on ne sait jamais) :
https://bottlepy.org/docs/dev/tutorial.html#installation

Après ça, il faudra lancer les commandes : 

`cd bottle_venv`
`python my_version.py`