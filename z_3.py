import argparse
import requests
import json


parser = argparse.ArgumentParser()
parser.add_argument('arg', nargs='*')
parser.add_argument('--shadow', type=int, default=0)
parser.add_argument('--intensity', type=str, default='')
args = parser.parse_args()

print(args)

server = args.arg[0]
port = args.arg[1]
colors = args.arg[2:]


with open('data.json') as cat_file:
    json_resp = json.load(cat_file)


out_list = []

for key_tree, v_tree in json_resp.items():
    for dct in v_tree:
        for color in colors:
            if color in dct['color'] and args.intensity in dct['color']:
                if args.shadow <= dct['shadow']:
                    out_list.append([dct['name'], key_tree, dct['drought'], dct['shadow']])

out_list = sorted(out_list, key=lambda x: (-x[3], -x[2], x[0]))

with open('pampa.json', 'w', encoding='utf-8') as f:
    json.dump(out_list, f)