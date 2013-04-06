from BeautifulSoup import BeautifulSoup
import requests

def get_from_wiki(keyword):
    url = 'http://en.wikipedia.org/wiki/%s' % keyword
    response = requests.get(url)
    return response

def get_first_paragraph(html):
    soup = BeautifulSoup(html)
    paragraph = soup.find('p')
    link_names = [ link.text for link in paragraph.findAll('a') ]
    return paragraph.getText(separator=u' ')

