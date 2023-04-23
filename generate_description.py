import requests
import re
from bs4 import BeautifulSoup
import random

url_base = "https://www.gutenberg.org/ebooks/"
Max = 67915

def get_book_url(number):
    url_requests = url_base + number
    response = requests.get(url_requests)
    response_text = response.text
    soup = BeautifulSoup(response_text, 'html.parser')
    category_tag = soup.find_all("td", property="dcterms:type")
    if len(category_tag) == 0:
        return None
    category = category_tag[0].string
    if category == "Text":
        hijos = soup.body.find("table").contents
        url = hijos[len(hijos)-4]["about"]
        return url
    else:
        return None

def rand_description(words, position, book):
    """
        (int) words : number of words for description
        (int) position : initial position in the book
        (int) book : book at gutenberg.org
    """
    url = get_book_url(str(book))
    # print('words', words, 'position', position, 'book', book)
    # print(url)
    if url == None:
        book = random.randint(1, Max)
        return rand_description(words, position, book)
    response = requests.get(url)
    text = response.text
    s = " ".join(re.split(r"\s+", text))
    lista = s.split(' ')
    description = ' '.join(lista[position:position+words])
    return description.lower()

"""
# TEST rand_description(words, position, book)
for i in range(10):
    words = random.randint(1, 100)
    position = random.randint(100, 500)
    book = random.randint(1, 200)
    print('description: ',rand_description(words, position, book),'\n')
"""
