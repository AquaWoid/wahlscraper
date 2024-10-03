from bs4 import BeautifulSoup
import pandas
import requests
import re

class Result:

    def __init__(self, name : str, nameabbr: str, votes : int, percent :float, mandates : str):
        self.name = name
        self.nameabbr = nameabbr
        self.votes = votes 
        self.percent = percent
        self.mandates = mandates


def process_data(url):

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    print(type(soup.find("tbody")) )
    content = []

    for tr in soup.find("tbody"):
        content.append(tr.text.split("\n"))


    content_cleaned = [i for i in content if i != ["",""]]
    content_cleaned = [[i for i in l if i] for l in content_cleaned]


    print(content_cleaned)

    for t in content_cleaned:

        res = Result(t[0],t[1],int(re.sub("\.|,", "", t[2])), float(t[3].replace(",",".")), t[4])

        print(res.name)
        print(res.nameabbr)
        print(res.votes)
        print(res.percent)
        print(res.mandates)

    return res

process_data("https://www.bmi.gv.at/412/Nationalratswahlen/Nationalratswahl_1953/start.aspx")
