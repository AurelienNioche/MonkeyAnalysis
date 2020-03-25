# TO DO

### Figures 
* Display stats on figures [DONE]
* Freq against EV: put losses and gains on the same figure [DONE]

### Output table

* bias L/R [DONE]
* Each median control per type [DONE]
* Each best-fit parameter value [DONE]
* Total number of trials [DONE]
* documentation [DONE]
    
### Supplementary analysis
* for control: sigmoid EV / p choice [DONE]
* Reaction time / EV
    
### Data structure
* Choose between n_chunk and n_trial_per_chunk
 
### Define hypothesis

* Rank <=> risk
* understanding prob <=> rank
* Food access due to rank => risk

## Target
* Animal Cognition
* Animal Behavior

## Sebastien's remarks
- Est ce que tu pourrais afficher les trois figures en ligne plutôt qu'en colonne ?
- Peut-être que définir l'espace par V(left)-V(right) serait plus judicieux et que les résultats ressemblerai plus a des sigmoides ? En effet ici il y a une 'bonne' réponse et donc l'espace entre 0 et .5 sur l'axe des ordonnés n'est pas vraiment utilisable pour le fit...
- Il faudrait sur ces courbes définir la pente et le point d'inflexion (si on conserve cette version on pourrait considérer la valeur à .75 en ordonné pour ne pas avoir de valeurs aberrantes pour Alaryc par exemple). Une fois que tu l'auras fait, tu pourras les rajouter au tableau de summary

qq pistes de réflexions:
- Le point d'inflexion de la première figure nous permettra de définir une différence de valeur pour laquelle le singe commence à "décider"

En y repensant, la 2nd figures est une sorte de reproduction de la 1er dans un intervalle de valeurs plus restreint (de 0 à 2.5 environ):
- A l'inverse de la 1er figure, dans la 2nd les probabilités sont différentes de 1. Donc si le singe comprend bien le concept proba, les fits de la 2nd et de la 1er figure devrait être similaire. Tu confirmes ? quid de la 3éme figure ?
- En plus de cela, il y a aussi la dimension gains vs pertes à considérer. Peut-être qu'il serait pertinent de calculer l'aire sous les courbes entre les décisions en condition de gains et les pertes pour la 2nd et 3eme figures ?