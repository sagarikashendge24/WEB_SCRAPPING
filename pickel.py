import  requests
from bs4 import BeautifulSoup
import pprint
import json

def scrap_pickel():
    url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
    r=requests.get(url)
    soup=BeautifulSoup(r.text,"html.parser")
    div=soup.find("div",class_="_1gX7")
    s=div.span.get_text()
    name=s.split(" ")
    a=int(name[1])
    c=a//32+1      
    pickle=[]
    serialno=1
    i=1
    while i<=c:
        url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
        m = requests.get(url)
        soup = BeautifulSoup(m.text,"html.parser")
        div = soup.find("div",class_="_3RA-")
        b = div.find_all("div",class_="UGUy")      
        j=0
        while j<len(b):
            Pickle_name=(div.find_all("div",class_="UGUy")[i]).get_text()
            Pickle_price=(div.find_all("div",class_="_1kMS")[i]).get_text()
            Pickle_link=(div.find_all("div",class_="_3WhJ")[i]).a["href"]
            m="https://paytmmall.com/"+Pickle_link
            dict={"Position":serialno,"Name":Pickle_name,"Price":Pickle_price,"Url":m}
            pickle.append(dict)
            serialno+=1
            j+=1
        i+=1
            
        with open("task_4.json","w") as file:
            json.dump(pickle,file,indent=4)
# print(pickle())
print(scrap_pickel())
