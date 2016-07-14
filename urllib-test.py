import urllib3 as ulib
from bs4 import BeautifulSoup as bsoup

"""
this gets html from website and prettifies it into the terminal
"""

connectBuilder = ulib.PoolManager()

"""
r = http.request('GET', 'http://httpbin.org/robots.txt')
r.status
r.data
"""

content = connectBuilder.request('GET','https://lora415.org')

soup = bsoup(content.data)



print(soup.prettify())
