import json
import matplotlib.pyplot as plt


with open('new_cases.json', 'r+') as f:
    new_cases = json.load(f)

COUNTRIES = ['India', 'Italy', 'Spain', 'South Korea']
growth_rate = {}
for country in COUNTRIES:
    growth_rate[country] = []

report_no = 0
for country in COUNTRIES:
    for report in range(len(new_cases[country])):
        report_no = new_cases[country][report][0]
        if report_no == 14:
            growth_factor = 0
        else:
            if new_cases[country][report-1][2] == 0:
                growth_factor = 0
            else:
                growth_factor = new_cases[country][report][2]/new_cases[country][report-1][2]
        growth_rate[country].append([report_no, growth_factor])

for country in COUNTRIES:
    plt.plot(
        [item[0] for item in growth_rate[country]],
        [item[1] for item in growth_rate[country]],
        label=country
    )
plt.hlines(1, 14, report_no, linestyles='dashed')
plt.legend()
plt.show()
