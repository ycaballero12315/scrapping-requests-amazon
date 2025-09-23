import requests
import re as re

html:str = ''

url:str = 'https://www.apple.com/es/shop/buy-mac/macbook-air'

response = requests.get(url)

encontrado = re.search(r'(.*?)', response.text)
if encontrado:
    print(f'Encontrado con search: {encontrado.group(1)}')

patter_title = r'<title>(.*?)</title>'

if response.status_code == 200:
    print('Exitos!!!')
    html = response.text
    pattern = r'<span class="rc-prices-fullprice">(.*?)</span>' 

    mach_title = re.search(patter_title, html)

    if mach_title:
        print(f'el titulo de la pagina es {mach_title.group(1)}')

    mach_patter = re.findall(pattern, html, re.S)

    if mach_patter:
        for elem in mach_patter[:3]:
            precio = elem.strip()
            precio = ''.join(c for c in precio if c.isdigit() or c in '.,')
            precio = precio.replace('$', ' ').replace('€', ' ').replace(',', ' ')
            print(precio.upper())
            
    else:
        patt = f'<span[^>]*class="[^"]*price[^"]*"[^>]*>([^<]+)</span>'
        mach_patter_other = re.findall(patt,html, re.S)
        print('Aplicando otros patrones')
        if mach_patter_other:
            for elem in mach_patter_other[:5]:
                print(elem.strip())

else:
    print("Error en la carga de la requests")


