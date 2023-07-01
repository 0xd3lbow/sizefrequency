# size frequency
This script will pull recent or current trade data and calculates the frequency distribution of order size. 
It writes the trade data to a CSV file for further analysis and modeling, filtering the size to a certain threshold to cut out some noise and randomness, and finally uses matplotlib to get a live visualization of the distribution. 

The trading pair can be replaced with any ticker and the filter can be adjusted to your preference.

I found that consistently logging trade data and size-frequency can be useful for backtesting, quantifying participant behavior, visualizing clustering effects, spotting exchange inefficiencies that can be exploited, and getting an idea of the market depth (liquidity available at different price levels).
