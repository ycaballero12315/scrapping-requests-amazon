from bs4 import BeautifulSoup
import requests as req
from urllib.parse import urljoin
# import json
# from pathlib import Path
import re

# path_json = Path('./data/price.json')

# Path('data').mkdir(exist_ok=True)
# headers = {
#     'User-Agent':'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/131.0.0.0 Safari/537.36'
# }
def Scraping(url):
    response = req.get(url)

    if response.status_code == 200:
        print('Exitos!!!')
        soup = BeautifulSoup(response.text, 'html.parser')
        # enlaces = [urljoin(url,link.get('href')) for link in soup.find_all('a')]
        # print(enlaces)
        main_text = soup.find('main').get_text()
        print(main_text)

        opimage = soup.find('meta', property='og:image')
        print(opimage['content'])
        
Scraping('https://www.montevideo.com.uy/Noticias/Esta-tarde-comienza-oficialmente-la-primavera-2025-y-al-parecer-sera-de-las-buenas-uc937301')