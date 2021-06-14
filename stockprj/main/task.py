import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

try:
    url = requests.get('http://www.nepalstock.com/todaysprice')
except Exception as e:
    print(f'Error getting data because : {e}')

soup = BeautifulSoup(url.content,'html.parser')
#@sharedtask

def scrap():  
    try:
        tp_table = soup.find('table', class_="table table-condensed table-hover") #finding the today table
        data_date = tp_table.find('label',class_="pull-left").text
        heading_ = tp_table.find('tr',class_="unique").text
        main_data = tp_table.find('tr')
        print(main_data).prettify()
        print(heading_)
        print(data_date)
        
    #print(tp_table.prettify())
    except Exception as e:
        print("Unable to get the class 'table table-condensed table-hover' maybe the site has changed this style")
        print(f"main error is : {e}")     

scrap()
