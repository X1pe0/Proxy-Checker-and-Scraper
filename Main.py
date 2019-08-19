import urllib2, socket
import urllib, urllib2
import time, datetime
import threading, Queue
import re
import StringIO, gzip
import sys
#Your Welcome. I'm sick of these bs pay for this trash vb.net proxy checker. This does everything. Scrapes and Checks and exports in a TXT file. Created by W0rMz000. Sharing is caring. Edit as you wish. 
debug = False


def bug(line):
	if debug == True:
		print "Debug:: " + line

def queueThread():
	global proxyCount
	ts = time.time()
	dt = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
	print 'Saving...'
	fout = open("scrape.txt", "w")

	while not workerQueue.empty():
		fout.write(workerQueue.get() + "\n")
		proxyCount+=1
	fout.close()

def proxylist():
	print "Grabbing..."
	primary_url = "http://proxy-list.org/english/index.php?p="
	urls = []
	for i in range(1, 11):
		urls.append(primary_url + str(i))

	for url in urls:
		try:
			bug("grabbing " + "'" + url + "'")
			opener = urllib2.build_opener()
			opener.addheaders = [('Host', 'www.proxylisty.com'),
								 ('Connection', 'keep-alive'),
								 ('Cache-Control', 'max-age=0'),
								 ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
								 ('Upgrade-Insecure-Requests', '1'),
								 ('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'),
								 ('Referer', 'https://www.google.co.za/'),
								 ('Accept-Encoding','gzip, deflate, sdch'),
								 ('Accept-Language','en-US,en;q=0.8')]

			response = opener.open(url, timeout=10)
			compressedFile = StringIO.StringIO()
			compressedFile.write(response.read())
			compressedFile.seek(0)
			decompessedFile = gzip.GzipFile(fileobj=compressedFile, mode='rb')
			html = decompessedFile.read()

			templs = re.findall(r'<li class="proxy">([1-99999].*)?</li>', html)
			for line in templs:
				workerQueue.put(line)
				bug("proxylist() " + line)

		except Exception, e:
			if e.message == " ":
				bug(e.message)
				bug("Failed to grab " + "'" + url + "'")
			else:
				bug("Failed to grab " + "'" + url + "'")
		

def usproxy():
	
	templs = []
	url = "http://www.us-proxy.org/"
	try:
		bug("grabbing " + "'" + url + "'")
		opener = urllib2.build_opener()
		opener.addheaders = [('Host', 'www.proxylisty.com'),
							('Connection', 'keep-alive'),
							('Cache-Control', 'max-age=0'),
							('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
							('Upgrade-Insecure-Requests', '1'),
							('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'),
							('Referer', 'https://www.google.co.za/'),
							('Accept-Encoding','gzip, deflate, sdch'),
							('Accept-Language','en-US,en;q=0.8')]

		response = opener.open(url, timeout=10)
		html = response.read()

		templs = re.findall(r'<tr><td>(.*?)</td><td>', html)
		templs2 = re.findall(r'</td><td>[1-99999].*?</td><td>', html)

		for i in range(len(templs)):
			temp = templs[i] + ":" + templs2[i].replace('</td><td>', '')
			workerQueue.put(temp)
			bug("usproxy() " + templs[i] + ":" + templs2[i].replace('</td><td>', ''))

	except Exception, e:
		if e.message == " ":
			bug(e.message)
			bug("Failed to grab " + "'" + url + "'")
		else:
			bug("Failed to grab " + "'" + url + "'")


def freeproxylist():

	url = "http://free-proxy-list.net/"
	try:
		bug("grabbing " + "'" + url + "'")
		opener = urllib2.build_opener()
		opener.addheaders = [('Host', 'www.proxylisty.com'),
							('Connection', 'keep-alive'),
							('Cache-Control', 'max-age=0'),
							('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
							('Upgrade-Insecure-Requests', '1'),
							('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'),
							('Referer', 'https://www.google.co.za/'),
							('Accept-Encoding','gzip, deflate, sdch'),
							('Accept-Language','en-US,en;q=0.8')]

		response = opener.open(url, timeout=10)
		html = response.read()

		templs = re.findall(r'<tr><td>(.*?)</td><td>', html)
		templs2 = re.findall(r'</td><td>[1-99999].*?</td><td>', html)

		for i in range(len(templs)):
			workerQueue.put(templs[i] + ":" + templs2[i].replace('</td><td>', ''))
			bug("freeproxylist() " + templs[i] + ":" + templs2[i].replace('</td><td>', ''))

	except Exception, e:
		if e.message == " ":
			bug(e.message)
			bug("Failed to grab " + "'" + url + "'")
		else:
			bug("Failed to grab " + "'" + url + "'")


def coolproxy():
	
	primary_url = "http://www.cool-proxy.net/proxies/http_proxy_list/sort:score/direction:desc/page:"
	urls = []
	for i in range(1, 13):
		urls.append(primary_url + str(i))

	for url in urls:
		bug("grabbing " + "'" + url + "'")
		try:
			opener = urllib2.build_opener()
			opener.addheaders = [('Host', 'www.proxylisty.com'),
								 ('Connection', 'keep-alive'),
								 ('Cache-Control', 'max-age=0'),
								 ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
								 ('Upgrade-Insecure-Requests', '1'),
								 ('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'),
								 ('Referer', 'https://www.google.co.za/'),
								 ('Accept-Encoding','gzip, deflate, sdch'),
								 ('Accept-Language','en-US,en;q=0.8')]

			response = opener.open(url, timeout=10)
			compressedFile = StringIO.StringIO()
			compressedFile.write(response.read())
			compressedFile.seek(0)
			decompessedFile = gzip.GzipFile(fileobj=compressedFile, mode='rb')
			html = decompessedFile.read()

			templs = re.findall(r'str_rot13(.*?)</script>', html)
			templs2 = re.findall(r'<td>[1-99999].*?</td>', html)

			for i in range(len(templs)):
				temp = templs[i].replace('("', '')#remove front of string
				temp = temp.replace('")))', '')#remove back of string
				temp = temp.decode('rot13').decode('base64')#decode from rot13 then from base64
				workerQueue.put(temp + templs2[i].replace('<td>', ':').replace('</td>', ''))
				bug("coolproxy() " + temp + templs2[i].replace('<td>', ':').replace('</td>', ''))
		
		except Exception, e:
			if e.message == " ":
				bug(e.message)
				bug("Failed to grab " + "'" + url + "'")
			else:
				bug("Failed to grab " + "'" + url + "'")


def proxylisty():

	primary_url = "http://www.proxylisty.com/ip-proxylist-"
	urls = []
	for i in range(1, 68):
		urls.append(primary_url + str(i))

	for url in urls:
		try:
			bug("grabbing " + "'" + url + "'")
			opener = urllib2.build_opener()
			opener.addheaders = [('Host', 'www.proxylisty.com'),
								 ('Connection', 'keep-alive'),
								 ('Cache-Control', 'max-age=0'),
								 ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
								 ('Upgrade-Insecure-Requests', '1'),
								 ('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'),
								 ('Referer', 'https://www.google.co.za/'),
								 ('Accept-Encoding','gzip, deflate, sdch'),
								 ('Accept-Language','en-US,en;q=0.8')]

			response = opener.open(url, timeout=10)
			compressedFile = StringIO.StringIO()
			compressedFile.write(response.read())
			compressedFile.seek(0)
			decompessedFile = gzip.GzipFile(fileobj=compressedFile, mode='rb')
			html = decompessedFile.read()

			templs = re.findall(r'<tr>\n<td>(.*?)</td>', html)
			templs2 = re.findall(r'com/port/(.*?)-ip-list', html)

			for i in range(len(templs)):
				workerQueue.put(templs[i] + ":" + templs2[i])
				bug("proxylisty() " + templs[i] + ":" + templs2[i])

		except Exception, e:
			if e.message == " ":
				bug(e.message)
				bug("Failed to grab " + "'" + url + "'")
			else:
				bug("Failed to grab " + "'" + url + "'")


if __name__ == "__main__":
	
	print "Starting Proxy Scraper...\n"

	proxyCount = 0
	workerQueue = Queue.Queue()
	tQueueThread = threading.Thread(target=queueThread)
	tQueueThread.deamon = True


	tProxylist = threading.Thread(target=proxylist)
	tProxylist.deamon = True

	tUsproxy = threading.Thread(target=usproxy)
	tUsproxy.deamon = True

	tFreeproxylist = threading.Thread(target=freeproxylist)
	tFreeproxylist.deamon = True

	tCoolproxy = threading.Thread(target=coolproxy)
	tCoolproxy.deamon = True


	
	tProxylisty = threading.Thread(target=proxylisty)
	tProxylisty.deamon = True

	tProxylist.start()
	time.sleep(.500)
	tUsproxy.start()
	time.sleep(.500)
	tFreeproxylist.start()
	time.sleep(.500)
	tCoolproxy.start()
	time.sleep(.500)

	tProxylisty.start()

	time.sleep(2)
	print "\nPlease wait..."

	tProxylist.join()
	tUsproxy.join()
	tFreeproxylist.join()
	tCoolproxy.join()

	tProxylisty.join()

	if not workerQueue.empty():
		tQueueThread.start()
		tQueueThread.join()
		print "Saved to file!\n"
		print "Proxies found: " + str(proxyCount)
	else:
		print "Could not scrape any proxies!"

print "Checking..."
time.sleep(2)
text_file = open("Working.txt", "w")
text_file.write("")
text_file.close()

socket.setdefaulttimeout(.4)
with open('scrape.txt') as f:
    proxyList = f.readlines()
# read the list of proxy IPs in proxyList
#proxyList = ['172.30.1.1:8080', '172.30.3.3:8080'] # there are two sample proxy ip

def is_bad_proxy(pip):    
    try:        
        proxy_handler = urllib2.ProxyHandler({'http': pip})        
        opener = urllib2.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib2.install_opener(opener)        
        req=urllib2.Request('http://www.google.com')  # change the url address here
        sock=urllib2.urlopen(req)
    except urllib2.HTTPError, e:        
        #print 'Error code: ', e.code
        return e.code
    except Exception, detail:

        #print "ERROR:", detail
        return 1
    return 0

for item in proxyList:
    if is_bad_proxy(item):
        None
    else:
        print item 
	text_file = open("Working.txt", "a+")
	text_file.write(item)
	text_file.close()
