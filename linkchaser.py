import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

certs = ssl.create_default_context()
certs.check_hostname = False
certs.verify_mode = ssl.CERT_NONE

url = input('Enter a link: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
ncount = 0
while ncount != (count + 1):
    try:
        html = urllib.request.urlopen(url, context=certs).read()
    except: 
        print('Cannot open link:', url)
        exit()
    print('Retrieving:', url)
    soup = BeautifulSoup(html, 'html.parser')
    npos = 1
    tags = soup('a')
    for tag in tags:
        if npos == position:
            url = tag.get('href', None)
            ncount += 1
            break
        npos += 1
