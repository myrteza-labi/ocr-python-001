import requests
from bs4 import BeautifulSoup

# Remplacez l'URL par celle de la page produit que vous souhaitez scraper
url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"

# Envoyer une requête GET à l'URL
response = requests.get(url)

# Vérifier si la requête a réussi (statut 200)
if response.status_code == 200:
    # Utiliser BeautifulSoup pour analyser le contenu HTML de la page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extraire l'URL de la page produit
    product_page_url = url

    # Afficher l'URL de la page produit
    print("URL de la page produit:", product_page_url)

else:
    print("La requête a échoué avec le code d'état:", response.status_code)
