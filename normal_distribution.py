import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, fsolve
from math import sqrt


def normal_distribution(x, mu, sigma, k):
    return k * np.exp(-1/2 * ((x - mu)/sigma) ** 2)


with open('new_cases.json', 'r+') as f:
    new_cases = json.load(f)

COUNTRIES = ['South Korea']

for country in COUNTRIES:
    Y = np.array([item[2] for item in new_cases[country]])
    X = np.array(range(len(Y)))
    fit = curve_fit(normal_distribution, X, Y)
    mu, sigma, k = fit[0]
    print(mu, sigma, k)
    day = int(fsolve(lambda x: normal_distribution(x, mu, sigma, k) - int(k), mu))
    print(day)
    plt.plot(X, Y, label='Actual - '+country)
    plt.plot(X, normal_distribution(X, mu, sigma, k), label='Normal Distribution - '+country)
plt.xlabel('DAY')
plt.ylabel('NO_OF_NEW_CASES')
plt.legend()
plt.show()
