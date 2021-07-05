from bs4 import BeautifulSoup

with open("C:\\Users\\Antri\\Desktop\\practice\\HTML\\Blog html\\template.html","r") as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content,'lxml')
    course_cards = soup.findAll('div',class_='tags')
    for course in course_cards:
        print(course_cards)
   

    
