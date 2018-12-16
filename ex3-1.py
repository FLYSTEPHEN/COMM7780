import math as m
cities={
    "Hong_Kong":[22.32,114.17],
    "New_York":[40.71,-74.01],
    "Vancouver":[49.28,-123.12],
    "Stockholm":[59.33,18.07],
    "London":[51.51,-0.13],
    "Buenos_Aires":[-34.60,-53.38],
    "Perth":[-31.95,115.86],
}

def cal(city1):
    try:
        r=6371.009
        f1=m.radians(cities[city1][0])
        l1=m.radians(cities[city1][1])

        for i in range(0,len(cities)):
            city2=list(cities.keys())[i]
            if city1==city2:
                continue
            laititude,longitude=list(cities.values())[i][0],list(cities.values())[i][1]
            f2=m.radians(laititude)
            l2=m.radians(longitude)
            Ds1=m.acos(m.sin(f1)*m.sin(f2)+m.cos(f1)*m.cos(f2)*m.cos(l1-l2))
            distance=round(r*Ds1,1)
            print('The straight line distance on earth surface from %s to %s is %s kilometers'%(city2,city1,distance))
            
    except KeyError:
        print("Oops!There is no such city in the database.")
    
cal("Hong_Kong")