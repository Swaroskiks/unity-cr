# Flat

## Pages individuelles

| | |
|---|---|
| **Binôme 1** | Ibraguim TEMIRKHAEV |
| **Binôme 2** | Mouad MOUSTARZAK |
| **Classe - groupe** | E3FI - Groupe 3L |
| **Année** | 2024-2025 |
| **École** | ESIEE Paris |
| **Dépôt Github** | https://github.com/ckizp/Flat |

## Présentation Générale du Projet

Flat est un jeu d'atmosphère psychologique en 3D à la première personne, conçu dans Unity, qui plonge le joueur dans une expérience d'horreur psychologique intime. Le jeu se déroule dans un appartement ordinaire, où l'ambiance bascule progressivement vers l'étrange et le dérangeant.

## Partie Technique

Au cours du développement, nous avons tenté de suivre les conventions de structure et de nommage définies par [Justin Wasilenko](https://github.com/justinwasilenko/Unity-Style-Guide). Cela nous a permis de bien séparer les systèmes et de maintenir une structure claire tout au long du projet.

Les systèmes d'interaction, d'inventaire et d'objectifs ont été implémentés de manière modulaire l'un à la suite de l'autre.

### Système d'interaction

Le système d'interaction repose sur un composant **Interactor** attaché au joueur, qui émet régulièrement un raycast vers l'avant pour détecter des objets implémentant l'interface IInteractable. Lorsqu'un objet est détecté, Interactor le garde en mémoire comme "focus" et gère les interactions selon son type (Instant ou Hold). Si le joueur appuie sur la touche d'interaction, la méthode Interact() est appelée (immédiatement pour Instant, après un temps maintenu pour Hold). Les objets interactifs héritent de BaseInteractable, qui centralise les données (prompt, durée, ID) et peut émettre un événement global (AnyInteraction).

### Système d'inventaire

Le système d'inventaire repose sur deux composants : **PlayerInventory**, qui stocke les objets (Item) dans 4 slots, et **PlayerInventoryController**, qui gère les entrées du joueur (utilisation, drop, navigation). Lorsqu'un objet interactif de type ItemPickup est ramassé (via le système d'interaction), il est ajouté à PlayerInventory via AddItem(), qui déclenche l'événement ItemAdded. Le joueur peut faire défiler les slots (scroll ou touches 1–4) et utiliser l'objet sélectionné (touche F) ou le jeter (touche G).

### Système d'objectifs

Le système d'objectifs est piloté par le **ObjectiveManager** qui permet de charger les objectifs, lancer un objectif, changer l'état, etc. Chaque objectif est défini par un ObjectiveInfoSO (ScriptableObject contenant un ID, un nom, et une séquence de prefab d'étapes), et chargé dynamiquement grâce au système Addressables. Lorsqu'un objectif est lancé (StartObjective), sa première étape est instanciée dans la scène via InstantiateCurrentObjectiveStep(). Chaque étape hérite d'ObjectiveStep, une classe abstraite qui encapsule la logique de progression.

Par exemple, les sous-classes comme InteractionObjectiveStep ou ItemObjectiveStep réagissent à des événements globaux (AnyInteraction, ItemAdded) pour valider l'étape.

Une fois validée, l'étape appelle FinishObjectiveStep(), qui notifie le système (AdvanceObjective) pour charger l'étape suivante ou marquer l'objectif comme terminé. Toute la communication repose sur le bus d'événements central ObjectiveEvents.

#### Exemple : Objectif "When Light Fades"

On a par exemple le premier objectif du jeu "When Light Fades", dont l'identifiant est Objective_RestoreLights. Il est composé de quatre étapes :

1. **FindBreakerStep** : Essayer d'ouvrir la porte d'entrée (utilise InteractionObjectiveStep écoutant try_open_entrance_door)
2. **FindKeyStep** : Récupérer la clé (utilise ItemObjectiveStep attendant l'item "Key")
3. Et ainsi de suite...

### Gestion des entrées

L'**InputManager** sert de point central pour toutes les entrées du joueur. Il utilise le nouveau système d'Input d'Unity pour récupérer les actions définies dans le projet (déplacements, mouvement caméra, interaction, etc.), puis met à jour des propriétés que les autres scripts peuvent consulter facilement (Move, Look, Run, Interact, etc.).

L'idée, c'est de **découpler totalement la logique d'entrée** du reste du code : les autres systèmes n'ont pas à savoir comment les touches sont configurées, ils lisent simplement ce que fait le joueur.

| Action | Touche |
|---|---|
| Déplacement | Z/Q/S/D |
| Caméra | Curseur souris |
| Courir | Shift |
| S'accroupir | C |
| Interagir | E |
| Utiliser | F |
| Jeter | G |
| Sélectionner un slot | 1/2/3/4 |
| Switch de slot | Molette souris |

### Mouvements du joueur

Le système de mouvement du joueur repose sur le contrôleur d'animation AC_PlayerController, basé sur un Blend Tree 2D qui gère les transitions entre la marche et la course en fonction de la direction et de la vitesse du personnage. La majorité des animations proviennent de la bibliothèque [Mixamo](https://www.mixamo.com/). Pour celles qui manquaient (comme la marche arrière en étant accroupi) nous sommes passés par Blender pour inverser et adapter une animation existante.

## Partie Artistique

Lorsque nous avons fini de développer l'idée, nous avons pensé tout d'abord au plan de l'appartement. Nos points de direction étaient l'appartement du personnage (en rouge), celui du voisin (en violet) ainsi que de longs couloirs (en vert clair), typique des Backrooms, un concept popularisé par la culture internet et les "creepypastas". Autour de cette base, nous avons ajouté deux autres appartements (en jaune), des toilettes de palier (en rose) et un débarras commun (en vert foncé) pour ne pas fermer la porte au développement futur du projet.

### Éclairage et ambiance

Pour poser l'ambiance et donner une première lecture de cet espace, on a beaucoup réfléchi à l'éclairage. Le contraste entre la lumière du couloir et celle de l'appartement n'est pas là par hasard : on voulait que l'extérieur paraisse froid, presque clinique, comme un espace transitoire sans vie propre. À l'inverse, l'intérieur de l'appartement est plus lumineux, mais cette lumière révèle un désordre inquiétant, presque dérangeant. L'idée, c'était de créer un malaise subtil dès les premiers instants, en montrant que même un lieu familier comme son propre chez-soi peut rapidement devenir instable, voire menaçant.

### Symbolisme narratif

Sur le plan narratif, l'étage représente la conscience troublée du personnage, tandis que l'appartement du voisin symbolise le traumatisme qu'il refuse d'affronter. On retrouve ainsi plusieurs indices subtils dans son appartement :

- Des **tableaux** représentant sa famille, avec son propre visage effacé
- Un **fauteuil** entouré de bouteilles d'alcool
- Une **horloge** dont le son régulier et oppressant perturbe le silence

### Post-processing

Tous les effets de post-processing reposent sur un seul profil appliqué à l'ensemble du niveau. Les réglages sont précis :

- **Bloom marqué** avec texture de saleté sur l'objectif
- **Exposition réduite** et contraste accentué
- **Grain filmique** pour une perception déformée
- **Occlusion ambiante** modérée
- **Vignettage discret** pour focaliser l'attention

Ce traitement visuel est directement inspiré de l'**expressionnisme allemand**, courant artistique où les décors, les ombres et les jeux de lumière ne cherchent pas à reproduire fidèlement la réalité, mais plutôt à exprimer des émotions brutes et des états psychologiques troublés.

### Ambiance sonore

L'ambiance sonore a été une composante essentielle pour appuyer l'atmosphère du jeu :

- **Son de fond** constant et aigu pour installer une tension
- **Bruits ponctuels** : horloge, réfrigérateur
- **Voix féminine** (générée via Elevenlabs) criant "Pourquoi tu m'as fait ça ?" lors de l'objectif "When Light Fades"
- **Sons de pas** réalistes sur différentes surfaces

### Interface utilisateur

Nous avons opté pour un design très épuré, inspiré du jeu *Dying Light*. L'objectif était de proposer quelque chose de simple, lisible, et non intrusif. Typographie utilisée : [Museo](https://fonts.adobe.com/fonts/museo). Code couleur limité avec l'orange pour mettre en valeur les informations importantes.

## Démo

[Vidéo de démonstration](https://www.youtube.com/watch?v=dmeN4AAUujA)

## Références

1. [Tutorial 1](https://www.youtube.com/watch?v=UyTJLDGcT64)
2. [Tutorial 2](https://www.youtube.com/watch?v=xbtSM7B_htU)
3. [Playlist Unity](https://www.youtube.com/watch?v=-xB4xEmGtCY&list=PLg7sMWZoap4B8N1pR8nl2-eG_D5k9MfWY&index=1)
4. [Tutorial 4](https://www.youtube.com/watch?v=OiZXAsn5BWo)
 voici les informations sur le jeu flat si jamais t'en a pas assez