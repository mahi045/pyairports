from pyairports.airports import Airports
import numpy as np
from sklearn.cluster import KMeans

coordinates = []

# This stuff are necessary for visualization
# color = ["#ED44FE", "#2D1380", "#c25d38", "#752D70", "#0487F5", "#B51936", "#05A346", "#540c12"]
# color_7 = ["#641e16", "#cb4335", "#641e16", "#a93226", "#cb4335","#f1948a", "#cb4335"]
# color_6 = ["#a93226", "#641e16", "#cb4335", "#cb4335", "#cb4335","#fadbd8"]
# color_5 = ["#ec7063", "#641e16", "#ec7063", "#ec7063", "#a93226"]
airports = Airports()
index = 0
mapping = dict()
cluster = open("cluster_group.txt", "w")
f = open("iata_code.txt", "r")  ## this file contains all the IATA codes
# f_vis = open("file_vis.csv", "w")  for visualization
for _ in f:
    data = airports.airport_iata(_)
    coordinates.append([float(data.lat), float(data.lon)])
    mapping[index] = _.split()
    index += 1


points = np.array(coordinates)
n_cluster = 5   ## hyperparameter
clusterer = KMeans(n_clusters=n_cluster, random_state=0).fit(points)
# use line: f_vis.write(str(coordinates[a][0]) + "," + str(coordinates[a][1]) + "," + color[_] + ",square," + "\n") for accuracy
# use line: f_vis.write(str(coordinates[a][0]) + "," + str(coordinates[a][1]) + "," + color[_] + ",," + "\n") for not accuracy
for _ in range(n_cluster):
    print(_, np.count_nonzero(clusterer.labels_ == _))
    index_list = np.where(clusterer.labels_ == _)
    for a in index_list[0]:
        cluster.write(str(a) + ":" + str(_) + "\n")
        # f_vis.write(str(coordinates[a][0]) + "," + str(coordinates[a][1]) + "," + color_5[_] + ",square," + "\n")

    # s = "".join(mapping[_][0] + " " for _ in index_list[0])
    # cluster.write(s + "\n")

cluster.close()

# helpful stuff: https://www.world-airport-codes.com/ 