import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, fsolve


def logistic_function(x, a, b, c):
    return c/(1+np.exp(-(x-b)/a))


with open('country_wise_data.json', 'r+') as f:
    country_wise_data = json.load(f)

COUNTRIES = ['Italy', 'South Korea', 'Spain', 'Iran']

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

for country in COUNTRIES:
    Y = np.array([item[1] for item in plot_data[country]])
    X = np.array(range(len(Y)))
    fit = curve_fit(logistic_function, X, Y)
    a, b, c = fit[0]
    # We want to find x such that f = c
    day = int(fsolve(lambda x: logistic_function(x, a, b, c) - int(c), b))
    # Day with peak infections
    print(int(b))
    # End day
    print(day)
    # Infection count at End day
    print(c)
    plt.plot(X, Y, label='Actual - ' + country, linewidth=4)
    plt.plot(range(int(day)), logistic_function(range(int(day)), *fit[0]), label='Logistic Model - ' + country)
plt.xlabel('DAY')
plt.ylabel('NO_OF_CASES')
plt.legend()
plt.show()
