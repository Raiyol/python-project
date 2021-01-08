# python-project

Projet final en Python for Data Analyst

## Dataset

Mon dataset : <https://archive.ics.uci.edu/ml/datasets/Seoul+Bike+Sharing+Demand>

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

![viz1](./images/1.png)

![viz2](./images/2.png)

![viz3](./images/3.png)

![viz4](./images/4.png)

![viz5](./images/5.png)

![viz6](./images/6.png)

![viz7](./images/7.png)

![viz8](./images/8.png)

![viz9](./images/9.png)

## Modélisation

Nous avons tester 6 algorithmes pour voir quelles étaient le plus performant sur notre dataset. De plus nous avons comparé 2 jeux de données d'entrée différents. Les deux jeux de données ont les lignes avec Functionning day = 0 supprimé et la colonne supprimé.

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

Vous pouvez maintenant tester les routes avec des applications tels que Postman, Insomna ou curl.

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
