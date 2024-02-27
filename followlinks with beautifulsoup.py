import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup
import ssl
import re


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the link: ')
position = int(input('Enter the position of the word you want: '))
repeatnumbers: int(input('How many times do you want to repeat the loop? '))
current_repeat = 0

def html_parse(url):
    fhand = urllib.request.urlopen(url)
    soup = BeautifulSoup(fhand, 'html.parser')
    tags = soup ('href')
    return tags

while current_repeat<repeatnumbers:
    print ("Retrieving", url)


#values = soup('href')
#print (values)
#for value in values:
#   print (value[2])




#html = urlopen(url, context=ctx).read()
#soup = BeautifulSoup(html, "html.parser")