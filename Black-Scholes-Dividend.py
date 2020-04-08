import numpy as np
import scipy.stats as si
import sympy as sy
import matplotlib as mpl
from sympy.stats import Normal, cdf
from sympy import init_printing
from matplotlib import pyplot as plt
init_printing()

def euro_vanilla_dividend(S, K, T, r, q, sigma, option = 'call'):
    
    #S: spot price
    #K: strike price
    #T: time to maturity
    #r: interest rate
    #q: rate of continuous dividend paying asset (set to zero for no dividend)
    #sigma: volatility of underlying asset
    
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - q - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    if option == 'call':
        result = (S * np.exp(-q * T) * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    if option == 'put':
        result = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * np.exp(-q * T) * si.norm.cdf(-d1, 0.0, 1.0))
        
    return result

# ABOVE HAS BEEN PULLED FROM https://aaronschlegel.me/black-scholes-formula-python.html [NOT MY WORK]

#Input variables for Black-Scholes model
F = float(input("Stock Option Fee: "))
S = float(input("Spot Price: "))
K = float(input("Strike Price: "))
T = float(input("Time to Maturity: "))
r = float(input("Interest Rate: "))
q = float(input("Rate of Continuous Dividend Paying Asset: "))
sigma = float(input("Implied Voltality (sigma): "))
option_type = input("Enter either call or put: ")

#Assign method to variable and print valuation of option
d3 = euro_vanilla_dividend(S, K, T, r, q, sigma, option = option_type)
print(d3)

#Define variables for Profitability Graph
Z = 70 # Random number to extrapolate data on graph - can be adjusted to suite preference
M = 1 # Slope of the line before lower limit (i.e., the fee is the lower limit)
X = K + F + Z
Y = M*X - (K + F)

#Define x-axis is equal to spot price (i.e., this is one point on the chart)
xscat = S

#Below defines y-axis based on either call or put option (i.e., this is one point on the chart)
def pp2(S, K, F, option = 'call'):
    if option =='call' and ((S - K) - F) >= -F: #200 - 150 - 55  >= -55
        return ((S - K) - F)
    if option == 'put' and ((K - S) - F) >= -F:
        return K - S - F
    else:
        return - F
    
yscat = pp2(S, K, F, option = option_type)

#Define y-axis for plot (this is for the curve - note x-axis is given insite the plt.plot below)
def pp4(K, F, X, Y, option = 'call'):
    if option =='call':
         yplot = [-F,-F, 0, Y]
    if option =='put':
        yplot = [K - F, -F, -F, -F]

    return yplot

yplot = pp4(K, F, X, Y, option = option_type)

#Producing the profitability chart for the option
plt.scatter([xscat], [yscat], c='r', label='Spot Price')
plt.plot([0, K, K + F, X], yplot, label = 'Profitability Line')
plt.title("Option Profitability (per single option)")
plt.xlabel("Stock Price ($)")
plt.ylabel("Profit Earned ($)")
plt.savefig('Vanilla_Dividend_Profitability.png')
#plt.show()
plt.clf() #clear graph

#Producing the valuation chart (i.e., compared to stock price) for the option; x-axis is valuation, y-axis is stock price

#Defining found_fit with black-scholes function
def found_fit(x):
    return euro_vanilla_dividend(x, K, T, r, q, sigma, option = option_type)

x_func = np.linspace(1, S + 100, 1000)
y_func = found_fit(x_func)

plt.scatter([S], [d3], c='r', label='Option Value')
plt.plot(x_func, y_func, label='Option Valuation Line')
plt.title("Option Valuation (per single option)")
plt.xlabel("Stock Price ($)")
plt.ylabel("Option Valuation ($)")
plt.savefig('Vanilla_Dividend_Valuation.png')
#plt.show()
plt.clf() #clear graph

