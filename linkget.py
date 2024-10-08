from bs4 import BeautifulSoup

def get_all_links():

    with open("resources/Historischer_Rückblick.html") as f:
        soup = BeautifulSoup(f, "html.parser")
        ul = soup.find("ul", {"class":"ergebnisse_historisch"})
        #ul_vor = soup.find("ul", {"class":"ergebnisse_vor_1945"})

    output_list = []


    for li in ul.find_all("a"):
        print(li["href"])
        output_list.append(li["href"])


    return output_list

get_all_links()