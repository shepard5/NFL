## A simple football model
#/Users/samscott/Desktop/NFL Model
from functions import *
def football(team):
    data = scrape_page_typeA('American Football','0','USA','NFL','2023')
    print(data)
