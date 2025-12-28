from seeds.image_loader import load_image_as_base64

QUESTIONS_DATA = [
    {
        'position': 1,
        'title': 'Qu\'est-ce que le Machine Learning ?',
        'description': 'Le Machine Learning est une branche de l\'intelligence artificielle. Mais qu\'est-ce qui le caractérise principalement ?',
        'answers': [
            {'answer_text': 'Un système qui suit des règles prédéfinies par un programmeur', 'is_correct': False},
            {'answer_text': 'Un système qui apprend à partir de données sans être explicitement programmé', 'is_correct': True},
            {'answer_text': 'Un langage de programmation spécialisé', 'is_correct': False},
            {'answer_text': 'Un type de base de données', 'is_correct': False}
        ],
        'image_base64': load_image_as_base64('machine-learning.webp')
    },
    {
        'position': 2,
        'title': 'Qu\'est-ce qu\'un réseau de neurones ?',
        'description': 'Les réseaux de neurones sont au cœur de l\'apprentissage profond. Comment fonctionnent-ils ?',
        'answers': [
            {'answer_text': 'Des ordinateurs connectés en réseau', 'is_correct': False},
            {'answer_text': 'Un modèle mathématique inspiré du cerveau humain avec des couches de neurones interconnectés', 'is_correct': True},
            {'answer_text': 'Un protocole de communication réseau', 'is_correct': False},
            {'answer_text': 'Un type de serveur web', 'is_correct': False}
        ],
        'image_base64': load_image_as_base64('reseaux-neurones.webp')
    },
    {
        'position': 3,
        'title': 'Qu\'est-ce qu\'une attaque par phishing ?',
        'description': 'Le phishing est l\'une des menaces les plus courantes en cybersécurité. En quoi consiste-t-il ?',
        'answers': [
            {'answer_text': 'Une attaque qui bloque l\'accès à un système', 'is_correct': False},
            {'answer_text': 'Une technique d\'ingénierie sociale visant à tromper les utilisateurs pour obtenir des informations sensibles', 'is_correct': True},
            {'answer_text': 'Un virus qui se propage par email', 'is_correct': False},
            {'answer_text': 'Une méthode de chiffrement des données', 'is_correct': False}
        ],
        'image_base64': load_image_as_base64('phishing.webp')
    },
    {
        'position': 4,
        'title': 'Qu\'est-ce que le Deep Learning ?',
        'description': 'Le Deep Learning a révolutionné l\'IA moderne. Quelle est sa particularité ?',
        'answers': [
            {'answer_text': 'Un apprentissage avec des réseaux de neurones à une seule couche', 'is_correct': False},
            {'answer_text': 'Un apprentissage avec des réseaux de neurones à plusieurs couches (deep)', 'is_correct': True},
            {'answer_text': 'Un langage de programmation pour l\'IA', 'is_correct': False},
            {'answer_text': 'Une méthode de stockage de données', 'is_correct': False}
        ],
        'image_base64': load_image_as_base64('deep-learning.webp')
    },
    {
        'position': 5,
        'title': 'Qu\'est-ce qu\'un ransomware ?',
        'description': 'Les ransomwares sont une menace majeure en cybersécurité. Comment fonctionnent-ils ?',
        'answers': [
            {'answer_text': 'Un logiciel qui protège contre les virus', 'is_correct': False},
            {'answer_text': 'Un malware qui chiffre les données et demande une rançon pour les déchiffrer', 'is_correct': True},
            {'answer_text': 'Un outil de sauvegarde automatique', 'is_correct': False},
            {'answer_text': 'Un protocole de sécurité réseau', 'is_correct': False}
        ],
        'image_base64': load_image_as_base64('ransomware.webp')
    },
    {
        'position': 6,
        'title': 'Qu\'est-ce que le Natural Language Processing (NLP) ?',
        'description': 'Le NLP permet aux machines de comprendre le langage humain. Quelle est sa fonction principale ?',
        'answers': [
            {'answer_text': 'Traiter et comprendre le langage humain par les machines', 'is_correct': True},
            {'answer_text': 'Créer des langages de programmation', 'is_correct': False},
            {'answer_text': 'Gérer les réseaux informatiques', 'is_correct': False},
            {'answer_text': 'Optimiser les performances des processeurs', 'is_correct': False}
        ],
        'image_base64': load_image_as_base64('nlp.webp')
    },
    {
        'position': 7,
        'title': 'Qu\'est-ce qu\'une attaque DDoS ?',
        'description': 'Les attaques DDoS sont fréquentes. En quoi consistent-elles ?',
        'answers': [
            {'answer_text': 'Une attaque qui supprime toutes les données d\'un serveur', 'is_correct': False},
            {'answer_text': 'Une attaque qui surcharge un serveur avec un trafic massif pour le rendre indisponible', 'is_correct': True},
            {'answer_text': 'Une méthode de chiffrement des communications', 'is_correct': False},
            {'answer_text': 'Un protocole de sécurité pour les emails', 'is_correct': False}
        ],
        'image_base64': load_image_as_base64('ddos.webp')
    },
    {
        'position': 8,
        'title': 'Qu\'est-ce que l\'apprentissage supervisé ?',
        'description': 'L\'apprentissage supervisé est l\'une des principales méthodes du Machine Learning. Comment fonctionne-t-il ?',
        'answers': [
            {'answer_text': 'Un apprentissage sans données étiquetées', 'is_correct': False},
            {'answer_text': 'Un apprentissage avec des données étiquetées (input et output connus)', 'is_correct': True},
            {'answer_text': 'Un apprentissage qui nécessite une supervision humaine constante', 'is_correct': False},
            {'answer_text': 'Un type de réseau neuronal spécialisé', 'is_correct': False}
        ],
        'image_base64': load_image_as_base64('learn.webp')
    },
    {
        'position': 9,
        'title': 'Qu\'est-ce qu\'un firewall ?',
        'description': 'Les firewalls sont essentiels pour la sécurité réseau. Quel est leur rôle ?',
        'answers': [
            {'answer_text': 'Un logiciel antivirus', 'is_correct': False},
            {'answer_text': 'Un système qui contrôle et filtre le trafic réseau selon des règles de sécurité', 'is_correct': True},
            {'answer_text': 'Un outil de sauvegarde de données', 'is_correct': False},
            {'answer_text': 'Un protocole de communication', 'is_correct': False}
        ],
        'image_base64': load_image_as_base64('firewall.webp')
    },
    {
        'position': 10,
        'title': 'Qu\'est-ce que ChatGPT utilise comme architecture ?',
        'description': 'ChatGPT a révolutionné l\'IA conversationnelle. Sur quelle technologie s\'appuie-t-il principalement ?',
        'answers': [
            {'answer_text': 'Des règles de programmation classiques', 'is_correct': False},
            {'answer_text': 'Des Transformers, un type de réseau de neurones pour le traitement du langage', 'is_correct': True},
            {'answer_text': 'Un système expert traditionnel', 'is_correct': False},
            {'answer_text': 'Un algorithme de recherche classique', 'is_correct': False}
        ],
        'image_base64': load_image_as_base64('chatgpt.webp')
    }
]
