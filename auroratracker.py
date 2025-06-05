import requests
import os
from dotenv import load_dotenv


load_dotenv()

api = os.getenv('API')

response = requests.get(api)

data = response.json()
names = []


for key, aurora in data.items():
    if key == 'message':
        continue
    else:
        if aurora['country']:
            names.append(aurora['name'])
    
print('\n'.join(names))







