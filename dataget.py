from bs4 import BeautifulSoup
import requests
import re
import linkget
import pandas

class Result:

    def __init__(self, year : int, name : str, nameabbr: str, votes : int, percent :float, mandates : str):
        self.year = year
        self.name = name
        self.nameabbr = nameabbr
        self.votes = votes 
        self.percent = percent
        self.mandates = mandates

df_init = {"year" : [1945,1946], "Name" : ["Sozialistische Partei Österreich", "Österreichische Volksparte"], "Abbr" : ["SPö", "ÖVP"] , "Votes" : [120, 1200], "Percent" : [30, 49], "Mandates" : [19,29]}
df = pandas.DataFrame(data=df_init)

def process_data(url):

    print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
   # print(type(soup.find("tbody")) )
    content = []

    for tr in soup.find("tbody").find_all("tr"):

        td_list = []

        for td in tr.find_all(["td"]):

            if td.name == "td":
                td_list.append(td.text)

        if td_list:
            content.append(td_list)


    content_cleaned = [i for i in content if i != ["",""]]
    content_cleaned = [[i for i in l if i] for l in content_cleaned]


    print(content_cleaned)

    for t in content_cleaned:

        df.loc[len(df)] = [re.findall((r"\d{4}"), url), t[0],t[1],int(re.sub("\.|,", "", t[2])), float(t[3].replace(",",".")), t[4]]

        res = Result(re.findall((r"\d{4}"), url), t[0],t[1],int(re.sub("\.|,", "", t[2])), float(t[3].replace(",",".")), t[4])
        """
        print(res.year)
        print(res.name)
        print(res.nameabbr)
        print(res.votes)
        print(res.percent)
        print(res.mandates)       
                
        """




    return res


def get_full_data():

    all_results = []

    for link in linkget.get_all_links():

        try:
            all_results.append(process_data(link))
        except:
            print(f"invalid formatting on {link} moving on")
        #process_data(link)

    return all_results

get_full_data()
print(df)
df.to_csv(r"C:\Users\stefa\Desktop\results_unfiltered.csv", header=True)
#process_data("https://www.bmi.gv.at/412/Nationalratswahlen/Nationalratswahl_1962/start.aspx")
