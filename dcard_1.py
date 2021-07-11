import requests, json
import matplotlib.pyplot as plt
#匯入matplotlib函式庫下的pylopt函式，並且命名為plt

url = 'https://www.dcard.tw/_api/forums/funny/posts?popular=true'
res = requests.get(url)
resjson = json.loads(res.text)

gender_count = {'F':0, 'M':0, 'D':0}

for outome in resjson:
	gender_count[outome['gender']] = gender_count[outome['gender']]+1

sex = ['Women','Man']
total = [gender_count['F'],gender_count['M']]
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.bar(sex,total)
plt.show()


# import matplotlib.pyplot as plt 
# labels = 'A','B','C','D','E','F'
# size = [33,52,12,17,62,48]
# plt.pie(size , labels = labels,autopct= '%1.1f%%') #pie
# plt.axis('equal')
# plt.show()

#print(resjson)
