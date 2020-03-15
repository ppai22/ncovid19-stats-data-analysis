import json
import camelot
import pandas
import re


with open('directory.json', 'r+') as f:
    directory = json.load(f)
COUNTRIES = {'India': 'India', 'Iran': 'Iran', 'USA': 'United States',
             'UK': 'United Kingdom', 'Italy': 'Italy', 'Spain': 'Spain',
             'South Korea': 'Korea'}
data = dict()
for report in directory:
    print(report[0])
    data[report[0]] = list()
    try:
        tables = camelot.read_pdf(report[1], pages='1-end')
        for table in tables:
            df = pandas.DataFrame(table.df)
            for i in df.index:
                for country in COUNTRIES.keys():
                    if re.findall(COUNTRIES[country], df.loc[i][0]):
                        data[report[0]].append([country, df.loc[i].values.tolist()])
                    elif re.findall(COUNTRIES[country], df.loc[i][1]):
                        data[report[0]].append([country, df.loc[i].values.tolist()])
    except Exception as e:
        print(e)
with open('data.json', 'w+') as f:
    json.dump(data, f, indent=4)
