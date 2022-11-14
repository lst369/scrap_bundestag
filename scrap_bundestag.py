import requests
from bs4 import BeautifulSoup
import lxml
import time
import random
import json
# Парсим список всех кандидатов и записываем его в файл
# person_url_list = []

# for i in range (0, 760, 20):
#     url = f"https://github.com/lst369/scrap_bundestag.gitajax/filterlist/en/members/863330-863330?limit=20&noFilterSet=true&offset={i}"
    
#     q = requests.get(url)
#     result = q.content

#     soup =  BeautifulSoup(result, "lxml")

#     persons = soup.find_all("a")


#     for person in persons:
#         person_page_url = person.get("href")
#         person_url_list.append(person_page_url)
    
#     time.sleep(random.randrange(2, 4))

# with open ("scrap_bundestag/data/person_url_list.txt", "a") as file:
#     for line in person_url_list:
#         file.write(f"{line}\n")

with open ("scrap_bundestag/data/person_url_list.txt") as file:

    lines = [line.strip() for line in file.readlines()]

    data_dict = []
    count = 0

    for line in lines:
        q = requests.get(line)
        result = q.content
        
        soup = BeautifulSoup(result, "lxml")
        person = soup.find(class_="col-xs-8 col-md-9 bt-biografie-name").find("h3").text
        person_name_company = person.strip().split(",")
        person_name = person_name_company [0]
        person_company = person_name_company[1].strip()

        social_networks = soup.find_all(class_="bt-link-extern")

        social_networks_url = []
        for item in social_networks:
            social_networks_url.append(item.get("href"))
        
        data = {
            "person_name": person_name,
            "company_name": person_company,
            "sosial_networks": social_networks_url
        }
        count += 1
        print(f"#{count}:{line} is done!")
        time.sleep(random.randrange(1, 2))

        data_dict.append(data)

        with open ("scrap_bundestag/data/data.json", "w") as json_file:
            json.dump(data_dict, json_file, indent=4)



