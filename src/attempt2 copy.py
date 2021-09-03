
import re
import requests
from bs4 import BeautifulSoup
import csv
url = "https://en.wikipedia.org/wiki/Australian_Football_League"
response = requests.get(url)

converting_html = response.text
page = BeautifulSoup(converting_html, "html.parser")

club_table = page.find("table", attrs={"class":"wikitable sortable"})
club_table_data = club_table.tbody.find_all("tr")

    
headings =[]
required_headings = []
    
for th in club_table_data[0].find_all("th"):
        headings.append(th.text.replace('\n', ' ').strip())
for main_headings in headings:
        
    if main_headings.lower() == "club":
        required_headings.append(main_headings)
    elif main_headings.lower() == "moniker":
        required_headings.append(main_headings)
    elif main_headings.lower() == "home venue":
            required_headings.append(main_headings)
    elif main_headings.lower() == "state":
        required_headings.append(main_headings)
    
required_headings.append("Club ID")
required_headings[1] = "Nick Name"

with open("..//Proj_postcode/output/club_details.csv", "w", newline= "") as Club_File:
    writer = csv.writer(Club_File)
    writer.writerow(required_headings)
    for index in range(2, len(club_table_data)):
        row_headings =[]
        data_list = []
        new_data_list =[]
        
        for th in club_table_data[index].find_all("th"):
            
            row_headings.append(th.text.replace("\n", " ").strip())
            
        
        for td in club_table_data[index].find_all("td"):
            
            data_list.append(td.text.replace("\n", " ").strip())
        new_data_list = data_list[1:4]
        for stuff in new_data_list:
            row_headings.append(stuff)
            
        row_headings.append(index + 1000)
        print(len(row_headings))
        if len(row_headings) > 4:
            writer.writerow(row_headings)
        else:
            pass

    Club_File.close()

response.close()

