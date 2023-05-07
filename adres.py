import requests
import random

tc = input("TC : ")

url = "https://randomuser.me/api/?nat=tr&inc=name,location&noinfo"
response = requests.get(url)
data = response.json()

name = data['results'][0]['name']['first'] + " " + data['results'][0]['name']['last']
city = data['results'][0]['location']['city']
state = data['results'][0]['location']['state']
postcode = data['results'][0]['location']['postcode']
latitude = data['results'][0]['location']['coordinates']['latitude']
longitude = data['results'][0]['location']['coordinates']['longitude']


mahalle_listesi = ['Merkez', 'Kuzey', 'Güney', 'Doğu', 'Batı', 'Orta', 'Yeni', 'Eski', 'İnönü', 'Atatürk', 'Cumhuriyet', 'Barış', 'Özgürlük', 'Gül', 'Çiçek', 'Meydan', 'Bahçe', 'Park', 'Yıldız', 'Ay', 'Güneş']
neighborhood = random.choice(mahalle_listesi)


sokak_listesi = ['Cumhuriyet', 'Atatürk', 'İnönü', 'Barış', 'Özgürlük', 'Bahçe', 'Park', 'Çınar', 'Güzel', 'Gül', 'Meydan', 'Yıldız', 'Ay', 'Güneş']
sokak = random.choice(sokak_listesi)
door_no = str(random.randint(1, 39))
apartment_no = str(random.randint(1, 999))

address = f"{sokak} Sokak No:{door_no}/{apartment_no}"
door_no = str(random.randint(1, 39))
print("ADRESI: " + address)
print("MAHALLE/SEMT: " + neighborhood)
print("ŞEHİR: " + city)
print("İL: " + state)
print("POSTA KODU: " + str(postcode))
print("ENLEM: " + str(latitude))
print("BOYLAM: " + str(longitude))
print("KAPINO: " + str(random.randint(1, 39)))
