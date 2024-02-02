from thefuzz import process
from thefuzz import fuzz
import metronetwork as mn



def match_station(stations_name,name):
    return process.extractOne(name,stations_name)[0]