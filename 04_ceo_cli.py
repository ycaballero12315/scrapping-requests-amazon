from bs4 import BeautifulSoup
import requests as req
from urllib.parse import urljoin
import argparse

parser = argparse.ArgumentParser(description='Webs Scraping to check seo for giving to url')
parser.add_argument("url", type=str, help='The url of the site you want to scrape and check')
args = parser.parse_args()
url = args.url

response = req.get(url)

if response.status_code == 200:
    print('Peticion exitosa')
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f'\033[34mRevisando la pagina: {url}\033[0m')
    print('\n\033[34m SEO Basico: \033[0m')

    if titulo := soup.find('a', title="Montevideo Portal").get('title'):
        print(f'\033[45m El titulo de la pagina es: {titulo}\033[0m')
        if len(titulo) < 75:
            print('\033[42mEl titulo tiene un tamanno correcto \033[0m')
        else:
            print('\033[41mEl titulo es muy largo033[0m')

    if titulos := [titulo.text for titulo in soup.find_all('h1')]:
        print
        if len(titulos) >1:
            print('\033[101m Se encontro mas de un titulo en la pagina \033[0m')
            for t in titulos:
                print(t)
        else:
            print('\033[102m Correcto encontramos solo un titulo <h1>! \033[0m')
    else:
        print('\033[101m Error no se encuentran titulos \033[0m')




# 'https://www.montevideo.com.uy/Noticias/Esta-tarde-comienza-oficialmente-la-primavera-2025-y-al-parecer-sera-de-las-buenas-uc937301')