import math

from xml.dom import minidom

Mydoc = minidom.parse("vane.xml")

VanSan = []
VanLat = []
VanLon = []

i = 0


for x in range(16):
     name = Mydoc.getElementsByTagName("nombre")[i]
     name = name.firstChild.data
     VanSan.append(name)
     i=i+1
print(VanSan)
j = 0
for x in range(16):
     lat = Mydoc.getElementsByTagName("latitud")[j]
     lat = lat.firstChild.data
     VanLat.append(lat)
     j = j + 1

k = 0
for x in range (16):
     lon = Mydoc.getElementsByTagName("longitud")[k]
     lon = lon.firstChild.data
     VanLon.append(lon)
     k = k +1


s1 = (input("Introdusca el nombre de la estacion de origen: "))

s2 = (input("Introdusca el nombre de la estacion de destino: "))
l=0
for x in range(15):

     if (s1 == VanSan[l]):
          lat1 = Mydoc.getElementsByTagName("latitud")[l]
          lat1 = lat1.firstChild.data
          lon1 = Mydoc.getElementsByTagName("longitud")[l]
          lon1 = lon1.firstChild.data
     l = l + 1

l=0
for x in range(15):

     if (s2 == VanSan[l]):
          lat2 = Mydoc.getElementsByTagName("latitud")[l]
          lat2 = lat2.firstChild.data
          lon2 = Mydoc.getElementsByTagName("longitud")[l]
          lon2 = lon2.firstChild.data
     l = l + 1

float(lat1)
float(lat2)
float(lon1)
float(lon2)

ss = 0

rad = math.pi / 180
distancia1 = (float(lat2) - float(lat1))
distancia2 = (float(lon2) - float(lon1))
R = 6372.795477598
a = (math.sin(rad * distancia1 / 2)) ** 2 + math.cos(rad * float(lat1)) * math.cos(rad * float(lat2)) * (math.sin(rad * distancia2 / 2)) ** 2
ss = 2 * R * math.asin(math.sqrt(a)) + ss

print(ss)

