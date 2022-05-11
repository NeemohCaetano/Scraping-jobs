#importando bibliotecas
from bs4 import BeautifulSoup as soup 
import requests as req
import time

#escolhendo skills que você não tem
unfamiliar_skill = input('wich skills you dont have?')
#print pra avisar que os dados estão sendo mineirados
print(f'Filtering out {unfamiliar_skill}...')

#função para encontrar os dados
def find_jobs():
    #escolhendo o site onde os dados estão sendo buscados
    html_text = req.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    #pegando a página em si
    soup_html = soup(html_text, 'lxml')
    #aqui eu to transformando essa página em uma var utilizavel
    jobs = soup_html.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    #encontrando o atributo class para: nome da empresa,experiência necessária,local,habilidades necessárias, informações adicionais; 
    for job in jobs:
        publish_date = job.find('span', class_ = 'sim-posted').span.text
        if 'few' in publish_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace('(More Jobs)', '')   #this finds the class where the company name is
            experience = job.find('ul', class_ = 'top-jd-dtl clearfix').li.text
            experience_time = experience[11:]
            location = job.find('ul', class_= 'top-jd-dtl clearfix').text.replace(' ', '')
            job_location= location[31:]
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')#this finds the class where the skills r
            more_info = job.header.h2.a['href']
            #definindo que o script só vai retornar dados para vagas de trabalho onde a var skills não contem os valores da var unfamiliar_skills
            if unfamiliar_skill not in skills:
        
                print(f'Company Name: {company_name.strip()}')
                print(f'Required Skills: {skills.strip()}')
                print(f'Needed Experience: {experience_time.strip()}')
                print(f'Location: {job_location.strip()}')
                print(f'More Info: {more_info}')
                print('----------------------------------------------------------------------------------------------')
#timer para que o programa possa ficar aberto por tempo indeterminado, dependendo do usuário matar ele
if __name__ == '__main__':
    while True: 
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} seconds...')
        time.sleep(time_wait*60)