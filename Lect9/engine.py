from flask import Flask

app = Flask(__name__)


@app.route('/submit', methods = ['GET'])
def process_order():
    return '<h1>order received</h1>'
def main():
    app.run(debug=True)
if __name__ == '__main__':
    main()


