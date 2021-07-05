from bs4 import BeautifulSoup #bs4 folder contaning module
import requests
import time

print('put the skill that you are not familiar with')
unfamiliar_skill = input('>')#filter your skill interests
print(f'filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.findAll('li',class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs): #enumerate
        published_date = job.find('span',class_='sim-posted').span.text
        if 'few' in published_date: #constraint by key value
            company_name = job.find('h3',class_="joblist-comp-name").text.replace(' ','')
            skills = job.find('span',class_='srp-skills').text.replace(" ","") 
            more_info = job.header.h2.a['href']#link obtain
            if unfamiliar_skill not in skills:
                with open(f'D:\\Antriksh\\{index}.txt','w') as f:
                    f.write(f'Company Name : {company_name}')
                    f.write(f'Required Skills : {skills}')
                    f.write(f'Publish Date : {published_date}')
                    f.write(f'moreinfo : {more_info}')
                print(f'file saved {index}')
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting for {time_wait} minutes......')
        time.sleep(time_wait * 60)
