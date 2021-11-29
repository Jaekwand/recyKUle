import requests
from bs4 import BeautifulSoup

# first_page = True
# has_next = True
# while has_next or first_page:
#     first_page = False
# page_idx = 1
# url = f"http://kartprice.net/price/list/?search_val=%2522%25EA%25B0%2595%25EC%2584%25B8%25ED%2599%25A9%2522&type=works&sort=trade&sorttype=desc&artchk=Y&workchk=Y&page={page_idx}&prefix="
# res = requests.get(url)
# res.raise_for_status()
#
# soup = BeautifulSoup(res.text, "lxml")

url = "http://kartprice.net/price/list/?search_val=%2522%25EA%25B0%2595%25EC%2584%25B8%25ED%2599%25A9%2522&type=works&sort=trade&sorttype=desc&artchk=Y&workchk=Y&page=&prefix="
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

nums = soup.find_all("td", attrs={"class":"num"})
for num in nums:
    print(num.get_text())

pics = soup.find_all("td", attrs={"class":"pic"})
for pic in pics:
    print(pic.img["src"])

titles = soup.find_all("td", attrs={"class":"title"})
for title in titles:
    print(title.p.get_text())


names = soup.find_all("td", attrs={"class":"name"})
for name in names:
    print(name.p.get_text())

names = soup.find_all("td", attrs={"class": "name"})
for name in names:
    yearsize = name.next_sibling.next_sibling
    year = (yearsize.select('p')[0]).get_text()
    print(year)

names = soup.find_all("td", attrs={"class": "name"})
for name in names:
    yearsize = name.next_sibling.next_sibling
    size = (yearsize.select('p')[-1]).get_text()
    print(size)

names = soup.find_all("td", attrs={"class": "name"})
for name in names:
    genretechnique = name.next_sibling.next_sibling.next_sibling.next_sibling
    genre = (genretechnique.select('p')[0]).get_text()
    print(genre)

names = soup.find_all("td", attrs={"class": "name"})
for name in names:
    genretechnique = name.next_sibling.next_sibling.next_sibling.next_sibling
    technique = (genretechnique.select('p')[-1]).get_text()
    print(technique)

names = soup.find_all("td", attrs={"class": "name"})
for name in names:
    auctiontradedate = name.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
    auction = (auctiontradedate.select('p')[0]).get_text()
    print(auction)

names = soup.find_all("td", attrs={"class": "name"})
for name in names:
    auctiontradedate = name.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
    tradedate = (auctiontradedate.select('p')[-1]).get_text()
    print(tradedate)

prices = soup.find_all("td", attrs={"class":"money"})
for price in prices:
    print(price.get_text())