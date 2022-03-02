import json
import requests
import csv

with open('migration.json') as file:
    data = json.load(file)

output = []

response = requests.get(f"http://{data['serv']}:{data['gate']}")
json_resp = response.json()


for key, value in json_resp.items():

    if key == data["kind"]:
        for val in value:
            if val["size"] >= data["min_size"]:
                c = 0
                for elem in output:
                    if val["place"] in elem:
                        elem[2] += val["amount"]
                        c = 1
                if c == 0:
                    output.append([val["place"], val["size"], val["amount"]])

output = sorted(output, key=lambda x: (-x[2], -x[1], x[0]))
output.insert(0, ["place", "size", "total"])
with open('butterflies.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='*', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in output:
        writer.writerow(i)