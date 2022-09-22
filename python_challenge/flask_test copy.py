from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello!'



if __name__ == '__main__':
    app.run()
    

from bs4 import BeautifulSoup
import requests


def extract_jobs(term):
  url = f"https://remoteok.com/remote-{term}-jobs"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    # write your ✨magical✨ code here
    job_tr = soup.find_all('tr', class_="job")
    for job_tr_section in job_tr:
      job_td = job_tr_section.find_all('td')
      #job_td.pop(0)
      job_td.pop(-1)
      #print(job_td)
    #   print("---------------------------------------------------------------")
      for job_td_section in job_td:
        #base = job_td_section.find_all('a')
        if job_td_section.find('h3', itemprop="name") != None:
          company_name = job_td_section.find('h3', itemprop="name")
          print(f"{company_name.string}", end='  ')
          
        if job_td_section.find('span', class_="verified tooltip") != None:
          #verified = job_td_section.find('span', class_="verified tooltip")
          print("✅ Verified", end='')

        if job_td_section.find('h2', itemprop="title") != None:
          title = job_td_section.find('h2', itemprop="title")
          print(title.string)

        if job_td_section.find('div', class_="location") != None:
          location, money = job_td_section.find_all('div', class_="location")
          print(location.string, money.string)
          
        if job_td_section.find('a', itemprop="url") != None:
          link = job_td_section.find('a', itemprop="url")
          reuslt = (f"{url}{link['href']}")
          
        #if job_td_section.find('span', class_="verified tooltip") != None:
          #verified = job_td_section.find('span', class_="verified tooltip")
          #print("Verified")
        #anchor = base[0]
        #link = company_name['herf']
        #print(link)
        
        #print(anchors)
        #print("----------------------")
      #print("---------------------------------------------------------------")
  else:
    print("Can't get jobs.")

extract_jobs("rust")