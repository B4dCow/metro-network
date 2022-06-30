import csv
import io
import collections
import json
import os
import pandas


filename = '서울교통공사 노선별 지하철역 정보.csv'
opendata = os.path.join(os.path.abspath("metronetwork"), 'data', filename)

def read_seoul_metro():
	samdasu = {}
	df = pandas.read_csv(opendata, sep=',', encoding='CP949')
	for rows in df.values:
		li = []
		li.append(str(rows[1]))
		li.append(str(rows[3]))
		samdasu[rows[4]] = li
	od = collections.OrderedDict(sorted(samdasu.items(), key=str))
	return od

def read_seoul_subway():
	df = pandas.read_csv(opendata, sep=',', encoding='CP949')
	df = df.sort_values([df.columns[3], df.columns[4]])
	return df

def readSeoulMetro():
	samdasu = {}
	with io.open(opendata, mode='r', encoding='utf-8') as csvfile:
		datareader = csv.reader(csvfile, delimiter=' ', quotechar=',')
		next(datareader)
		for row in datareader:
			str = "\" ".join(row)
			str = str.replace('\"','')
			obj = str.rstrip().split(',')

			li = []
			li.append(obj[1])
			li.append(obj[2])
			samdasu[obj[3]] = li

	od = collections.OrderedDict(sorted(samdasu.items()))
	return od	

def name_fr_mapping(od):
	mapping = {}
	for fr, name_line in od.items():
		mapping[name_line[0]] = fr
	return mapping

def fr_station_mapping(od):
	mapping = {}
	for fr, name_line in od.items():
		mapping[fr] = name_line[0]
	return mapping

def create_json(path=None):
	jsondata = os.path.join(os.path.abspath("metronetwork"), 'data', "seoul_subway_json");
	if path:
		jsondata = os.path.join(path, "seoul_subway_json");
	
	data = read_seoul_metro()
	with open(jsondata, "w", encoding="utf-8") as outfile:
		json.dump(data, outfile, indent = 4, ensure_ascii = False)

def read_seoul_metro_transfer():
	pass

def load_edges():
	edgedata = os.path.join(os.path.abspath("metronetwork"), 'data', "edge_list.json");
	with open(edgedata, "r", encoding="UTF-8") as f:
		data = json.loads(f.read())
	return data
