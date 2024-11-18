import requests
from bs4 import BeautifulSoup

def download_url_and_get_all_hrefs(url):
    """
    Funkce stáhne URL předanou v parametru url pomocí volání response = requests.get(),
    zkontroluje návratový kód response.status_code, který musí být 200,
    pokud ano, najde ve staženém obsahu stránky response.content všechny odkazy <a href="url">odkaz</a>
    a z nich načte URL, které vrátí jako seznam pomocí return.
    """
    hrefs = []
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        for a in soup.find_all('a', href=True):
            link = a['href']   
            if not link.startswith('http'):
                if link.startswith('/'):
                    link = url + link
                else:
                    link = url + '/' + link 
            hrefs.append(link)
    else:
        print(f"Chyba: Status kód není 200. Vrátilo se: {response.status_code}")
    return hrefs


if __name__ == "__main__":
    try:
        url = "https://www.jcu.cz/"
        links = download_url_and_get_all_hrefs(url)
        print(links)
    except IndexError:
        print("Nebyla zadána žádná URL adresa.")
    except Exception as e:
        print(f"Program skončil chybou: {e}")
