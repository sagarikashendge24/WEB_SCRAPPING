from task1 import scrape_top_list
import json
import pprint
screpped=scrape_top_list()
def group_by_year(movies):
    years=[]
    for i in movies:
        year = i["Year"]
        if year not in years:
            years.append(year)
    # print(years)        
    movie_dic = {i:[]for i in years}
    print(i)
    for i in movies:
        year=i["Year"]
        for x in movie_dic:
            if str(x)==str(year):
                movie_dic[x].append(i)
            with open("task_2.json","w") as file:
                json.dump(movie_dic,file,indent=4)    
    return movie_dic
group_by_year(screpped)



