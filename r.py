import json
import requests
x=requests.get('http://saral.navgurukul.org/api/courses')
h=x.json()
#print(h)
with open('courses.json',"w") as y:
    json.dump(h,y,indent=4)
c=0
id=[]
for i in h["availableCourses"]:
    print(c,i['name'],i['id'])
    id.append(i['id'])
    c=c+1
num=int(input("enter your serial number::"))
r=0
k=requests.get("http://saral.navgurukul.org/api/courses/"+id[num]+"/exercises")
m=k.json()
s=[]
for i in m["data"]:
    print(r,i["slug"]) 
    s.append(i["slug"])
    r+=1
num2=int(input("enter your slug number::"))
l=requests.get("http://saral.navgurukul.org/api/courses/"+str(num)+"exercise/getBySlug?slug="+s[num2])
o=l.json()
print(o)

        
        
        
        