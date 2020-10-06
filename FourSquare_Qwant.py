
#Importation des packages requis :
#region
from scipy.integrate import quad
from geopy.geocoders import Nominatim

import json                         #Exploration des données
import requests                     #Requêtage de l'application
import os                           #Fonctions de base de python
import pandas as pd                 #Utilisations des Dataframes
import datetime                     #Utilisations du Datetime pour now()
import scipy.stats                  #Utilisation de la courbe de Gauss
import numpy as np      


from collections import Counter     #conteur
from string import punctuation      #Pour éviter d'avoir des ponctuation dans les mots fréquents


import seaborn as sns               #module pour le graph
import matplotlib.pyplot as plt     #"Idem"
import nltk
import qwant                        #importation de qwant (pip install qwant/import qwant)
#import spacy                       #Utilisation du framework spacy pour la fréquence
#nlp = spacy.load("en_core_web_lg")
from stop_words import get_stop_words #Liste de mots banaux




                                        ###############################################################################
                                        #                                                                             #
                                        #                                                                             #
                                        #                                                                             #
                                        #                              API Foursquare                                 #
                                        #                                                                             #
                                        #                                                                             #
                                        #                                                                             #
                                        ###############################################################################





#endregion

#Url de connexion à l'API
url = 'https://api.foursquare.com/v2/venues/explore'

#Permet d'utiliser le temps dans le programme
current_time = datetime.datetime.now()

#On affiches toutes les lignes de dataframes pour éviter les raccourcis : 
pd.set_option('display.max_rows', 500)

#Paramétrage de l'API :
#region
#   # # # # # # # # # # # # # # # # # # # # # #
#Définition du paramétrage de l'API #
#Entrée : Latittude et Longitude : Int #
#Paramètres : l'ID Client (Qui utilise l'API) : String #
#           - Mot de Passe du client : String #
#           - La date d'actualisation : DateTime #
#           - Les coordonées GPS : String #
#           - La demande : String # #
#Sortie : Les Paramètres de l'API #
#Description : Permet de requêter Foursquare avec toutes les données
#necessaires #
#   # # # # # # # # # # # # # # # # # # # # # #
def customParams(latitude, longitude, besoin):
    #Si le mois est inférieur à 10, on rajoute un "0" dans la date pour être
    #conforme à la norme foursquare
    if int(current_time.month) < 10 :
        params = dict(client_id='NCY3QDJ2ZNXNNQNQVQBVLQO44JBMGTYL3KQSHQBT3WFVIOPW',
        client_secret='R3CCH5GJHTAS3IAQUV1H2X5NJT20TNTIJDW5QXMBEYMSUW35',

        v = str(current_time.year) + str(0) + str(current_time.month) + str(0) + str(current_time.day),

        #Paramètres entrés par l'utilisateurs
        ll= str(latitude) + ',' + str(longitude),
        query='coffee',
    
        #Limite de données
        limit=75)
        return params
    else :
        params = dict(client_id='NCY3QDJ2ZNXNNQNQVQBVLQO44JBMGTYL3KQSHQBT3WFVIOPW',
        client_secret='R3CCH5GJHTAS3IAQUV1H2X5NJT20TNTIJDW5QXMBEYMSUW35',

        v = str(current_time.year) + str(current_time.month) + str(current_time.day),

        #Paramètres entrés par l'utilisateurs
        ll= str(latitude) + ',' + str(longitude),
        query=besoin,
    
        #Limitation du nombre de données
        limit=10)
        return params

#Paramètres manuels :
latitude = 45.18409801691486
longitude = 0.7175019022911489


print("Obtention des données...")
#Lieu Recherché Authentique
print("     > Locales ..................................................")
df0 = orgaData(latitude, longitude, "restaurants")
print("     > Locales .................................................. : OK")

#Échantillonage sur 30km
#~Échantillon Nord
print("     > Echantillon Nord .........................................")
df1 = orgaData(latitude + 0.25, longitude, "restaurants")
print("     > Echantillon Nord ......................................... : OK")


#~Échantillon Sud Est
print("     > Echantillon Sud-Est ......................................")
df2 = orgaData(latitude - 0.2, longitude + 0.2, "restaurants")
print("     > Echantillon Sud-Est ...................................... : OK")

#~Échantillon Sud Ouest
print("     > Echantillon Sud-Ouest ....................................")
df3 = orgaData(latitude - 0.2, longitude - 0.2, "restaurants")
print("     > Echantillon Sud-Ouest .................................... : OK")

#Échantillonage sur 60km
#~Échantillon Sud
print("     > Echantillon Sud+ .........................................")
df4 = orgaData(latitude - 0.55 , longitude, "restaurants")
print("     > Echantillon Sud+ ......................................... : OK")

#~Échantillon Nord-Est
print("     > Echantillon Nord-Est+ ....................................")
df5 = orgaData(latitude + 0.5, longitude + 0.5, "restaurants")
print("     > Echantillon Nord-Est+ .................................... : OK")

#~Échantillon Nord-Ouest
print("     > Echantillon Nord-Ouest+ ..................................")
df6 = orgaData(latitude + 0.5, longitude - 0.5, "restaurants")
print("     > Echantillon Nord-Ouest+ .................................. : OK")

#Affichage : 
print ("Données locales :\n")
print(df0)
print("\n-------------------------------------------------------------")
print ("Données échantillonés N°1 (Restaurants) :\n")
print(df1)
print("\n-------------------------------------------------------------")
print ("Données échantillonés N°2 (Restaurants) :\n")
print(df2)
print("\n-------------------------------------------------------------")
print ("Données échantillonés N°3 (Restaurants) :\n")
print(df3)
print("\n-------------------------------------------------------------")
print ("Données échantillonés N°4 (Restaurants) :\n")
print(df4)
print("\n-------------------------------------------------------------")
print ("Données échantillonés N°5 (Restaurants) :\n")
print(df5)
print("\n-------------------------------------------------------------")
print ("Données échantillonés N°6 (Restaurants) :\n")
print(df6)








ville = df0.loc[0,"Ville"]

print(ville)

#Récupération des mots avec un score = 0


dfmscore0 = dfms.loc[ dfms['score']==0,]


motscles = ""
for x in dfmscore0['mots'][0:1] :           
    motscles = motscles + ' ' + x

print("\n-------------------------------------------------------------")
print("Mots spécifiques du lieu: \n")
print(motscles)

###################### ICI NOUS AVONS LE MOT RENTRER PAR L'UTILISATEUR  ############################################



mot_utilisateur = "recettes"

resultat1 = qwant.items(motscles+' '+ville+' '+ mot_utilisateur)[1]['url']    # Pour récupérer seulement les urls
resultat2 = qwant.items(motscles+' '+ville+' '+ mot_utilisateur)[2]['url']
resultat3 = qwant.items(motscles+' '+ville+' '+ mot_utilisateur)[3]['url']


                                                            #                                                                            #
                                                            #                                                                            #
print(resultat1)                                            # Affiche les résultats des recherches de l'API QWANT                        #
print(resultat2)                                            #                                                                            #
print(resultat3)                                            #                                                                            #





