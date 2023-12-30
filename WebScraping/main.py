
import requests 
from bs4 import BeautifulSoup 

# Making a GET request 
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/') 
  
# Parsing the HTML 
soup = BeautifulSoup(r.content, 'html.parser') 
print(soup.prettify()) 
