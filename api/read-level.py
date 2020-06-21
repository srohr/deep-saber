from json import load as json_load
from pprint import pprint


FILE = "/home/steven/projects/deep-saber/api/data/mr-blue-sky/Expert.dat"

with open(FILE) as f:
    level = json_load(f)

pprint(level)
