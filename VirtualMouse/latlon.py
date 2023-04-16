from math import radians, cos, sin, asin, sqrt , atan2


def distance(lat1, lat2, lon1, lon2):
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

    c = 2 * asin(sqrt(a))
    r = 6371
    return (c * r)


import json
limitval = int(input('Limit - '))
requiredlist = []
f = open('countriesV2.json' )
totalsum = 0
# returns JSON object as
# a dictionary
data = json.load(f)
count =0

# Iterating through the json
for i in range(len(data)):
    x = data[i]['population']

    if (x >= limitval):
        #print(i,x,data[i]['latlng'])
        requiredlist.append([i,x,data[i]['latlng']])


requiredlist = sorted(requiredlist, key=lambda x: x[1])
requiredlist.reverse() #I also tried without reversing the list and getting the distances Alphabetically as given in the dataset and also by population both didnt work
print(requiredlist)
for i in range(0,20):
    # print(data[requiredlist[i][0]]['name'])
    print(requiredlist[i][0])
    lat1 = requiredlist[i][2][0]
    lon1 = requiredlist[i][2][1]
    for j in range(i+1,20):
        if (requiredlist[i][0]!= requiredlist[j][0]):
            lat2 = requiredlist[j][2][0]
            lon2 = requiredlist[j][2][1]

            totalsum += round(distance(lat1,lat2,lon1,lon2),2)

            print(i,j)
            count+=1



print(round(totalsum,2),totalsum,count)

# Closing file
f.close()
