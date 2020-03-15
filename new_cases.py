import json
import matplotlib.pyplot as plt


with open('plot_growth_data.json', 'r+') as f:
    growth_data = json.load(f)

COUNTRIES = ['India', 'USA', 'UK', 'Italy', 'Spain', 'South Korea']

new_cases = dict()
for country in COUNTRIES:
    new_cases[country] = []

for country in COUNTRIES:
    for report in range(len(growth_data[country])):
        report_no = growth_data[country][report][0]
        if report_no == 14:
            new_cases_today = growth_data[country][report][1]
        else:
            new_cases_today = growth_data[country][report][1] - growth_data[country][report-1][1]
        new_cases[country].append([report_no, growth_data[country][report][1], new_cases_today])

with open('new_cases.json', 'w+') as f:
    json.dump(new_cases, f, indent=4)

for country in COUNTRIES:
    plt.plot(
        [item[0] for item in new_cases[country]],
        [item[2] for item in new_cases[country]],
        label=country
    )
plt.xlabel('DAY')
plt.ylabel('NO_OF_NEW_CASES')
plt.legend()
plt.show()
