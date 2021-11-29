import requests
from bs4 import BeautifulSoup

url = "http://kartprice.net/proc/abc_sort.php?word=all"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

artists = soup.find_all("a")

#artist name
for artist in artists:
    artist_name = artist.get_text()
    print(artist_name)

#artist url
for artist in artists:
    artist_link = "http://kartprice.net" + artist["href"]
    print(artist_link)