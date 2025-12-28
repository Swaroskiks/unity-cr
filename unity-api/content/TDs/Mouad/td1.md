# Compte rendu — TD 1 : Création d’un terrain sous Unity  
*ESIEE – Année 2025-2026*  
*Référence : TD 1 Unity*  [oai_citation:0‡Chapitre 3 - TD 1.pdf](sediment://file_0000000008f0720e80fb27570d8bd58f)

## 1. Finalité et utilité du TD
Ce premier TD avait pour but de nous initier aux outils fondamentaux de création d’environnements 3D dans Unity.  
L’objectif n’était pas simplement de produire un terrain, mais de comprendre les mécanismes de base utilisés dans l’industrie pour générer rapidement un prototype de scène : sculpture de reliefs, gestion des textures, placement procédural d’arbres et d’herbes, ainsi que composition visuelle d’un paysage cohérent.  
Ce TD pose donc les fondations nécessaires pour tout travail futur de level design ou de prototypage en 3D.

## 2. État de l’art
Unity propose un système de terrain intégré combinant :
- **Des outils de sculpture** (élévation, abaissement, lissage) permettant de modeler un relief de manière intuitive.
- **Des systèmes de texturation multi-couches** pour reproduire des sols variés (terre, roche, herbe), en s’appuyant sur des textures sans couture.
- **Un moteur de végétation** permettant de placer et de gérer arbres, buissons et herbes avec des réglages de densité, de variation et de performance (LOD).
- **Un écosystème d’assets** (Asset Store) incluant textures, arbres, shaders d’eau et prefabs, permettant d’accélérer la création d’environnements.

Ces outils sont standard dans la plupart des workflows de conception d’environnements 3D et sont utilisés dans les studios pour la pré-production ou le prototypage.

## 3. Apports du TD
Le TD m’a permis :
- de comprendre concrètement comment fonctionne l’outil Terrain de Unity ;  
- d’expérimenter les paramètres essentiels (taille du pinceau, opacité, intensité) et leur impact sur le rendu ;  
- d’identifier les bonnes pratiques pour éviter les artefacts visuels (textures répétitives, transitions abruptes) ;  
- de me familiariser avec la logique de placement naturel de la végétation (densité variable selon l’altitude ou la proximité de l’eau) ;  
- d’intégrer un élément d’eau via un prefab et de comprendre son rôle dans la composition d’une scène.

Au-delà de l’aspect technique, le TD illustre l’importance de travailler avec des références visuelles pour obtenir un environnement crédible.

## 4. Usage raisonné de l’IA
L’IA a été utilisée uniquement pour clarifier quelques notions théoriques (ex. différence entre opacité et intensité dans la peinture de textures).  
Elle n’a pas remplacé l’expérimentation pratique mais a aidé à interpréter certains paramètres de l’outil.

## 5. Conclusion
Ce TD constitue une introduction essentielle au level design.  
Il montre comment Unity combine outils artistiques et techniques pour générer rapidement un environnement jouable.  
La compréhension de ces bases est indispensable pour la suite du module, notamment pour la création de scènes plus complexes, l’ajout d’interactions ou l’intégration d’un contrôleur joueur.