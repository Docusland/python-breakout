# Contexte

Ce projet a été réalisé en suivant un tutoriel présent ici : 
 - https://www.101computing.net/breakout-tutorial-using-pygame-getting-started/

# Objectif premier
Faites en sorte que ce projet compile et puisse être executé à partir de votre IDE.
Pour celà, vous pouvez cloner ce dépôt ou le télécharger en utilisant le lien <div class="btn-primary btn"> Code </div> ci-dessus.
Dézippez le contenu au sein du dossier de votre choix. Puis ouvrez le dossier avec votre IDE.  Pycharm par exemple.

Executez le fichier main.py (Souvent click droit sur le fichier, Run main.py)
Si toutes les bibliothèques de dépendance sont disponible dans l'environnement virtuel, vous devriez réussir à lancer le jeu. Le cas échéant vérifiez votre interpreteur python et les requirements.

# Lecture du code
Avant tout chose, partons à la découverte du code existant. 
Lisez les commentaires et essayez de comprendre le code présent.

# Exercices
## Exercice 1
Vous avez uniquement 3 vies et ce jeu est assez difficile. 
Faites en sorte d'avoir 5 vies.

## Exercice 2
Au sein de la classe Game, du code semble être dupliqué au sein de la méthode
 `__generate_bricks`.
 Faites en sorte pour qu'il n'y ait qu'une seule boucle au sein de cette
  méthode

## Exercice 3
En suivant le tutoriel, de nombreuses valeurs étaient écrites en "dur" au sein du code. Faites du **refactoring** en les généralisant par le biais de constantes dans le fichiers `constants.py`.

Attentions aux nommages et à la pertinence de définir ces constantes.

## Exercice 4

En jouant un peu, on peut se rendre compte qu'il y a quelques problèmes au
 sein de l'application. 
 
 En effet, parfois la balle rebondit étrangement et reste horizontale.
 Trouvez commment corriger cette anomalie. 
 
## Exercice 5

Nous allons rajouter une nouvelle fonctionnalité.
Les blocks jaunes , lorsqu'ils sont détruits, changent le paddle et l
'agrandissent.