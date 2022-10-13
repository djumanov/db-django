
from tinydb import TinyDB
import requests

url = 'http://127.0.0.1:8000/add/'

db     = TinyDB('db.json')
tables = db.tables()

for table_name in tables:
    table = db.table(name=table_name)
    products = table.all()
    for product in products:
        payload = {}
        for key, value in product.items():
            if key == "RAM":
                payload['ram'] = value
            else:
                payload[key] = value

        
        r = requests.post(url, data=payload)
        print(r.status_code)