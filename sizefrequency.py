import ccxt
import csv
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

exchange = ccxt.coinbasepro()

symbol = 'ETH/USD'

filename = exchange.id + '_' + symbol.replace('/', '') + '.csv'
csv_f = open(filename, mode="w", newline="")
csv_writer = csv.DictWriter(csv_f, delimiter=",", fieldnames=["timestamp", "size", "price", "side"])
csv_writer.writeheader()

sizes = []

def update_graph(frame):
    try:
        trades = exchange.fetch_trades(symbol, limit=1000)
        
        for trade in trades:
            if float(trade['amount']) > 0.5:
                sizes.append(float(trade['amount']))

            csv_writer.writerow({
                'timestamp': trade['timestamp'],
                'size': "{:.7f}".format(float(trade['amount'])),
                'price': trade['price'],
                'side': trade['side'],
            })

        plt.clf()
        plt.hist(sizes, bins=50, edgecolor='black')
        plt.xlabel('Size')
        plt.ylabel('Frequency')
        plt.title(f'{symbol} Size Distribution')

    except KeyboardInterrupt:
       
        csv_f.close()
        plt.close()

    
    time.sleep(1)


ani = FuncAnimation(plt.gcf(), update_graph, interval=1000, cache_frame_data=False)

plt.show()
