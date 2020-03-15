import json
import matplotlib.pyplot as plt
from math import log10


with open('country_wise_data.json', 'r+') as f:
    country_wise_data = json.load(f)

COUNTRIES = ['India', 'Iran', 'USA', 'UK', 'Italy', 'Spain', 'South Korea']

plot_data = dict()
for country in COUNTRIES:
    plot_data[country] = []

for country in COUNTRIES:
    for report in country_wise_data[country]:
        try:
            report_no = int(report[0].split('-')[1].strip())
            if report_no < 30:
                cases = int(report[1][2].split('(')[0].strip())
            else:
                cases = int(report[1][1].split('(')[0].strip())
            plot_data[country].append([report_no, cases])
        except:
            pass

with open('plot_growth_data.json', 'w+') as f:
    json.dump(plot_data, f, indent=4)

for country in COUNTRIES:
    plt.plot(
        [item[0] for item in plot_data[country]],
        [log10(item[1]) for item in plot_data[country]],
        label=country
    )
plt.xlabel('DAY')
plt.ylabel('LOG_OF_NO_OF_CASES')
plt.legend()
plt.show()
