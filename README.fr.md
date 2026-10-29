# Présentations

Comment construire une présentation pour que l'auditoire, ou le lecteur d'un diaporama, la suive et la retienne au
moindre coût.

Ce dépôt étend [reader-ergonomics](https://github.com/Tewf/reader-ergonomics), le standard pour tout lecteur. Les
principes que celui-ci contient sont liés, jamais recopiés. Ce dépôt n'ajoute que ce qu'un exposé change : l'auditeur
ne règle pas le rythme et ne peut pas relire.

> **État :** en cours. Le [standard](standard.md) compte neuf principes, trois contextes et la forme d'un exposé,
> avec un diaporama d'exemple et sept vérifications qui s'exécutent sur les diaporamas. Il a été testé sur trois vrais
> exposés, académique, d'affaires et informel, qui ont changé les vérifications. C'est
> une lecture informelle de la recherche et de la pratique publiées : pas un standard officiel, pas une étude relue
> par des pairs, pas un résultat nouveau.
>
> **Comment il est fait :** avec Claude, un assistant IA d'Anthropic, sous la direction du mainteneur, comme
> reader-ergonomics. Des agents rédigent les revues de littérature ; chaque référence est résolue par programme, et un
> chiffre lu seulement dans un résumé est marqué « (secondary) ». Les corrections sont bienvenues en issues.

## Portée

Une base, et des contextes qui la modifient, comme un style de lecteur modifie le standard. La manière de présenter
de chacun est un style à part, gardé par lui, qui modifie à son tour ce standard.

![Ce standard contient une base, ce qu'est toute présentation, et trois contextes qui la modifient : l'exposé académique, la présentation d'affaires et l'exposé informel ; le style propre à chacun modifie à son tour tout le standard.](readme-scope.fr.svg)

## Contenu

| Partie | Contient | État |
|---|---|---|
| [standard.md](standard.md) | la fiche : comment utiliser le standard, et chaque principe avec son niveau de preuve | écrit |
| [principles/](principles/) | neuf principes en trois groupes : rythme, diapositive, exposé | écrit ; pas encore testé sur un vrai exposé |
| [reader-styles/](reader-styles/) | les contextes, écrits comme des auditoires : académique, affaires, informel | écrit |
| [shapes/](shapes/) | la forme d'un exposé, et un diaporama HTML d'exemple qui la suit | écrit |
| [checks/](checks/) | sept vérifications qui s'exécutent sur les diaporamas HTML, avec leurs tests | écrit |
| [decisions/](decisions/) | les choix qui ont façonné ce dépôt, un enregistrement chacun | sept enregistrements |
| [evidence/](evidence/) | deux revues multivocales : les présentations, en dix questions, et les figures, comment dessiner une figure ou un diagramme (question 11) ; 258 travaux | écrites, auditées |

La version anglaise, [README.md](README.md), fait foi.

## Licence

Code sous [Apache License 2.0](LICENSE) ; texte sous [CC BY 4.0](LICENSES/CC-BY-4.0.txt).
