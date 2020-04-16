from bs4 import BeautifulSoup
import requests
import os
from colorama import Fore, Style


def menu():
	user_url = input()
	if "dir" in user_url:
		create_dir(user_url)
	elif "." in user_url:
		try:
			printer(user_url)
			writer(user_url)
		except requests.exceptions.ConnectionError:
			print("input valid url")
			return menu()
	elif user_url == "exit":
		exit(0)
	return menu()


def printer(url):
	page = requests.get("http://" + url)
	soup = BeautifulSoup(page.content, 'html.parser')
	for a in soup.find_all(g):
		if a.name == "li":
			print(Fore.BLUE + a.get_text() + Style.RESET_ALL)
		elif a.name != 'li':
			print(a.get_text())


def create_dir(user_url):
	try:
		os.mkdir(user_url)
		global dir_name
		dir_name = user_url
	except FileExistsError:
		print("error")
		return menu()


def writer(user_url):
	page = requests.get("http://" + user_url)
	soup = BeautifulSoup(page.content, 'html.parser')
	if not os.path.exists(dir_name):
		os.mkdir(dir_name)
		with open('{}/{}.txt'.format(dir_name, page_url(user_url)), 'a') as f:
			for a in soup.find_all(g):
				f.write(a.get_text())
	else:
		with open('{}/{}.txt'.format(dir_name, page_url(user_url)), 'a') as f:
			for a in soup.find_all(g):
				f.write(a.get_text())
	history.append(user_url)


def page_url(user_url):
	# Return name url
	return user_url.rsplit(".").pop(0)


history = []
g = ['a', 'p', 'ul', 'ol', 'li']
dir_name = "tb_tabs"
menu()

