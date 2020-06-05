from selenium import webdriver
from bs4 import BeautifulSoup
import csv

csv_filename = 'menu_list2.csv'
csv_open = open(csv_filename, '+w', encoding='utf-8')
csv_write = csv.writer(csv_open)
csv_write.writerow(['Drinks', 'Descriptions', 'Images'])

chrome_path = '/usr/bin/chromedriver'
driver = webdriver.Chrome(chrome_path)
driver.get('https://www.starbucks.co.kr/menu/drink_list.do')

# 여기서부터 for문
MAX = 100 

for i in range(1,MAX):
	try:
		for j in range(1, MAX):
				try:
					drink = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[2]/div/dl/dd[1]/div[1]/dl/dd['+str(i)+']/ul/li['+str(j)+']/dl/dt/a/img')
				        # xpath를 보고 어느 부분을 변수로 바꾸어야할지가 관건이었다. 또한 변수를 설정한다고 해도 마지막이 어디인지 구할수가 없어서 exception을 사용하기로 했다.	
					drink.click()
					# 데이터 긁어오기
					detail = driver.page_source
					soup = BeautifulSoup(detail, 'html.parser')
					drink_name = soup.find('h4').text
					drink_desc = soup.find('p',{'class':'t1'}).getText()
					drink_img = soup.select('ul.product_thum img')
					img = drink_img[0]
					
					csv_write.writerow([drink_name, drink_desc, img['src']])
		#			print(img['src'])
		#			print(drink_desc)
		#			print(drink_name)
					driver.back()
				except Exception:
					break
	except Exception:
		break				
csv_open.close()
