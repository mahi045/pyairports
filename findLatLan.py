from pyairports.airports import Airports
airports = Airports()

f = open("iata_code.txt", "r")
for _ in f:
    airports.airport_iata(_)

