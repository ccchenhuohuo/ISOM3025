import requests
from time import sleep
for i in range(10):
    res = requests.get('http://127.0.0.1:5000/submit')
    print(res.content.decode('utf-8'))
    sleep(1)