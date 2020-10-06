from bs4 import BeautifulSoup #import de bs4.BeautifulSoup (pip install bs4)
from urllib import request #import de urllib.request

#Dans cette exemple, nous allons scrapper, récupérer le contenu de la page de Mr.Massé (Aide à l'utilisation de R)
#:Exécuter le programme

def main(): #fonction principale
    soup = get_parsed_page("https://sites.google.com/site/rgraphiques/home?authuser=0") #récupération de la page parsée (url de la page) 
    print_post_titles(soup) #affichage des titres des posts
    print('') #pour un retour à la ligne entre les titres et les catégories
    print_post_categories(soup) #affichage des catégories des posts

    print('') #pour un retour à la ligne entre les catégories et le texte
    print_post_text(soup) #affichage du texte de la page

def get_parsed_page(url): #fonction qui retourne une page parsée à partir d'une url
    with request.urlopen(url) as page:
        html = page.read()
    return BeautifulSoup(html, 'html.parser') #parse la page avec BeautifulSoup

def print_post_titles(soup):
    print('Titles:')
    post_titles = soup.find_all('h1') #find_all retourne toutes les occurences, utiliser "find" pour n'en récupérer qu'une seule
    post_titles2 = soup.find_all('h2')
    print_html_elements_text(post_titles)
    print_html_elements_text(post_titles2)

def print_post_categories(soup):
    print('Categories:')
    post_categories = set(soup.find_all('a')) #utilisation d'un set pour ne pas avoir de doublons
    print_html_elements_text(post_categories)

def print_post_text(soup):
    print('Text:')
    post_text = soup.find_all('p') #find_all retourne toutes les occurences, utiliser "find" pour n'en récupérer qu'une seule
    print_html_elements_text(post_text)

def print_html_elements_text(html_elements):
    for html_element in html_elements:
        print(html_element.getText()) #utilisation de getText() pour récupérer le texte affiché

main()