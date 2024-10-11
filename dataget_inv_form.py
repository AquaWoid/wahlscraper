from bs4 import BeautifulSoup
import os
import re
import pandas

df_init = {"year" : [1945], "Name" : ["Sozialistische Partei Österreich"], "Abbr" : ["SPö"] , "Votes" : [120], "Percent" : [30], "Mandates" : [19]}
df = pandas.DataFrame(data=df_init)

content = []


for file in os.listdir("resources/invalid_format"): 

    with open(f"resources/invalid_format/{file}", encoding="UTF-8") as f:

        soup = BeautifulSoup(f, "html.parser")
        #print(soup.prettify())

        for tr in soup.find("tbody", {"class":"result_format"}).find_all("tr"):

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

            df.loc[len(df)] = [re.findall((r"\d{4}"), file), t[0],t[1],int(re.sub("\.|,", "", t[2])), t[3].replace(",","."), None]

        print(file, "  DONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")


print(df)
df.to_csv(r"C:\Users\stefa\Desktop\results_inv_form.csv", header=True)

   # print (file)


