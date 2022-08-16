import csv
import math
with open('data99.csv',newline='') as o:
    reader=csv.reader(o)
    filedata=list(reader)
data=filedata[0]
def mean(data):
    p=len(data)
    total=0
    for x in data:
        total+=int(x)
    mean=total/p
    return mean
squarelist=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    squarelist.append(a)
sum=0
for i in squarelist:
    sum=sum+i
result=sum/(len(data)-1)
standarddeviation=math.sqrt(result)
print(standarddeviation)
