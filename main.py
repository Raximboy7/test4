# def foiz(x: int, y: int):
#     return x * y / 100
#
# def soz(a: str, b : int):
#     print(a * b)
#
# def qoshish(x, y):
#     print(x + y)
#
# def ayirish(x, y):
#     print(x - y)
#
# def daraja(x, y):
#     print(x ** y)
#
# def foiz2(a, b):
#     print(a / b * 100)
#
# def bolish(a, b):
#     print(a / b)
#
# def qoshiq2(a,b):
#     print(a+b)
#
# def qoldiq(a, b):
#     print(a % b)
#
# def bolish2(son: 10):
#     print(son)
#
# print(foiz(98, 30))
# soz('salom', 3)
# ayirish(34, 40)
#
import requests
from bs4 import BeautifulSoup
import json


res = requests.get('https://qalampir.uz/news/category/olam')
soup = BeautifulSoup(res.text, 'html.parser')
box = soup.find('div', class_='row g-4')
products = box.find_all('div', class_='col-lg-4 col-md-6')
data = []
for product in products:
    title = product.find('p', class_='news-card-content-text').get_text()
    link = 'https://qalampir.uz' + product.find('a')['href']
    img = product.find('img')['src']
    data.append({
        'title':title,
        'link':link,
        'img':img
    })
with open('qalampir`1.json', mode='w', encoding='utf-8') as file:
    json.dump(data,file, indent=4, ensure_ascii=False)





















