# size frequency
This script will pull recent or current trade data and calculates the frequency distribution of order size. It writes the trade data to a CSV file for further analysis and modeling, filtering the size to a certain threshold to cut out some noise and randomness, and finally uses matplotlib to get a live visualization of the distribution.

![Figure_1](https://github.com/0xd3lbow/sizefrequency/assets/130616587/4baa7e62-0ca5-48e5-9c1b-b64e6980c054)

The trading pair can be replaced with any ticker and the filter can be adjusted to your preference.

<img width="341" alt="Screenshot 2023-07-01 152719" src="https://github.com/0xd3lbow/sizefrequency/assets/130616587/0821d692-ff47-497e-9717-627c8e451e93">

I found that consistently logging trade data and size-frequency can be useful for backtesting, quantifying participant behavior, visualizing clustering effects, spotting exchange inefficiencies that can be exploited, and getting an idea of the market depth (liquidity available at different price levels).
