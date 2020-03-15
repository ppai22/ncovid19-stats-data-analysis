import json


with open('data.json', 'r+') as f:
    data = json.load(f)

COUNTRIES = ['India', 'Iran', 'USA', 'UK', 'Italy', 'Spain', 'South Korea']

country_wise_data = dict()
for country in COUNTRIES:
    country_wise_data[country] = []
for report in data.keys():
    for item in data[report]:
        country_wise_data[item[0]].append([report, item[1]])

with open('country_wise_data.json', 'w+') as f:
    json.dump(country_wise_data, f, indent=4)
