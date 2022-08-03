import requests
from bs4 import BeautifulSoup
import csv
   
# URL = "https://www.mykhel.com/football/fifa-world-cup-2022-netherlands-squad-tp366-l4/"  #netheralnd
# URL = "https://www.mykhel.com/football/fifa-world-cup-2022-england-squad-tp114-l4/" #england
# URL = "https://www.mykhel.com/football/fifa-world-cup-2022-germany-squad-tp357-l4/" #england
# URL = "https://www.mykhel.com/football/fifa-world-cup-2022-spain-squad-tp118-l4/" #england
# URL = "https://www.mykhel.com/football/fifa-world-cup-2022-portugal-squad-tp359-l4/" #england
URL = "https://www.mykhel.com/football/fifa-world-cup-2022-england-squad-tp114-l4/" #england
r = requests.get(URL)
   
soup = BeautifulSoup(r.content, 'html5lib')
      
quotes = soup.find_all('div', {'class' :'playerinfo-name'})
for w in quotes:
    q = w.text
    x = q.split()
    position = q.split().pop(-1)
    name = " ".join(x[:-1])
    print("list.add(Player('" + position + "','" + name + "'));")  
    # print(q.text)
filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['theme','url','img','lines','author'])
    w.writeheader()
