from bs4 import BeautifulSoup
import urllib.request

# Helpers
def get_soup(path):
	#page = urllib.request.urlopen('http://services.runescape.com/m=hiscore/ranking?table=0&category_type=0&time_filter=0&date=1519066080774&user=zezima')
	page = open(path, "r")
	soup = BeautifulSoup(page.read(), 'html.parser')
	page.close()
	return soup

def get_elem_remove_word(element, tag, class_, remove_word):
	return element.find(tag, class_=class_).getText().strip()[len(remove_word):].strip()


data = []

# Top 2018 Startups
# https://www.top100startup.ch/index.cfm?CFID=49993854&CFTOKEN=e3e36c38c83093d-A97ED65E-952A-95B0-009A171CE2CC1B25&page=136340&profilesEntry=1
def get_top100():
	soup = get_soup("../static/top100.html")
	ul = soup.findAll("ul", class_="table-top100")[0]
	lis = ul.findAll("li")

	results = []
	for li in lis:
		name = get_elem_remove_word(li, "span", "col-star", "Startup")
		if name == "": continue

		results.append({
			"name": name,
			"description": get_elem_remove_word(li, "span", "col-desc", "Description"),
			"link": "",
			"city": get_elem_remove_word(li, "span", "col-head", "Headquarter"),
			"category": get_elem_remove_word(li, "span", "col-cate", "Category")
			})

	return results

# https://angel.co/zurich 
def get_angel_zurich():
	soup = get_soup("angelco.html")
	maindiv = soup.find("div", class_="with_data")
	divs = maindiv.findAll("div", class_="dts27")
	
	results = []
	for div in divs:

		link = div.find("a", class_="startup-link")

		print(div)
		results.append({
			"name": get_elem_remove_word(div, "div", "name", ""),
			"description": "",
			"link": ""
			})

	return results

# https://de.glassdoor.ch/Bewertungen/schweiz-bewertungen-SRCH_IL.0,7_IN226.htm 
def get_glassdoor():
	soup = get_soup("glassdoor_1.html")
	return []


#data += get_top100()
data += get_angel_zurich()
data += get_glassdoor()


print(data[0])
print(data[1])
print(data[2])