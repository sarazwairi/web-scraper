import requests
from bs4 import BeautifulSoup
import json


def get_citation_needed_count(url):
    response=requests.get(url)
    content=BeautifulSoup(response.content,"html.parser").find_all('a',title='Wikipedia:Citation needed')
    return len(content)


def get_citation_needed_report(url):
    response=requests.get(url)
    content=BeautifulSoup(response.content,"html.parser").find_all('a',title='Wikipedia:Citation needed')
    result=""
    resultarr=[]
    for i in content:
        result+=f'{i.parent.parent.parent.text}\n'
        resultarr.append({'paragraph':i.parent.parent.parent.text})
    obj=json.dumps(resultarr,indent=4)
    with open('citation-needed.json','w') as file:
        file.write(obj)
    return result

if __name__=="__main__":
    url ="https://en.wikipedia.org/wiki/History_of_Mexico"
    print(get_citation_needed_count(url))
    print(get_citation_needed_report(url))

