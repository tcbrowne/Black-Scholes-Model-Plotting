# Black-Scholes-Model-Plotting

Objective: plot the Profitability and Valuation of either call or put option (as per the Black-Scholes model)

Black-Scholes Python calculation from here: https://aaronschlegel.me/black-scholes-formula-python.html

This should assist in providing a visualization of the variable at play in the Black-Scholes model for the European Style option. For instance, you will see how the chart becomes more convex the higher the volatility (i.e., sigma) and the longer time to maturity (i.e., more uncertainty). 

# Instructions
Provide input of variables for the following:

    #S: spot price
    #K: strike price
    #T: time to maturity (set to 1 to equal 255 trading days in year)
    #r: interest rate
    #q: rate of continuous dividend paying asset (set to zero for no dividend)
    #sigma: volatility of underlying asset (zero to one)

# Output

1) Provide valuation of the call / put option
2) Chart the option's profitability (stock price on x-axis, profitability on y-axis)
3) Chart the option's valuation (stock price on x-axis, profitability on y-axis)

# Plotting the Results of Black-Scholes
![Vanilla_Dividend_Profitability](https://user-images.githubusercontent.com/13516076/78972819-a7831180-7adc-11ea-97b9-26c5615db242.png)
![Vanilla_Dividend_Valuation](https://user-images.githubusercontent.com/13516076/78972833-b073e300-7adc-11ea-9ac9-5f9df1dd8e94.png)
