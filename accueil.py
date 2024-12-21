import streamlit as st

def afficher_accueil():
    # Lien brut vers l'image sur GitHub
    image_url = "https://raw.githubusercontent.com/Awoutokoffisamson/Application_Web/main/co2_prediction_app/logo6.jpg"

    # Appliquer le CSS avec l'image en fond et des styles modernes
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            color: #00007F; /* Couleur du texte par défaut */
        }}
        .main-title {{
            font-size: 3.9rem;
            font-weight: bold;
            text-align: center;
            color: #00007F;
            background-color: #FFD700; /* Surlignage jaune */
            padding: 10px;
            border-radius: 10px;
        }}
        .intro-text {{
            font-size: 1.7rem;
            text-align: center;
            font-weight: bold;
            color: #FF0000;
            background-color: #FFFAE6; /* Surlignage clair */
            padding: 8px;
            border-radius: 10px;
            margin-bottom: 50px;
        }}
        .section-header {{
            font-size: 2.6rem;
            font-weight: bold;
            text-align: left;
            color: #00007F;
            text-shadow: 1px 1px 3px #00007F;
            background-color: #C0C0C0; /* Surlignage gris */
            padding: 10px;
            border-radius: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Contenu de la page d'accueil
    st.markdown('<h1 class="main-title">Bienvenue dans l\'application de prédiction de l\'émission du CO2</h1>', unsafe_allow_html=True)
    st.markdown('<p class="intro-text">Une application intuitive pour explorer et prédire l\'émission de CO2 des bâtiments de Seattle.</p>', unsafe_allow_html=True)

    st.markdown('<h2 class="section-header">🎯 Commencez dès maintenant !</h2>', unsafe_allow_html=True)

    # Ajouter un bouton déroulant pour le guide d'utilisation
    with st.expander("📘 Guide d'utilisation", expanded=False):
        st.markdown("""
        ### Visualisation des données
        - **Titre Principal** : "Visualisation des données"
        - **Description** : Cette section permet aux utilisateurs de visualiser les données concernant les bâtiments de la ville de Seattle, aux États-Unis.
        - **Affichage des Données** :
            - Tableau interactif affichant les informations sur 7104 bâtiments et leurs émissions de CO2.
        - **Options de Visualisation** :
            - **Statistiques Univariées** :
                - Sélectionnez une variable quantitative (ex. : surface des bâtiments) pour visualiser un histogramme et des statistiques descriptives (moyenne, écart-type, etc.).
            - **Statistiques Bivariées** :
                - Analysez la corrélation entre deux variables quantitatives avec un nuage de points.
                - Explorez les relations entre une variable qualitative et une quantitative via des diagrammes en barres ou des tableaux croisés.
            - **Carte Interactive** :
                - Visualisez la répartition géographique des bâtiments avec des marqueurs interactifs.

        ### Prédiction des émissions de CO2
        - **Titre Principal** : "Prédiction de la consommation de CO2"
        - **Description** : Faites des prédictions sur les émissions de CO2 en fonction des caractéristiques des bâtiments de Seattle.
        - **Prédiction Unique** :
            - Remplissez un formulaire avec des informations spécifiques (ex. : surface du bâtiment, nombre d'étages, âge, etc.).
            - Appuyez sur le bouton pour obtenir une prédiction immédiate des émissions de CO2.
        - **Prédictions Multiples** :
            - Téléchargez un fichier Excel contenant les caractéristiques de plusieurs bâtiments.
            - Lancez une prédiction groupée pour analyser les émissions de plusieurs bâtiments en une seule fois.
        """, unsafe_allow_html=True)

        # Ajouter un bouton de téléchargement pour le modèle Excel
        st.markdown("#### Téléchargez le modèle Excel pour les prédictions multiples :")
        st.markdown("[Télécharger le modèle Excel](https://github.com/Awoutokoffisamson/machine_learning/blob/main/modele.xlsx?raw=true)", unsafe_allow_html=True)

    ### Résumé des Variables de Prédiction
    st.markdown("""
    Voici un récapitulatif des variables utilisées pour les prédictions :
    | Nom en Anglais                         | Nom en Français                          |
    |----------------------------------------|------------------------------------------|
    | NumberofFloors                         | Nombre d'étages                          |
    | NumberofBuildings                      | Nombre de bâtiments                      |
    | PropertyGFABuilding(s)                 | Surface totale du bâtiment (GFA)         |
    | PropertyGFAParking                     | Surface du parking (GFA)                 |
    | ENERGYSTARScore                        | Score ENERGY STAR                        |
    | SiteEUIWN(kBtu/sf)                     | Site EUI (kBtu/sf)                       |
    | Electricity(kBtu)                      | Consommation d'électricité (kBtu)        |
    | NaturalGas(kBtu)                       | Consommation de gaz naturel (kBtu)       |
    | BuildingAge                            | Âge du bâtiment                          |
    """, unsafe_allow_html=True)

# Appel de la fonction pour afficher l'accueil
if __name__ == "__main__":
    afficher_accueil()
