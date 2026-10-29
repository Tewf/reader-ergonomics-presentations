# Présentations

Comment construire une présentation pour que l'auditoire, ou le lecteur d'un diaporama, la suive et la retienne au
moindre coût.

Ce dépôt étend [reader-ergonomics](https://github.com/Tewf/reader-ergonomics), le standard pour tout lecteur. Les
principes que celui-ci contient sont liés, jamais recopiés. Ce dépôt n'ajoute que ce qu'un exposé change : l'auditeur
ne règle pas le rythme et ne peut pas relire.

> **État :** en cours. Le [standard](standard.md) compte neuf principes, trois contextes et la forme d'un exposé,
> avec un diaporama d'exemple et sept vérifications qui s'exécutent sur les diaporamas. Il a été testé sur deux vrais
> exposés, l'un académique, l'autre d'affaires, qui ont changé les vérifications ; un test informel est en cours. C'est
> une lecture informelle de la recherche et de la pratique publiées : pas un standard officiel, pas une étude relue
> par des pairs, pas un résultat nouveau.
>
> **Comment il est fait :** avec Claude, un assistant IA d'Anthropic, sous la direction du mainteneur, comme
> reader-ergonomics. Des agents rédigent les revues de littérature ; chaque référence est résolue par programme, et un
> chiffre lu seulement dans un résumé est marqué « (secondary) ». Les corrections sont bienvenues en issues.

## Portée

Une base, et des contextes qui la modifient, comme un style de lecteur modifie le standard. La manière de présenter
de chacun est un style à part, gardé par lui, qui modifie à son tour ce standard.

```text
présentations
 ├─ la base : ce qu'est une présentation
 │    un média rythmé, un orateur, une salle
 └─ les contextes qui la modifient
    ├─ l'exposé académique
    │    colloque, séminaire, soutenance
    ├─ la présentation d'affaires
    │    pitch, vente, point de direction
    └─ l'exposé informel
         meetup, club, entre amis
```

## Contenu

| Partie | Contient | État |
|---|---|---|
| [standard.md](standard.md) | la fiche : comment utiliser le standard, et chaque principe avec son niveau de preuve | écrit |
| [principles/](principles/) | neuf principes en trois groupes : rythme, diapositive, exposé | écrit ; pas encore testé sur un vrai exposé |
| [reader-styles/](reader-styles/) | les contextes, écrits comme des auditoires : académique, affaires, informel | écrit |
| [shapes/](shapes/) | la forme d'un exposé, et un diaporama HTML d'exemple qui la suit | écrit |
| [checks/](checks/) | sept vérifications qui s'exécutent sur les diaporamas HTML, avec leurs tests | écrit |
| [decisions/](decisions/) | les choix qui ont façonné ce dépôt, un enregistrement chacun | six enregistrements |
| [evidence/](evidence/) | une revue multivocale en neuf questions ; 172 travaux | écrite, auditée |

La version anglaise, [README.md](README.md), fait foi.

## Licence

Code sous [Apache License 2.0](LICENSE) ; texte sous [CC BY 4.0](LICENSES/CC-BY-4.0.txt).
