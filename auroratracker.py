import requests


api = 'http://api.auroras.live/v1/?type=locations'


response = requests.get(api)

data = response.json()
names = []

for key, aurora in data.items():
    if key == 'message':
        continue
    else:
        names.append(aurora['name'])


print('\n'.join(names))




