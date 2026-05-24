# Flat

<div style="padding: 15px; border-radius: 10px; background-color: #383836; text-align: center; width: 100%;">

<b>Welcome to our project</b>

</div>

## Contexte

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="border: 1px solid #2f2f2f; background-color: #202020; width: 25%; padding: 8px; color: white; text-align: left;">Informations</th>
    <th style="border: 1px solid #2f2f2f; background-color: transparent; width: 75%; padding: 8px; text-align: left;">Détails</th>
  </tr>
  <tr>
    <td style="border: 1px solid #2f2f2f; background-color: #202020; padding: 8px; color: white;">Binôme 1</td>
    <td style="border: 1px solid #2f2f2f; background-color: transparent; padding: 8px;">
      Ibraguim TEMIRKHAEV <a href="https://www.notion.so/ibratmkv-1ce63972f17b80ed87f7f9e5cfe46559?pvs=21">@ibratmkv</a>
    </td>
  </tr>
  <tr>
    <td style="border: 1px solid #2f2f2f; background-color: #202020; padding: 8px; color: white;">Binôme 2</td>
    <td style="border: 1px solid #2f2f2f; background-color: transparent; padding: 8px;">
      Mouad MOUSTARZAK <a href="https://www.notion.so/hiks1803-1ce63972f17b80be8e57c0221d8eaca3?pvs=21">@hiks1803</a>
    </td>
  </tr>
  <tr>
    <td style="border: 1px solid #2f2f2f; background-color: #202020; padding: 8px; color: white;">Classe - groupe</td>
    <td style="border: 1px solid #2f2f2f; background-color: transparent; padding: 8px;">E4FI - Groupe 3I</td>
  </tr>
  <tr>
    <td style="border: 1px solid #2f2f2f; background-color: #202020; padding: 8px; color: white;">Année</td>
    <td style="border: 1px solid #2f2f2f; background-color: transparent; padding: 8px;">2024-2026</td>
  </tr>
  <tr>
    <td style="border: 1px solid #2f2f2f; background-color: #202020; padding: 8px; color: white;">École</td>
    <td style="border: 1px solid #2f2f2f; background-color: transparent; padding: 8px;">ESIEE Paris</td>
  </tr>
  <tr>
    <td style="border: 1px solid #2f2f2f; background-color: #202020; padding: 8px; color: white;">Dépôt Github</td>
    <td style="border: 1px solid #2f2f2f; background-color: transparent; padding: 8px;">
      <a href="https://github.com/ckizp/Flat">Lien Github</a>
    </td>
  </tr>
</table>

## I. Présentation Générale du Projet

Flat est un jeu d’atmosphère psychologique en 3D à la première personne, conçu dans Unity, qui plonge le joueur dans une expérience d’horreur psychologique intime. Le jeu se déroule dans un appartement ordinaire, où l’ambiance bascule progressivement vers l’étrange et le dérangeant.

## II. Partie Technique

Au cours du développement, nous avons tenté de suivre les conventions de structure et de nommage définies par [Justin Wasilenko](https://github.com/justinwasilenko/Unity-Style-Guide). Cela nous a permis de bien séparer les systèmes et de maintenir une structure claire tout au long du projet.

<div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 20px; flex-wrap: wrap;">

  <figure style="margin: 0; width: 45%;">
    <img src="http://51.77.147.126/api/images/images/struct1.png" alt="Aperçu de la hiérarchie d’une scène" style="width: 100%; height: auto;">
    <figcaption style="color: #ada9a3; text-align: left;">Aperçu de la hiérarchie d’une scène</figcaption>
  </figure>

  <figure style="margin: 0; width: 45%;">
    <img src="http://51.77.147.126/api/images/images/struct2.png" alt="Aperçu de la structure du projet" style="width: 100%; height: auto;">
    <figcaption style="color: #ada9a3; text-align: left;">Aperçu de la structure du projet</figcaption>
  </figure>

</div>

Les systèmes d’interaction, d’inventaire et d’objectifs ont été implémentés de manière modulaire l’un à la suite de l’autre.

<figure style="margin: 0;">
<img src="http://51.77.147.126/api/images/images/systems.png" alt="Aperçu des principaux systèmes du projet" style="width: 100%; height: auto;">
<figcaption style="color: #ada9a3; text-align: left;">Aperçu des principaux systèmes du projet</figcaption>
</figure>

### Système d’interaction

Le système d’interaction repose sur un composant <span style="color: #d9d9a7;">Interactor</span> attaché au joueur, qui émet régulièrement un raycast vers l’avant pour détecter des objets implémentant l’interface <span style="color: #d9d9a7;">IInteractable</span>. Lorsqu’un objet est détecté, <span style="color: #d9d9a7;">Interactor</span> le garde en mémoire comme "focus" et gère les interactions selon son type (<span style="color: #d9d9a7;">Instant</span> ou <span style="color: #d9d9a7;">Hold</span>). Si le joueur appuie sur la touche d’interaction, la méthode <span style="color: #d9d9a7;">Interact()</span> est appelée (immédiatement pour <span style="color: #d9d9a7;">Instant</span>, après un temps maintenu pour <span style="color: #d9d9a7;">Hold</span>). Les objets interactifs héritent de <span style="color: #d9d9a7;">BaseInteractable</span>, qui centralise les données (prompt, durée, ID) et peut émettre un événement global (<span style="color: #d9d9a7;">AnyInteraction</span>).

<figure style="margin: 0;">
<img src="http://51.77.147.126/api/images/images/interaction_system.png" alt="Aperçu du système d’interaction" style="width: 100%; height: auto;">
<figcaption style="color: #ada9a3; text-align: left;">Aperçu du système d’interaction</figcaption>
</figure>

### Système d’inventaire

Le système d’inventaire repose sur deux composants : <span style="color: #d9d9a7;">PlayerInventory</span>, qui stocke les objets (Item) dans 4 slots, et <span style="color: #d9d9a7;">PlayerInventoryController</span>, qui gère les entrées du joueur (utilisation, drop, navigation). Lorsqu’un objet interactif de type <span style="color: #d9d9a7;">ItemPickup</span> est ramassé (via le système d’interaction), il est ajouté à <span style="color: #d9d9a7;">PlayerInventory</span> via <span style="color: #d9d9a7;">AddItem()</span>, qui déclenche l’événement <span style="color: #d9d9a7;">ItemAdded</span>. Le joueur peut faire défiler les slots (scroll ou touches 1–4) et utiliser l’objet sélectionné (touche F) ou le jeter (touche G).

<figure style="margin: 0;">
<img src="http://51.77.147.126/api/images/images/inventory_system.png" alt="Aperçu du système d’inventaire" style="width: 100%; height: auto;">
<figcaption style="color: #ada9a3; text-align: left;">Aperçu du système d’inventaire</figcaption>
</figure>

### Système d’objectifs

Le système d’objectifs est piloté par le <span style="color: #d9d9a7;">ObjectiveManager</span> qui permet de charger les objectifs, lancer un objectif, changer l’état, etc. Chaque objectif est défini par un <span style="color: #d9d9a7;">ObjectiveInfoSO</span> (ScriptableObject contenant un ID, un nom, et une séquence de prefab d'étapes), et chargé dynamiquement grâce au système <span style="color: #d9d9a7;">Addressables</span>. Lorsqu’un objectif est lancé (<span style="color: #d9d9a7;">StartObjective</span>), sa première étape est instanciée dans la scène via <span style="color: #d9d9a7;">InstantiateCurrentObjectiveStep()</span>. Chaque étape hérite d’<span style="color: #d9d9a7;">ObjectiveStep</span>, une classe abstraite qui encapsule la logique de progression.

Par exemple, les sous-classes comme <span style="color: #d9d9a7;">InteractionObjectiveStep</span> ou <span style="color: #d9d9a7;">ItemObjectiveStep</span> réagissent à des événements globaux (<span style="color: #d9d9a7;">AnyInteraction</span>, <span style="color: #d9d9a7;">ItemAdded</span>) pour valider l’étape.

Une fois validée, l’étape appelle <span style="color: #d9d9a7;">FinishObjectiveStep()</span>, qui notifie le système (<span style="color: #d9d9a7;">AdvanceObjective</span>) pour charger l'étape suivante ou marquer l'objectif comme terminé. Toute la communication repose sur le bus d'événements central <span style="color: #d9d9a7;">ObjectiveEvents</span>.

<figure style="margin: 0;">
<img src="http://51.77.147.126/api/images/images/objective_system.png" alt="Aperçu du système d’objectifs" style="width: 100%; height: auto;">
<figcaption style="color: #ada9a3; text-align: left;">Aperçu du système d’objectifs</figcaption>
</figure>
</br>

On a par exemple le premier objectif du jeu "When Light Fades", dont l'identifiant est <span style="color: #d9d9a7;">Objective_RestoreLights</span>. Il est composé de quatre étapes, définies dans le ScriptableObject <span style="color: #d9d9a7;">ObjectiveInfoSO</span> :

<figure style="margin: 0;">
<img src="http://51.77.147.126/api/images/images/objective_restorelights.png" alt="Instance d’ObjectiveInfoSO pour l’objectif “When Light Fades”" style="width: 100%; height: auto;">
<figcaption style="color: #ada9a3; text-align: left;">Instance d’ObjectiveInfoSO pour l’objectif “When Light Fades”</figcaption>
</figure>
</br>
  
La première étape, <span style="color: #d9d9a7;">FindBreakerStep</span>, consiste à essayer d’ouvrir la porte d’entrée. Elle utilise le composant <span style="color: #d9d9a7;">InteractionObjectiveStep</span>, qui écoute l’événement d’interaction <span style="color: #d9d9a7;">try_open_entrance_door</span>. Lorsque cet événement est déclenché (en interagissant avec la porte), l’étape est automatiquement validée.

<figure style="margin: 0;">
<img src="http://51.77.147.126/api/images/images/step_find_circuitbreaker.png" alt="Script InteractionObjectiveStep attaché au préfab FindBreakerStep avec comme cible try_open_entrance_door" style="width: 100%; height: auto;">
<figcaption style="color: #ada9a3; text-align: left;">Script InteractionObjectiveStep attaché au préfab FindBreakerStep avec comme cible try_open_entrance_door</figcaption>
</figure>
</br>

La deuxième étape, <span style="color: #d9d9a7;">FindKeyStep</span>, demande au joueur de récupérer la clé de la porte. On utilise ici le composant <span style="color: #d9d9a7;">ItemObjectiveStep</span>, qui attend que l’objet nommé "Key" soit ajouté à l’inventaire. Dès que c’est le cas, l’étape est validée et l’objectif passe à l’étape suivante.

<figure style="margin: 0;">
<img src="http://51.77.147.126/api/images/images/step_find_entrancekey.png" alt="Script ItemObjectiveStep attaché au préfab FindKeyStep avec comme cible l’item nommé “Key”" style="width: 100%; height: auto;">
<figcaption style="color: #ada9a3; text-align: left;">Script ItemObjectiveStep attaché au préfab FindKeyStep avec comme cible l’item nommé “Key”</figcaption>
</figure>

### Gestion des entrées

L’<span style="color: #d9d9a7;">InputManager</span> sert de point central pour toutes les entrées du joueur. Il utilise le nouveau système d’Input d’Unity pour récupérer les actions définies dans le projet (déplacements, mouvement caméra, interaction, etc.), puis met à jour des propriétés que les autres scripts peuvent consulter facilement (<span style="color: #d9d9a7;">Move</span>, <span style="color: #d9d9a7;">Look</span>, <span style="color: #d9d9a7;">Run</span>, <span style="color: #d9d9a7;">Interact</span>, etc.).

<figure style="margin: 0;">
<img src="http://51.77.147.126/api/images/images/input_manager.png" alt="Aperçu de la gestion des entrées" style="width: 100%; height: auto;">
<figcaption style="color: #ada9a3; text-align: left;">Aperçu de la gestion des entrées</figcaption>
</figure>
</br>

L’idée, c’est de découpler totalement la logique d'entrée du reste du code : les autres systèmes n’ont pas à savoir comment les touches sont configurées, ils lisent simplement ce que fait le joueur.

<table style="border-collapse: collapse; width: 100%; font-size: 13px;">
  <tr>
    <th style="border: 1px solid #2f2f2f; background-color: #202020; width: 25%; padding: 8px; color: white; text-align: left;">Action</th>
    <th style="border: 1px solid #2f2f2f; background-color: #202020; width: 75%; padding: 8px; color: white; text-align: left;">Key</th>
  </tr>
  <tr>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">Déplacement</td>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">Z/Q/S/D</td>
  </tr>
  <tr>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">Caméra</td>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">Curseur souris</td>
  </tr>
  <tr>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">Courir</td>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">Shift</td>
  </tr>
  <tr>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">S’accroupir</td>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">C</td>
  </tr>
  <tr>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">Interagir</td>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">E</td>
  </tr>
  <tr>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">Utiliser</td>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">F</td>
  </tr>
  <tr>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">Jeter</td>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">G</td>
  </tr>
  <tr>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">Sélectionner un slot</td>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">1/2/3/4</td>
  </tr>
  <tr>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">Switch de slot</td>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">Molette souris</td>
  </tr>
</table>

### Mouvements du joueur

Le système de mouvement du joueur repose sur le contrôleur d’animation <span style="color: #d9d9a7;">AC_PlayerController</span>, basé sur un Blend Tree 2D qui gère les transitions entre la marche et la course en fonction de la direction et de la vitesse du personnage. La majorité des animations proviennent de la bibliothèque [Mixamo](https://www.mixamo.com/). Pour celles qui manquaient (comme la marche arrière en étant accroupi) nous sommes passés par Blender pour inverser et adapter une animation existante.

<figure style="margin: 0;">
<img src="http://51.77.147.126/api/images/images/playercontroller_blendtree.png" alt="Blend Tree 2D de l’état par défaut de AC_PlayerController" style="width: 100%; height: auto;">
<figcaption style="color: #ada9a3; text-align: left;">Blend Tree 2D de l’état par défaut de AC_PlayerController</figcaption>
</figure>

<figure style="margin: 0;">
<img src="http://51.77.147.126/api/images/images/playercontroller.png" alt="Différents états de AC_PlayerController" style="width: 100%; height: auto;">
<figcaption style="color: #ada9a3; text-align: left;">Différents états de AC_PlayerController</figcaption>
</figure>

### Système de respiration et buée

Pour renforcer l'immersion et traduire l'état émotionnel du joueur, nous avons développé un système de respiration dynamique couplé à un effet visuel de buée. L'objectif était de créer une boucle sensorielle complète : plus le personnage est anxieux, plus sa respiration s'intensifie, et plus la buée qu'il exhale devient visible et dense.

Le système repose sur trois composants principaux : un contrôleur d'anxiété (<span style="color: #d9d9a7;">PlayerAnxietyController</span>), une gestion sonore via FMOD (<span style="color: #d9d9a7;">PlayerSound</span>), et un contrôleur de particules pour la buée (<span style="color: #d9d9a7;">BreathFogController</span>).

<figure style="margin: 0;">
<img src="http://51.77.147.126/api/images/images/breathing_system.png" alt="Aperçu du système d'anxiété et de respiration" style="width: 100%; height: auto;">
<figcaption style="color: #ada9a3; text-align: left;">Aperçu du système d'anxiété et de respiration</figcaption>
</figure>
</br>

Le <span style="color: #d9d9a7;">PlayerAnxietyController</span> centralise la gestion de l'anxiété du joueur sur une échelle de 0 à 100. Il distingue une anxiété de base (définie par l'environnement via des <span style="color: #d9d9a7;">AnxietyTrigger</span>) et des pics temporaires (provoqués par des événements ponctuels comme l'apparition de l'entité). L'anxiété effective est interpolée progressivement pour éviter les transitions brutales, et les pics se résorbent naturellement au fil du temps.

Pour la partie audio, nous avons utilisé FMOD Studio afin de créer un système de respiration adaptatif. L'event parent <span style="color: #d9d9a7;">Breathing</span> contient quatre sous-events correspondant à différents états émotionnels : <span style="color: #d9d9a7;">Breathing_Normal</span>, <span style="color: #d9d9a7;">Breathing_Stressed</span>, <span style="color: #d9d9a7;">Breathing_Heavy</span> et <span style="color: #d9d9a7;">Breathing_Panic</span>. Chaque sous-event est placé sur un track séparé dans une Timeline Sheet, et tous jouent simultanément en boucle.

La transition entre ces états repose donc sur un paramètre <span style="color: #d9d9a7;">Anxiety</span> (0-100) qui module le volume de chaque Event Instrument via des courbes d'automation. Concrètement, à une anxiété de 0, seul <span style="color: #d9d9a7;">Breath_Normal</span> est audible ; à 100, c'est <span style="color: #d9d9a7;">Breath_Panic</span> qui domine. Les zones intermédiaires créent un crossfade fluide entre les états adjacents, donnant l'impression d'une respiration qui s'emballe progressivement plutôt que de sauter d'un état à l'autre.

<figure style="margin: 0;">
<img src="http://51.77.147.126/api/images/images/fmod_breathing_highlight.PNG" alt="Vue d'ensemble de l'event Player_Breathing dans FMOD Studio" style="width: 100%; height: auto;">
<figcaption style="color: #ada9a3; text-align: left;">Vue d'ensemble de l'event Breathing dans FMOD Studio (<span style="color: #d9d9a7;">1:</span> aperçu des différents events, <span style="color: #d9d9a7;">2:</span> paramètre Anxiety réglé à 60.5, <span style="color: #d9d9a7;">3:</span> automatisation du volume du premier audio selon le paramètre Anxiety, ici à 0 le son est audible et disparaît en approchant 33, <span style="color: #d9d9a7;">4:</span> volume des différents tracks, ici le niveau d'anxiété étant à 60.5, seul le troisième audio (Breathing_Heavy) est audible)</figcaption>
</figure>
</br>

Pour synchroniser l'effet visuel de buée avec l'audio, chaque sous-event contient des markers nommés <span style="color: #d9d9a7;">Expire\_{niveau}</span> (par exemple <span style="color: #d9d9a7;">Expire_0</span>, <span style="color: #d9d9a7;">Expire_33</span>, <span style="color: #d9d9a7;">Expire_66</span>, <span style="color: #d9d9a7;">Expire_100</span>) placés au moment précis de l'expiration dans l'audio. Côté Unity, <span style="color: #d9d9a7;">PlayerSound</span> s'abonne aux callbacks de timeline FMOD et détecte ces markers. Lorsqu'un marker est atteint et que le niveau d'anxiété actuel correspond (avec une tolérance de ±17), un événement <span style="color: #d9d9a7;">OnExpire</span> est émis.

<figure style="margin: 0;">
<img src="http://51.77.147.126/api/images/images/fmod_markers.png" alt="Track du sous-event Breathing_Panic avec les markers Expire_100" style="width: 100%; height: auto;">
<figcaption style="color: #ada9a3; text-align: left;">Track du sous-event Breathing_Panic avec les markers Expire_100</figcaption>
</figure>
</br>

Le <span style="color: #d9d9a7;">BreathFogController</span> écoute cet événement et déclenche l'émission de particules. Le nombre de particules émises dépend également de l'anxiété : une respiration calme produit peu de buée, tandis qu'une respiration paniquée génère un nuage plus dense et visible. Ce détail renforce subtilement la tension sans jamais être explicite.

<figure style="margin: 0;">
  <iframe width="100%" height="480" 
          src="https://www.youtube.com/embed/MNAbsvxD3Ek"
          title="Demo of the Breathing event in Unity with FMOD"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
          allowfullscreen>
  </iframe>
  <figcaption style="color: #ada9a3; text-align: left;">
    Démonstration de l'event Breathing dans Unity avec FMOD
  </figcaption>
</figure>

<figure style="margin: 0;">
  <iframe width="100%" height="480" 
          src="https://www.youtube.com/embed/U5V89zKYve8"
          title="Unity FMOD - In-game breathing and fog rendering by anxiety zones"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
          allowfullscreen>
  </iframe>
  <figcaption style="color: #ada9a3; text-align: left;">
    Rendu en jeu de la respiration et de la buée selon les zones d'anxiété
  </figcaption>
</figure>

## III. Partie Artistique

Lorsque nous avons fini de développer l’idée, nous avons pensé tout d’abord au plan de l’appartement. Nos points de direction étaient l’appartement du personnage (en rouge), celui du voisin (en violet) ainsi que de longs couloirs (en vert clair), typique des Backrooms, un concept popularisé par la culture internet et les “creepypastas”. Autour de cette base, nous avons ajouté deux autres appartements (en jaune), des toilettes de palier (en rose) et un débarras commun (en vert foncé) pour ne pas fermer la porte au développement futur du projet.

<figure style="margin: 0;">
<img src="http://51.77.147.126/api/images/images/apartment_layout.png" alt="Plan final de l’appartement" style="width: 100%; height: auto;">
<figcaption style="color: #ada9a3; text-align: left;">Plan final de l’appartement</figcaption>
</figure>
</br>

Pour poser l’ambiance et donner une première lecture de cet espace, on a beaucoup réfléchi à l’éclairage. Le contraste entre la lumière du couloir et celle de l’appartement n’est pas là par hasard : on voulait que l’extérieur paraisse froid, presque clinique, comme un espace transitoire sans vie propre. À l’inverse, l’intérieur de l’appartement est plus lumineux, mais cette lumière révèle un désordre inquiétant, presque dérangeant. L’idée, c’était de créer un malaise subtil dès les premiers instants, en montrant que même un lieu familier comme son propre chez-soi peut rapidement devenir instable, voire menaçant. Ce jeu de lumière nous permet de suggérer que l’étrangeté ne vient pas forcément de l’extérieur, mais peut très bien surgir de l’intérieur, là où on est censé se sentir en sécurité.

<figure style="margin: 0;">
<img src="http://51.77.147.126/api/images/images/hallway_apartment_lights.png" alt="Différences d’éclairage entre le couloir principal et l’appartement du personnage" style="width: 100%; height: auto;">
<figcaption style="color: #ada9a3; text-align: left;">Différences d’éclairage entre le couloir principal et l’appartement du personnage</figcaption>
</figure>
</br>

Sur le plan narratif, l’étage représente la conscience troublée du personnage, tandis que l’appartement du voisin symbolise le traumatisme qu’il refuse d’affronter. En effet, notre protagoniste est marqué par un traumatisme dont il évite constamment de prendre conscience, ce que nous avons voulu traduire visuellement dans l'environnement. On retrouve ainsi plusieurs indices subtils dans son appartement : des tableaux représentant sa famille, avec son propre visage effacé, symbole de son refus d'affronter son identité et ses actes passés. On découvre aussi un fauteuil entouré de bouteilles d’alcool, élément qui renvoie directement à sa manière d'éviter de confronter la réalité, préférant sombrer dans l'oubli plutôt que d’affronter ses souvenirs douloureux. L’horloge, placée près du fauteuil, symbolise le temps qui passe et que le personnage tente en vain d’ignorer. Son son, régulier et oppressant, perturbe complètement le silence.

<figure style="margin: 0;">
<img src="http://51.77.147.126/api/images/images/player_apartment_elements.png" alt="Mise en évidence d’éléments clés dans le salon" style="width: 100%; height: auto;">
<figcaption style="color: #ada9a3; text-align: left;">Mise en évidence d’éléments clés dans le salon</figcaption>
</figure>
</br>

Tous les effets de post-processing reposent sur un seul profil appliqué à l’ensemble du niveau. Nous avons fait le choix assumé de ne pas multiplier les profils, préférant jouer directement sur la lumière et la scénographie pour créer différents effets émotionnels. Les réglages sont précis : un bloom marqué, accompagné d’une texture simulant une saleté sur l’objectif pour intensifier la sensation d’un regard trouble et fatigué ; une exposition fortement réduite et un contraste accentué, contribuant à l’ambiance oppressante du jeu. Nous avons ajouté du grain filmique pour évoquer une perception déformée, et une occlusion ambiante modérée afin d’intensifier l’impression d’espaces confinés et écrasants. Le vignettage discret permet quant à lui de focaliser subtilement l'attention du joueur, renforçant l'impression que quelque chose reste caché à la périphérie de sa vision.

<figure style="margin: 0;">
<img src="http://51.77.147.126/api/images/images/hallway_before_after.png" alt="Avant / après du post-processing dans le couloir principal" style="width: 100%; height: auto;">
<figcaption style="color: #ada9a3; text-align: left;">Avant / après du post-processing dans le couloir principal</figcaption>
</figure>
</br>

<figure style="margin: 0;">
<img src="http://51.77.147.126/api/images/images/apartment_before_after.png" alt="Avant / après du post-processing dans l’appartement" style="width: 100%; height: auto;">
<figcaption style="color: #ada9a3; text-align: left;">Avant / après du post-processing dans l’appartement</figcaption>
</figure>
</br>

Ce traitement visuel est directement inspiré de l’expressionnisme allemand, courant artistique où les décors, les ombres et les jeux de lumière ne cherchent pas à reproduire fidèlement la réalité, mais plutôt à exprimer des émotions brutes et des états psychologiques troublés. Dans notre jeu, c'est précisément cette approche qui est privilégiée : l'espace, l'éclairage et les choix graphiques ne sont pas là uniquement pour l'esthétique, mais deviennent le reflet direct de la psychologie du personnage principal, traduisant son angoisse intérieure et ses tentatives vaines d’échapper à son passé.

<figure style="margin: 0;">
<img src="http://51.77.147.126/api/images/images/apartment_before.png" alt="Vue du joueur sans le post-processing" style="width: 100%; height: auto;">
<figcaption style="color: #ada9a3; text-align: left;">Vue du joueur sans le post-processing</figcaption>
</figure>
</br>

<figure style="margin: 0;">
<img src="http://51.77.147.126/api/images/images/apartment_after.png" alt="Vue du joueur avec le post-processing" style="width: 100%; height: auto;">
<figcaption style="color: #ada9a3; text-align: left;">Vue du joueur avec le post-processing</figcaption>
</figure>

### Shader de l'entité Shadow

Pour renforcer l'atmosphère inquiétante du jeu, nous avons développé un shader personnalisé via Shader Graph (URP) destiné à l'entité qui hante le personnage. L'objectif était de créer une présence visuelle qui ne soit jamais totalement figée, une silhouette sombre qui semble respirer, vibrer, comme habitée par une énergie obscure. Cette approche s'inscrit dans notre volonté de ne jamais révéler clairement les détails de cette menace, préférant suggérer le danger plutôt que de l'exposer frontalement.

Le shader repose sur plusieurs paramètres exposés qui permettent d'ajuster finement le comportement visuel de l'entité : la couleur de base (un noir profond), la vitesse et l'intensité de la pulsation, ainsi que l'échelle et la vélocité du bruit procédural. Cette modularité nous a permis d'itérer rapidement sur le rendu jusqu'à obtenir un équilibre entre subtilité et malaise.

<div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 20px; flex-wrap: wrap;">

  <figure style="margin: 0; width: 40%;">
    <img src="http://51.77.147.126/api/images/images/sg_shadow_properties.png" alt="Properties du shader SG_Shadow" style="width: 100%; height: auto;">
    <figcaption style="color: #ada9a3; text-align: left;">Properties du shader SG_Shadow</figcaption>
  </figure>

  <figure style="margin: 0; width: 45%;">
    <img src="http://51.77.147.126/api/images/images/sg_shadow_preview.gif" alt="Aperçu du shader SG_Shadow" style="width: 100%; height: auto;">
    <figcaption style="color: #ada9a3; text-align: left;">Aperçu du shader SG_Shadow</figcaption>
  </figure>

</div>
</br>

<table style="border-collapse: collapse; width: 100%; font-size: 13px;">
  <tr>
    <th style="border: 1px solid #2f2f2f; background-color: #202020; width: 25%; padding: 8px; color: white; text-align: left;">Property</th>
    <th style="border: 1px solid #2f2f2f; background-color: #202020; width: 75%; padding: 8px; color: white; text-align: left;">Effect</th>
  </tr>
  <tr>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">Base Color</td>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">Couleur de base sombre</td>
  </tr>
  <tr>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">Pulse Speed</td>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">Vitesse de la "respiration"</td>
  </tr>
  <tr>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">Pulse Intensity</td>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">Amplitude de la déformation</td>
  </tr>
  <tr>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">Noise Scale</td>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">Taille des "vagues" de déformation</td>
  </tr>
  <tr>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">Noise Speed</td>
    <td style="border: 1px solid #2f2f2f; padding: 8px;">Vitesse de l'animation du bruit</td>
  </tr>
</table>

La première composante technique est le déplacement de vertex. Plutôt que de laisser le mesh statique, nous appliquons une déformation continue basée sur un bruit procédural (Simple Noise) animé dans le temps. Ce bruit est projeté sur les normales du mesh, créant des ondulations organiques à la surface de l'entité. Le résultat donne l'impression que la silhouette n'est jamais stable, qu'elle frémit constamment, comme si elle luttait pour maintenir sa forme. Cette instabilité visuelle contribue directement au sentiment d'étrangeté et de menace latente que nous cherchions à provoquer.

<figure style="margin: 0;">
<img src="http://51.77.147.126/api/images/images/sg_shadow_vertex_displacement.png" alt="Aperçu du bloc Vertex Displacement dans le shader SG_Shadow" style="width: 100%; height: auto;">
<figcaption style="color: #ada9a3; text-align: left;">Aperçu du bloc Vertex Displacement dans le shader SG_Shadow</figcaption>
</figure>
</br>

La seconde composante concerne la surface elle-même. Nous avons opté pour une couleur de base quasi noire, volontairement dépourvue de détails, afin de préserver le mystère autour de cette entité. À cela s'ajoute une émission pulsante, contrôlée par une fonction sinusoïdale liée au temps. Cette pulsation subtile simule une forme de respiration, donnant vie à ce qui devrait être une simple silhouette inerte. L'émission reste très faible, juste assez pour que le joueur perçoive inconsciemment ce mouvement sans pouvoir l'identifier clairement, renforçant ainsi le malaise psychologique.

<figure style="margin: 0;">
<img src="http://51.77.147.126/api/images/images/sg_shadow_surface.png" alt="Aperçu du bloc Surface Emission Pulse dans le shader SG_Shadow" style="width: 100%; height: auto;">
<figcaption style="color: #ada9a3; text-align: left;">Aperçu du bloc Surface Emission Pulse dans le shader SG_Shadow</figcaption>
</figure>
</br>

<figure style="margin: 0;">
<img src="http://51.77.147.126/api/images/images/sg_shadow.gif" alt="Rendu de l'entité en jeu avec le shader appliqué" style="width: 100%; height: auto;">
<figcaption style="color: #ada9a3; text-align: left;">Rendu de l'entité en jeu avec le shader appliqué</figcaption>
</figure>
</br>

Ce choix artistique s'inscrit pleinement dans notre direction visuelle inspirée de l'expressionnisme : l'entité n'est pas simplement un ennemi ou un obstacle, elle est la manifestation visuelle du traumatisme refoulé du personnage, une ombre animée qui observe et attend, imprévisible et menaçante.

### Essaim de moucherons

Pour renforcer le sentiment de malaise et de décrépitude lors de l'entrée dans l'appartement du voisin durant la quête "I'm Watching You", nous avons créé un essaim de moucherons à l'aide du système de particules d'Unity. L'objectif était de suggérer immédiatement que quelque chose ne va pas dans cet espace, sans avoir besoin de le montrer explicitement. Les insectes, par leur présence bourdonnante et chaotique, évoquent instinctivement la décomposition, l'abandon, et préparent le joueur à découvrir une scène perturbante.

Le système repose sur un émetteur en forme de boîte (Box Shape) qui génère des particules en continu dans un volume rectangulaire, simulant un nuage d'insectes concentré dans une zone précise de l'entrée. Chaque particule possède une durée de vie aléatoire et une taille variable pour éviter l'uniformité visuelle. Le mouvement est rendu organique grâce au module Noise, qui applique une turbulence tridimensionnelle aux trajectoires, donnant l'impression que chaque moucheron vole de manière erratique et imprévisible, comme le ferait un véritable insecte.

<figure style="margin: 0;">
  <iframe width="100%" height="480" 
          src="https://www.youtube.com/embed/5Wy6cYVV1kU"
          title="Preview of a particle system simulating a swarm of flies in an enclosed space"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
          allowfullscreen>
  </iframe>
  <figcaption style="color: #ada9a3; text-align: left;">
    Aperçu d’un essaim de moucherons simulé par un système de particules dans un espace fermé (<span style="color: #d9d9a7;">FlySwarmBoundary</span>)
  </figcaption>
</figure>

Pour le rendu visuel, nous avons créé un Sprite Atlas regroupant cinq sprites de moucherons différents, chacun représentant une silhouette légèrement distincte. Le module Texture Sheet Animation permet ensuite de sélectionner aléatoirement l'un de ces sprites pour chaque particule émise, brisant ainsi la répétition visuelle et donnant l'illusion d'un essaim composé d'individus variés. Ce détail, bien que subtil, contribue grandement au réalisme de l'effet.

<figure style="margin: 0;">
<img src="http://51.77.147.126/api/images/images/flies_neighbor.gif" alt="Rendu de l'essaim de moucherons à l'entrée de l'appartement du voisin" style="width: 100%; height: auto;">
<figcaption style="color: #ada9a3; text-align: left;">Rendu de l'essaim de moucherons à l'entrée de l'appartement du voisin</figcaption>
</figure>
</br>

Ce détail environnemental, bien que discret, participe pleinement à l'atmosphère oppressante du jeu. Il illustre notre approche narrative : plutôt que d'exposer frontalement l'horreur, nous préférons la suggérer par des indices sensoriels qui s'accumulent progressivement dans l'esprit du joueur.

### Pluie

Pour renforcer l'isolement du personnage et accentuer l'atmosphère mélancolique de l'appartement, nous avons intégré un effet de pluie visible depuis les fenêtres. L'objectif n'était pas de créer une pluie réaliste couvrant tout l'environnement, mais plutôt de suggérer un monde extérieur hostile et inaccessible, renforçant le sentiment de claustrophobie du protagoniste enfermé dans son espace mental.

Le système repose sur un émetteur en forme de boîte positionné devant les fenêtres. Les particules sont étirées verticalement grâce au mode Stretched Billboard, simulant des gouttes en chute rapide. Leur vélocité est randomisée sur l'axe Y pour éviter un effet trop uniforme et mécanique. Le module Collision est activé avec un amortissement maximal et aucun rebond, permettant aux gouttes de "mourir" proprement au contact des surfaces sans comportement physique parasite.

<figure style="margin: 0;">
  <iframe width="100%" height="480" 
          src="https://www.youtube.com/embed/Enl-TOU3O6s"
          title="Rain rendering on the apartment window"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
          allowfullscreen>
  </iframe>
  <figcaption style="color: #ada9a3; text-align: left;">
    Rendu de la pluie à la fenêtre de l'appartement du joueur
  </figcaption>
</figure>

L'effet visuel est accompagné d'une ambiance sonore de pluie générée via [myNoise](https://mynoise.net/NoiseMachines/rainNoiseGenerator.php), un générateur de bruits d'ambiance. Ce son continu et enveloppant participe à l'immersion en créant une couche sonore supplémentaire qui isole le joueur du silence oppressant de l'appartement, tout en rappelant constamment la présence d'un extérieur qu'il ne peut atteindre.

<figure style="margin: 0;">
  <audio controls style="width: 100%;">
    <source src="http://51.77.147.126/api/audio/audio/rain_ambience.wav" type="audio/wav">
    Votre navigateur ne supporte pas la lecture audio.
  </audio>
  <figcaption style="color: #ada9a3; text-align: left;">Ambiance sonore de pluie générée via <a href="https://mynoise.net/NoiseMachines/rainNoiseGenerator.php">myNoise</a></figcaption>
</figure>

### Conception Sonore

Enfin, l'ambiance sonore a été une composante essentielle pour appuyer l'atmosphère du jeu.

Enfin, l’ambiance sonore a été une composante essentielle pour appuyer l’atmosphère du jeu. Nous avons utilisé un son de fond constant et aigu pour installer une tension et un sentiment d'inconfort.

<figure style="margin: 0;">
  <audio controls style="width: 100%;">
    <source src="http://51.77.147.126/api/audio/audio/ha-undercurrent.wav" type="audio/wav">
    Votre navigateur ne supporte pas la lecture audio.
  </audio>
  <figcaption style="color: #ada9a3; text-align: left;">Son joué en arrière-plan dans le jeu, <a href="https://assetstore.unity.com/packages/audio/music/free-horror-ambience-2-215651">Free Horror Ambience 2</a></figcaption>
</figure>
</br>

À cela viennent s'ajouter d'autres éléments ponctuels : le bruit régulier et mécanique d’une horloge, le ronronnement étouffé d’un réfrigérateur, ou encore l’intervention inattendue d’une voix féminine lors du premier objectif, "When Light Fades", quand le joueur passe devant la porte du voisin.

Cette voix, générée via une IA (Elevenlabs), crie « Pourquoi tu m’as fait ça ? », accompagnée de coups violents contre une porte, et a été travaillée avec de la réverbération et un filtre passe-bas sur Audacity pour renforcer le réalisme et l'état émotionnel. Et petite anecdote, pour composer la voix, je me suis inspiré de la scène emblématique où Leonardo DiCaprio implore sa mère de le laisser entrer dans le film _The Basketball Diaries_.

<figure style="margin: 0;">
  <audio controls style="width: 100%;">
    <source src="http://51.77.147.126/api/audio/audio/FemaleWhy.wav" type="audio/wav">
    Votre navigateur ne supporte pas la lecture audio.
  </audio>
  <figcaption style="color: #ada9a3; text-align: left;">Voix féminine utilisée dans Flat criant “Pourquoi tu m’as fait ça”, son traité du Audacity</figcaption>
</figure>
</br>

<figure style="margin: 0;">
  <audio controls style="width: 100%;">
    <source src="http://51.77.147.126/api/audio/audio/door.wav" type="audio/wav">
    Votre navigateur ne supporte pas la lecture audio.
  </audio>
  <figcaption style="color: #ada9a3; text-align: left;">Tapage violent contre la porte, traité sur Audacity, <a href="https://pixabay.com/fr/users/freesound_community-46691455/">freesound_commnity</a></figcaption>
</figure>
</br>

Enfin, nous avons aussi travaillé les pas du personnage, pour renforcer l’immersion et rendre l’expérience plus réaliste.

<figure style="margin: 0;">
  <audio controls style="width: 100%;">
    <source src="http://51.77.147.126/api/audio/audio/Footstep_carpet1.wav" type="audio/wav">
    Votre navigateur ne supporte pas la lecture audio.
  </audio>
  <figcaption style="color: #ada9a3; text-align: left;">Extrait de sons de pas sur du tapis, utilisés pour le sol dans le couloir de l’étage, <a href="https://www.youtube.com/watch?v=19Y3yAGWcRc">Everyday Cinematic Sounds</a></figcaption>
</figure>
</br>

Pour finir avec l’interface utilisateur, nous avons opté pour un design très épuré, inspiré du jeu _Dying Light_. L’objectif était de proposer quelque chose de simple, lisible, et non intrusif, qui n'interfère jamais avec l’ambiance ou la tension du jeu. Nous avons utilisé des éléments discrets, une typographie claire ([Museo](https://fonts.adobe.com/fonts/museo#about-section)) et un code couleur limité, notamment avec l’orange pour mettre en valeur certaines informations importantes, comme les objectifs ou les interactions.

<figure style="margin: 0;">
<img src="http://51.77.147.126/api/images/images/interface.png" alt="Vue du joueur avec le post-processing" style="width: 100%; height: auto;">
<figcaption style="color: #ada9a3; text-align: left;">Aperçu des éléments de l’interface</figcaption>
</figure>

## IV. Démo

<figure style="margin: 0;">
  <iframe width="100%" height="480" 
          src="https://www.youtube.com/embed/dmeN4AAUujA"
          title="Flat - Démo 2024-2025"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
          allowfullscreen>
  </iframe>
  <figcaption style="color: #ada9a3; text-align: left;">
    Flat - Démo 2024-2025
  </figcaption>
</figure>

<figure style="margin: 0;">
  <iframe width="100%" height="480" 
          src="https://www.youtube.com/embed/NIrGnWUDSQ8"
          title="Flat - Démo 2025-2026"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
          allowfullscreen>
  </iframe>
  <figcaption style="color: #ada9a3; text-align: left;">
    Flat - Démo 2025-2026
  </figcaption>
</figure>

<figure style="margin: 0;">
  <iframe width="100%" height="480" 
          src="https://www.youtube.com/embed/FS1AbfgW82c"
          title="Bonus"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
          allowfullscreen>
  </iframe>
  <figcaption style="color: #ada9a3; text-align: left;">
    Bonus
  </figcaption>
</figure>

## Références

1. How create a Quest System in Unity | RPG Style | Including Data Persistence -  https://www.youtube.com/watch?v=UyTJLDGcT64
2. Adding Footsteps and Randomizing | Audio in Unity Episode3 - https://www.youtube.com/watch?v=xbtSM7B_htU
3. Unity Inventory UI Tutorial - https://www.youtube.com/watch?v=-xB4xEmGtCY&list=PLg7sMWZoap4B8N1pR8nl2-eG_D5k9MfWY&index=1
4. Horror Post Processing Profile in Unity - https://www.youtube.com/watch?v=OiZXAsn5BWo
5. LORD of the FLIES (Unity Particle System Tutorial) - https://www.youtube.com/watch?v=6OKaDjlHJJ8
6. Add Rain to your Unity Games! | Unity Tutorial - https://www.youtube.com/watch?v=MBVGUD5nZeA
