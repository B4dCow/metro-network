import metronetwork as mn
import networkx as nx
import os


class Paris():
    def __init__(self):
        self.line_edges = mn.dataloader.load_edges()
        self.line_transfer = mn.dataloader.load_transfers()
        self.stations = mn.dataloader.load_stations()
        self.stations_name = mn.dataloader.load_stations_name()

    # def graph(self):
    #     model_path = os.path.join(mn.metro_utils.INSTALLED_PATH, 'data', 'seoulgraph.gpickle')
    #     G = nx.read_gpickle(model_path)

    def code(self, fr):
        return self.stations.get(fr)[0]

    def station(self, name, autocorrect=False):
        if self.stations_name.get(name) == None:
            print(f'{name} is not a valid station name\n'
                  f'Do you mean {mn.match.match_station(self.stations_name.keys(), name)} ?')
            if autocorrect:
                return self.stations_name.get(mn.match.match_station(self.stations_name.keys(), name))
        return self.stations_name.get(name)

    def get_station(self, fr):
        return self.stations.get(fr)[1]

    def get_stations_name(self, fr_list):
        name = []
        for fr in fr_list:
            if self.stations.get(fr):
                name.append(self.stations.get(fr)[1])
            else:
                name.append(None)
        return name

    def station_eng(self, fr):
        return self.stations.get(fr)[2]

    def line(self, fr):
        return self.stations.get(fr)[3]

    def make_paris_metro_network(self):
        stations = self.stations
        edges = self.line_edges
        G = nx.DiGraph()

        G.add_nodes_from(stations.keys())
        for key in edges:
            G.add_edges_from(edges.get(key), weight=2)
        transfers = self.line_transfer
        for transfer_edge in transfers:
            if lambda x: True if "A" in x else False:
                G.add_edges_from(transfer_edge, weight=15)
            elif lambda x: True if "K" in x else False:
                G.add_edges_from(transfer_edge, weight=10)
            else:
                G.add_edges_from(transfer_edge, weight=5)
        return G


if __name__ == '__main__':
    paris = Paris()
    G = paris.make_paris_metro_network()
    print(G)
