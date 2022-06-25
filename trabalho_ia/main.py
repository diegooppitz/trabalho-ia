import googlemaps

from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

gmaps = googlemaps.Client(key='AIzaSyDqdspIV0djGL0uqYtFAuUJwtqyG2gVkUU')

cidade = "Porto Alegre"

lugar_preferido = input("Informe o lugar que você gostaria de ficar próximo:")
importancia_lugar= int(input("Informe a importancia do lugar preferido:"))

faculdade = input("Informe o endereço de sua faculdade:")
importancia_faculdade = int(input("Informe a importancia da faculdade:"))

trabalho = input("Informe o endereço de seu trabalho:")
importancia_trabalho = int(input("Informe a importancia de seu trabalho:"))

result = gmaps.geocode(''+ faculdade +',' + cidade +'')
result2 = gmaps.geocode(''+ trabalho +',' + cidade +'')
result3 = gmaps.geocode(''+ lugar_preferido +',' + cidade +'')

lat = result[0]['geometry']['location']['lat']
lng = result[0]['geometry']['location']['lng']

lat2 = result2[0]['geometry']['location']['lat']
lng2 = result2[0]['geometry']['location']['lng']

lat3 = result3[0]['geometry']['location']['lat']
lng3 = result3[0]['geometry']['location']['lng']

coordenadas = []
estudo = [lat,lng]
trabalho = [lat2,lng2]
preferido = [lat3,lng3]

for x in range(0,importancia_faculdade):
    coordenadas.append(estudo)

for x in range(0,importancia_trabalho):
    coordenadas.append(trabalho)

for x in range(0, importancia_lugar):
    coordenadas.append(preferido)

dataset = np.array([])
dataset = np.vstack(coordenadas)


plt.scatter(dataset[:, 1], dataset[:, 0])
plt.xlim(-51.26, -51.09)
plt.ylim(-30.25, -29.9)
plt.grid()

kmeans = KMeans(
   n_clusters=1,
   init='k-means++', n_init=10,
   max_iter=300
)

pred_y = kmeans.fit_predict(dataset)

plt.scatter(dataset[:, 1], dataset[:, 0], c=pred_y)
plt.xlim(-51.26, -51.09)
plt.ylim(-30.25, -29.9)
plt.grid()

plt.scatter(kmeans.cluster_centers_[:, 1], kmeans.cluster_centers_[:, 0], s=70, c='red')
plt.show()


