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

La valeur dont nous avons besoin de prédire est "Rented Bike count".

Le fichier csv original n'est pas en encoding utf-8, j'ai donc du d'abord changer l'encoding du fichier en utf-8 pour ensuite pouvoir l'utiliser.

Les changements sur les données qualitatif en quantitatif pour le machine learning sont :

| Donnée         | Type                                           |
| -------------- | ---------------------------------------------- |
| Seasons        | Winter = 1, Spring = 2, Summer = 3, Autumn = 4 |
| Holiday        | No Holiday = 0, Holiday = 1                    |
| Functional Day | No = 0, Yes = 1                                |
