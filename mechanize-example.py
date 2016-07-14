import re
import mechanize

response = mechanize.urlopen("http://www.example.com/")
print response.read()
