
from email import header
from unicodedata import name
import requests
import pandas as pd
from bs4 import BeautifulSoup
def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    url = f'https://in.linkedin.com/jobs/search?keywords=Data%Science&location=India&geoId=&trk=homepage-jobseeker_jobs-search-bar_search-submit&position=1&pageNum=0'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    return soup
print(extract(10))
def transform(soup):
    divs = soup.find_all('div', class_='base-card')
    
    # for i in link:

    #     date = i.find('a', class_='base-card__full-link').text
    #     print(date)
    # print(link)
    
    for item in divs:
        title = item.find('a').text.strip()
        name = item.find('h4', class_ = 'base-search-card__subtitle').text.strip()
        link = item.find('a', href = True)
        # print(title)
        # print(name)
        # print(link['href'])
        # print(" ")
        job = {
            'title': title,
            'name': name,
            'link': link['href']
        }
        joblist.append(job)
    return
joblist = [] 

   

c= extract(0)

transform(c)
print(joblist)
df = pd.DataFrame(joblist)
df.to_csv('jobs.csv')
