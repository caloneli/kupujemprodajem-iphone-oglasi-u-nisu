python
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url= 'https://www.kupujemprodajem.com/search.php?action=list&data%5Bpage%5D=1&data%5Bprev_keywords%5D=iphone+&data%5Blocation_id%5D=2&data%5Border%5D=posted+desc&submit%5Bsearch%5D=Tra%C5%BEi&dummy=name&data%5Bkeywords%5D=iphone+&data%5Bprice_from%5D=50&data%5Bcurrency%5D=eur'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll('div', class_='item clearfix')
container = containers [0]
ime = container.find('a', class_='adName').text
cena = container.find('span',class_='adPrice').text
filename="oglasi.csv"
import io
with io.open(filename, 'w',encoding="utf-8") as f:
    headers= "ime, cena"
    f.write(headers + "\n")
    for container in containers:
        ime = container.find('a', class_='adName').text
        ime =  ime.replace("\n\t\t\t\t\t\t\t\t","")
        cena = container.find('span',class_='adPrice').text
        cena= cena.replace("\n\t\t\t\t\t\t","")
        f.write(ime + "," +  cena.replace("\xa0€\n\t\t\t\t\t"," ") + "\n")
    f.close()
