# python-project

Projet final en Python for Data Analyst

## Dataset

Le dataset : <https://archive.ics.uci.edu/ml/datasets/Seoul+Bike+Sharing+Demand>

Avec l'introduction des vélos à loué en ville qui ont permis l'amélioration de la mobilité, on cherche à savoir/prédire le nombre de vélo qui doivent être disponible à toute heure de la journée.

Le dataset contient ces informations :

| Donnée                | Type                                                |
| --------------------- | --------------------------------------------------- |
| Date                  | year-month-day                                      |
| Rented Bike count     | Count of bikes rented at each hour                  |
| Hour                  | Hour                                                |
| Temperature           | Celsius                                             |
| Humidity              | %                                                   |
| Windspeed             | m/s                                                 |
| Visibility            | 10m                                                 |
| Dew point temperature | Celsius                                             |
| Solar radiation       | MJ/m2                                               |
| Rainfall              | mm                                                  |
| Snowfall              | cm                                                  |
| Seasons               | Winter, Spring, Summer, Autumn                      |
| Holiday               | Holiday/No holiday                                  |
| Functional Day        | NoFunc(Non Functional Hours), Fun(Functional hours) |

Le fichier csv original n'est pas en encoding utf-8, j'ai donc du d'abord changer l'encoding du fichier en utf-8 pour ensuite pouvoir l'utiliser.

Les changements sur les données qualitatif en quantitatif pour le machine learning sont :

| Donnée         | Type                                           |
| -------------- | ---------------------------------------------- |
| Seasons        | Winter = 1, Spring = 2, Summer = 3, Autumn = 4 |
| Holiday        | No Holiday = 0, Holiday = 1                    |
| Functional Day | No = 0, Yes = 1                                |

La valeur dont nous avons besoin de prédire est "Rented Bike count", le nombre de vélos loués à Séoul à chaque heure de la journée.

L'objectif est d'avoir :

1- un PowerPoint au format PDF contenant la démarche et les résultats de notre analyse et de nos modèles.

2- Deux fichier Jupyter Python contenant le code de data visualisation et de modeling

3- Une API Django

## Data Visualisation

Le dataset ne contient pas de data nulle. Cela facilite le traitement.
Toutefois, la variable Functioning day implique que la station est fermé et que, du coup, le nombre de location de velo est nul. Nous allons donc supprimer toutes les lignes correspondante afin d'améliorer notre dataset.

![rented bike](images/1.png)

On applique une fonction sqrt() sur le nombre de velo afin d'obrenir une pseudo gaussienne

![rented bike](images/2.png)

![rented bike](images/3.png)

![rented bike](images/4.png)

Nous pouvons voir que le nombre de vélo loué varie énormément en fonction du mois / saison de l'année. Examinons cela plus en détail.

![rented bike](images/5.png)

Nous pouvons voir qu'il y a une différence importante de distribution de location des velos en fonction de l'heure et si nous sommes en semaine ou week-end. Nous allons donc créer une variable working_day pour cela.

![rented bike](images/6.png)

Nous voyons bien la différence en fonction du mois. Nous allons créer une variable numérique mois (de 1 a 12).

![rented bike](images/7.png)

Il y a une petite difference en fonction de si l'on est en vacances ou non. Nous allons donc passer Holiday en variable quantitative.

![rented bike](images/8.png)

De même, la saison a un effet important et allons créer une variable quantitative dessus à la place du nom en dur.

![rented bike](images/9.png)

La matrice de correlation nous donne comme information la confirmation de l'importance de certaines variables.

Le fichier jupyter avec plus de détail est [datavis.ipynb](https://github.com/Raiyol/python-project/blob/main/datavis.ipynb).

## Modélisation

Nous avons tester 6 algorithmes pour voir quelles étaient le plus performant sur notre dataset. De plus nous avons comparé 2 jeux de données d'entrée différents. Les deux jeux de données ont les lignes avec Functioning day = 0 supprimé et la colonne supprimé.

Les jeux de données :

- L'original, avec la colonne date en moins
- Les variables qui sont ressorties et crées lors de la partie Data-visualisation

Les algorithmes :

- Logistic Regression​
- Linear Regression​
- SVR​
- SVC​
- K Nearest Neighbour​
- Random Forest Classifier

Le graphique des scores que nous obtenons :

- bleu : Dataset Orignal
- orange : Dataset Modifié

![modele](./images/modele.png)

Deux algorithmes ressortent du lots et sont _Linear Regression_ et _SVR_. On remarque aussi que les scores sont légèrement plus élevé avec le Dataset modifié.

Nous allons donc utilisé le Scaler et le modèle SVR du dataset modifié pour faire l'API Django.

Le fichier jupyter avec plus de détail est [ml.ipynb](https://github.com/Raiyol/python-project/blob/main/ml.ipynb)

## Django API

Pour lancer l'API, déplacez vous d'abord dans le répertoire :

```text
cd api_django
```

Et pour lancer le serveur :

```text
python manage.py runserver
```

Le serveur s'est normalement lancé sur <http://localhost:8000>

Vous pouvez maintenant tester les routes avec des applications tels que Postman, Insomnia ou curl.

Les routes :

| Méthode | Route     | Détail                                                          |
| ------- | --------- | --------------------------------------------------------------- |
| GET     | /bikes    | Liste de toutes les données                                     |
| POST    | /bikes    | Ajouté une ligne de donnée                                      |
| GET     | /bike/x/  | x un numéro, pour une ligne de donnée précise                   |
| DELETE  | /bike/x/  | x un numéro, supprimé la ligne avec ce numéro​                  |
| POST    | /predict/ | Prédire le nombre de vélo avec le modèle que nous avions fait.​ |

Un exemple du corps des requête POST, laisser RBC tel quel si c'est pour une prédiction :

```json
{
  "Hour": 2,
  "Temperature": 24,
  "Humidity": 40,
  "WS": 1,
  "Visibility": 1500,
  "SR": 0,
  "Rainfall": 0,
  "Snowfall": 0,
  "Holiday": 0,
  "Seasons": 3,
  "WD": 1,
  "Month": 9,
  "RBC": -1
}
```

- WS : Windspeed
- SR : Solar Radiation
- WD : Jour ouvré (jour de semaine ou pas) = 1, 0 sinon
- RBC : Rented Bike Count (Nombre de vélo loué)

La route /predict/ renvoie le corps json envoyé mais avec RBC modifié. RBC aura la valeur prédite par le modèle que nous avions choisi en fonction du reste des données entrées. Ce json sera aussi sauvegarder dans la Base de données et visible sur la route /bikes
