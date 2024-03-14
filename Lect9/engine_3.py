from orderbook import OrderBook
orderbook = OrderBook()
from flask import Flask
from flask import request, jsonify
import json
import time
import numpy as np
app = Flask(__name__)
@app.route('/submit', methods = ['POST'])
def process_order():
    order = request.get_json(force=True)
    order["submit_timestamp"] = time.time()

    print(order) # for testing purpose
    orderbook.receive_orders(order)
    orderbook.print_orderbook()
    return jsonify({"status": "received"})

def main():
    app.run(debug=True)

	
if __name__ == '__main__':
    main()

    
