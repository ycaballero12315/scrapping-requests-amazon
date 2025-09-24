from bs4 import BeautifulSoup
import requests as req
import json
from pathlib import Path
import re

path_json = Path('./data/price.json')

url:str = 'https://www.apple.com/es/shop/buy-mac/macbook-air'

Path('data').mkdir(exist_ok=True)

headers = {
    'User-Agent':'Mozilla/5.0 AppleWebKit/537.36 (KHTML,'
    ' like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) '
    'Chrome/140.0.0.0 Safari/537.36'
}
response = req.get(url, headers=headers)


precios = {}

if response.status_code == 200:
    print('Exitos!!!')
    soup = BeautifulSoup(response.text, 'html.parser')
    tags_title = soup.title
    # Buscar precio
    price = soup.find_all('span', class_='rc-prices-fullprice')

    for i, p in enumerate(price):
        price_text = p.text.strip()
        print(f'Original text: {price_text}')

        text_not_euro = p.text.replace('€', '').strip()
        print(f"Solo precio: {text_not_euro}")

        cleaning_price = text_not_euro.replace('.', '').replace(',', '').strip()
        print(f"Precio limpio: {cleaning_price}")

        precios[f'precio_{i+1}'] = float(cleaning_price)

    if tags_title:
        print(f'El title es {tags_title.string}')
    else:
        print('Algo fallo!')
    metas = tags_title.parent.find_all('meta')
else:
    print("Error en la carga de la requests")

with open("./data/price.json", 'w+') as file:
    json.dump(precios, file, indent=2)

def devolver_json():
    if path_json.exists():
        with open('./data/price.json', 'r+') as file:
            parse_json = json.load(file)
    else:
        parse_json = {}
    return parse_json

def details_price():
    products = {}
    if details := soup.find_all('div', class_="rc-productbundle-details"):
        for i, det in enumerate(details):
            specs = []
            if list_title := det.find(class_="list-title"):
                for title in list_title.find_all(['img', 'small', 'sub']):
                    title.decompose()
                texto = list_title.get_text()

                if 'CPU' in texto:
                    cpu = re.search(r'CPU de ([\d\s]+núcleos)', texto)
                    if cpu:
                        specs.append(f'CPU: {cpu.group(1).strip()}')

                if 'GPU' in texto:
                    gpu = re.search(r'GPU de ([\d\s]+núcleos)', texto)
                    if gpu:
                        specs.append(f'GPU: {gpu.group(1).strip()}')

                if "memoria" in texto:
                    memoria = re.search(r'(\d+\s*GB) de memoria',texto)
                    if memoria:
                        specs.append(f'RAM: {memoria.group(1).strip()}')

                if 'almacenamiento' in texto:
                    almacenamiento = re.search(r'(\d+\s*GB) de almacenamiento', texto)
                    if almacenamiento:
                        specs.append(f'SSD: {almacenamiento.group(1).strip()}')

            price_clean = ''      
            if price := det.find(class_='rc-prices-fullprice'):
                price_clean = price.text.strip()

            products[f"producto_{i+1}"] = {
                'especificaciones': specs,
                'price': price_clean
            }
    return products

file_direct = './data/details.json'
def save_elemns():
    with open(file_direct, 'w+', encoding='utf-8') as f:
        json.dump(details_price(),f, indent=2, ensure_ascii=False)

save_elemns()
def show_clean_products():
    with open(file_direct, 'r+', encoding='utf-8') as f:
        products = json.load(f)
        for key, product in products.items():
            print(f'-----------{key}------------------------')
            print('Especificaciones: ')
            if isinstance(product['especificaciones'], list):
                for spec in product['especificaciones']:
                    print(f'-> {spec}')
            else:
                print(f"->>> {product['especificaciones']}")
            print(f"Precio: {product['price']}")

show_clean_products()

# def properties():
    # elems = {}
    # if soup:
        # if elem:= soup.find('div', class_ = "rc-productbundle-details"):
            # print(f"elementos contenidos: {len(elem)}")
            # for i, e in enumerate(elem):
                # elems.update({f'{i+1}': e})
        # return elems
    # if soup:
        # if elem:= soup.find('div', class_ = "rc-productbundle-details"):
            # print(f"elementos contenidos: {len(elem)}")
            # for i, e in enumerate(elem):
                # elems.update({f'{i+1}': e})
        # return elems
    # if soup:
        # if elem:= soup.find('div', class_ = "rc-productbundle-details"):
            # print(f"elementos contenidos: {len(elem)}")
            # for i, e in enumerate(elem):
                # elems.update({f'{i+1}': e})
        # return elems
    # if soup:
        # if elem:= soup.find('div', class_ = "rc-productbundle-details"):
            # print(f"elementos contenidos: {len(elem)}")
            # for i, e in enumerate(elem):
                # elems.update({f'{i+1}': e})
        # return elems
    # if soup:
        # if elem:= soup.find('div', class_ = "rc-productbundle-details"):
            # print(f"elementos contenidos: {len(elem)}")
            # for i, e in enumerate(elem):
                # elems.update({f'{i+1}': e})
        # return elems
    # if soup:
        # if elem:= soup.find('div', class_ = "rc-productbundle-details"):
            # print(f"elementos contenidos: {len(elem)}")
            # for i, e in enumerate(elem):
                # elems.update({f'{i+1}': e})
        # return elems
    # if soup:
        # if elem:= soup.find('div', class_ = "rc-productbundle-details"):
            # print(f"elementos contenidos: {len(elem)}")
            # for i, e in enumerate(elem):
                # elems.update({f'{i+1}': e})
        # return elems
    # if soup:
        # if elem:= soup.find('div', class_ = "rc-productbundle-details"):
            # print(f"elementos contenidos: {len(elem)}")
            # for i, e in enumerate(elem):
                # elems.update({f'{i+1}': e})
        # return elems
# 
# print(properties())



