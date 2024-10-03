from bs4 import BeautifulSoup
import requests
import re 




def get_all_links():

    page = requests.get("https://www.bmi.gv.at/412/Nationalratswahlen/Historischer_Rueckblick.aspx")

    #soup = BeautifulSoup(page.content, "html.parser")



    with open("resources/Historischer_Rückblick.html") as f:
        soup = BeautifulSoup(f, "html.parser")
        ul = soup.find("ul", {"class":"ergebnisse_historisch"})


    output_list = []

    for li in ul.find_all("a"):
        print(li["href"])
        output_list.append(li["href"])

    return output_list
