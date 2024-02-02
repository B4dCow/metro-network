
import networkx as nx
import metronetwork as mn

paris = mn.Paris()
G = paris.make_paris_metro_network()

departure_a = paris.station("Exelmans")
departure_b = paris.station("Corentin-Celton")
departure_c = paris.station("Cardinal-Lemoine")

result = mn.find_center_one(G, [departure_a, departure_b,departure_c])
print(paris.stations[result])
