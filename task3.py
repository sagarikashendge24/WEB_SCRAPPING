from task1 import scrape_top_list
screpped=scrape_top_list()
from task2 import group_by_year
dec_arg=group_by_year(screpped)
import json
def group_by_decade(movies):
    moviedec = {}
    list1 = []
    for index in movies:
        mod = index%10
       
        decade=index-mod
        print(mod)
        print(decade)
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    print(list1)
    for i in list1:
        moviedec[i]=[]
    for i in moviedec:
        dec10 = i + 9
        for x in movies:
            if x <= dec10 and x>=i:
                for v in movies[x]:
                    moviedec[i].append(v)
                with open("task_3.json","w") as file:
                    json.dump(moviedec,file,indent=4)    
    return(moviedec)
group_by_decade(dec_arg)






