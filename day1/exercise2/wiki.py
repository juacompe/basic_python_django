from BeautifulSoup import BeautifulSoup
import requests
import sys

def get_from_wiki(keyword):
    url = 'http://en.wikipedia.org/wiki/%s' % keyword
    response = requests.get(url)
    return response

def get_first_paragraph(html):
    soup = BeautifulSoup(html)
    paragraph = soup.find('p')
    return paragraph.getText(separator=u' ')

if __name__ == '__main__':
    keyword = sys.argv[1]
    response = get_from_wiki(keyword)
    result = get_first_paragraph(response.content)
    print result
