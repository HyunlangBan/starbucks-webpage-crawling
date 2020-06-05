from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import csv

csv_filename = "starbucks.csv"
csv_open = open(csv_filename, '+w', encoding='utf-8')
csv_write = csv.writer(csv_open)
csv_write.writerow(('Drink', 'Image'))

chrome_path = "/usr/bin/chromedriver"
driver = webdriver.Chrome(chrome_path)

driver.get("https://www.starbucks.co.kr/menu/drink_list.do")
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

img_tags = soup.select('.goDrinkView > img')
#imgs = img_links[0]['src']
# tag로 받아와서 바로 또 bs의 메소드를 적용할 수 있다.

#title = soup.select('.goDrinkView > img')['alt']

#print(imgs)
#print(title)
#print(drinks)

for tag in img_tags:
    img_link = tag['src']
#    print(f'img link: {img_link}')
    coffee = tag['alt']
#   print(f'coffee: {coffee}')
    csv_write.writerow((coffee, img_link))

csv_open.close()


