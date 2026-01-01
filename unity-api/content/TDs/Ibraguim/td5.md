# TD 5 : Dômes Célestes

## Skydome

### Théorique
**Qu'est-ce qu'un skydome ?**
C'est une grande sphère ou demi-sphère texturée qui entoure la scène 3D pour simuler le ciel et l'horizon. Il donne une impression de profondeur infinie et contribue à l'immersion en empêchant le joueur de voir le "vide" du moteur de jeu.

### Pratique
**Création dans Unity :**
1.  Créer une sphère inversée (ou importer un modèle de dôme).
2.  Lui appliquer un matériau avec un shader "Unlit/Texture" ou "Skybox" pour qu'il ne soit pas affecté par l'éclairage de la scène.
3.  **Important :** Le script de contrôle doit centrer le Skydome sur la position de la caméra à chaque frame (sans copier la rotation) pour donner l'illusion qu'il est infiniment loin.

## Turbidité

### Théorique
**Impact de la turbidité :**
La turbidité représente la "brumosité" de l'air (poussière, humidité). Une turbidité élevée rend le ciel moins bleu (plus blanc/gris), diffuse davantage la lumière et rend les couchers de soleil plus rouges et plus longs. C'est essentiel pour sentir la densité de l'atmosphère.

### Pratique
**Implémentation Unity :**
On peut simuler cela simplement avec le **Fog** (Brouillard) d'Unity.
*   **Paramètres à exposer :** `float turbidityLevel` (0 à 1).
*   **Visuel :** Ce paramètre contrôlerait `RenderSettings.fogDensity` et interpolerait `RenderSettings.fogColor` entre une couleur claire (ciel pur) et une couleur grisâtre/ocre (air pollué).

```csharp
public float turbidity; // 0 à 10
void Update() {
    RenderSettings.fogDensity = turbidity * 0.01f;
    // Changer la couleur du fog vers le gris/orange si turbidité élevée
}
```

## Diffusion de Rayleigh

### Théorique
**Principe :**
C'est la diffusion de la lumière par les molécules d'air (très petites). Elle diffuse surtout les ondes courtes (bleu), d'où le ciel bleu. Au coucher du soleil, la lumière traverse plus d'atmosphère, le bleu est dispersé, il ne reste que le rouge.

### Pratique
**Système dynamique :**
L'altitude du joueur réduirait la densité de l'atmosphère.
*   **Formule simplifiée :** `CouleurCiel = Lerp(BleuCiel, NoirEspace, Altitude / MaxAltitude)`.
*   Plus on monte, moins il y a de diffusion (le ciel devient noir).
*   Au sol, la couleur dépend de l'angle du soleil (Bleu à midi, Rouge au soir).

## Théorie de Mie

### Théorique
**Principe :**
C'est la diffusion par des particules plus grosses (gouttelettes d'eau, aérosols). Contrairement à Rayleigh, elle n'est pas très dépendante de la couleur (donc lumière blanche) et est très directionnelle (vers l'avant). C'est ce qui crée le halo blanc éblouissant autour du soleil.

### Pratique
**Simulation du Halo :**
On peut utiliser un **Sprite** de halo (Billboard) sur la position du soleil ou un effet de **Bloom**.
*   **Paramètres :** `HaloIntensity`, `HaloSize`.
*   Si le temps est nuageux (Mie élevé), on augmente la taille et l'opacité du halo blanc autour de la source lumineuse directionnelle.

## Luminosité de la lumière du soleil

### Théorique
**Calcul :**
La luminosité dépend de l'angle d'incidence du soleil. À midi (zénith), l'intensité est maximale. Au coucher, la lumière traverse plus d'air et perd en énergie.

### Pratique
**Script de cycle jour/nuit :**
On fait varier l'intensité de la `DirectionalLight` selon sa rotation en X (hauteur).

```csharp
public Light sunLight;
void Update() {
    // Produit scalaire pour savoir si le soleil est haut (1) ou bas (0)
    float sunHeight = Vector3.Dot(sunLight.transform.forward, Vector3.down);
    // On clamp pour ne pas avoir de lumière négative la nuit
    sunLight.intensity = Mathf.Clamp01(sunHeight) * maxIntensity;
    
    // Changer la couleur : Blanc à midi, Rouge au soir
    sunLight.color = Color.Lerp(Color.red, Color.white, sunHeight);
}
```

## Objectifs d'un Skydome

### Théorique
**Objectifs :**
1.  **Repère spatial :** Donner le haut, le bas et l'horizon.
2.  **Ambiance :** Définir la météo et l'heure (ciel menaçant vs grand soleil).
3.  **Éclairage :** Servir de source pour l'éclairage ambiant (Global Illumination).

### Pratique
**Progression narrative :**
Créer un `SkyManager` qui écoute les événements du jeu.
*   *Mission Infiltration* -> Charger un profil "Nuit sombre".
*   *Mission Victoire* -> Transition vers "Aube claire".
*   Utiliser des `Coroutines` pour faire des transitions douces (fading) entre les propriétés du ciel (couleur, exposition) lors des changements de mission.

## Avantages et inconvénients des skydomes

### Théorique
*   **Avantages :** Très performant (juste une texture), facile à mettre en place, photoréaliste si la texture est bonne.
*   **Inconvénients :** Statique (les nuages ne bougent pas ou c'est une simple rotation), distorsion aux pôles de la sphère, résolution limitée (pixelisation si on zoom).

### Pratique
**Solution aux inconvénients (Environnements vastes) :**
Pour éviter l'effet statique sur une grande carte : utiliser un **Shader procédural** au lieu d'une texture fixe. Cela permet d'animer les nuages, de changer les couleurs dynamiquement sans perte de résolution, et de simuler le cycle jour/nuit sans changer de texture.

## Intégration (Missions et Cartes multiples)

### Théorique
Le ciel est un outil de narration visuelle. Il unifie la direction artistique d'une zone (ex: zone volcanique = ciel cendré).

### Pratique
**Approche dynamique :**
Utiliser des **Volumes** (comme le Post-Process Volume d'Unity) ou des **Triggers**.
*   Quand le joueur entre dans une zone (ex: "Forêt Maudite"), un script déclenche un changement progressif (`Lerp`) des paramètres du Skydome (couleur du brouillard, texture du ciel) vers le profil de cette zone.
*   Pour la performance : Ne pas instancier de nouveaux Skydomes, mais modifier les matériaux de celui existant. L'IDEE EST DE CE CENTRER SUR LES QUESTIONS NON CODE ET DONNER UN MINIMUM DE CODD QD MEME