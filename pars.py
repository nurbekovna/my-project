from bs4 import BeautifulSoup
import requests

def get_url_text(url):
    response = requests.get(url=url)
    if response.status_code == 200:
        return response.text
    return None

def get_links(html):
    soup = BeautifulSoup(markup=html, features="html.parser")
    listing = soup.find("div", {"class": "listings-wrapper"})
    publications = listing.find_all("div", {"class": "listing row-5"})
    urls = []
    for publication in publications:
        url = publication.find("a").get("href")
        urls.append("https://www.bazar.kg"+url)

    return urls

def get_data(html):
    soup = BeautifulSoup(markup=html, features="html.parser")
    title = soup.find("div", {"class": "left"}).find("h1").text.strip()
    price = soup.find("span", {"class": "main"}).text.strip()
    priceD = soup.find("span", {"class": "sub"}).text.strip()
    description = soup.find("p", {"class": "description"}).text.strip()
    dop_r = soup.find("div", {"class": "info-row"}).find("div", {"class": "label"}).text.strip()
    dop_inf = soup.find("div", {"class": "info-row"}).find("div", {"class": "info"}).text.strip()
    data = {
        "title": title,
        "price_soms": price,
        "price_dollars": priceD,
        "description": description,
        dop_r: dop_inf
    }
    return data
