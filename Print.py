from bs4 import *
import requests
import time
def updates(a,b):
	for i in range(len(a)):
		print(a[i].get_text())
		print(b[i].get_text())

while True:
	r=requests.get("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")
	doc=r.text
	soup=BeautifulSoup(doc,'html.parser')
	p=soup.find_all('description')[1:]
	q=soup.find_all('title')[2:]
	updates(q,p)
	time.sleep(5)
	print('\n \n \n \n \n \n ')
