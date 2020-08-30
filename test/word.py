import requests
from aip import AipOcr

image = requests.get('https://res.pandateacher.com/python_classic.png').content

APP_ID = '19428563'
API_KEY = 'LDOG9yjT2kuDbOXxaykL46DU'
SECRET_KEY = '36UTwAnwixDHFY6HDzyBf5RX2EvZ0GDd'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
res = client.basicGeneral(image)
if 'words_result' in res.keys():
    for item in res['words_result']:
        print(item['words'])

# else:
#     APP_ID = '11756541'
#     API_KEY = '2YhkLuyQGljPUYnmi1CFgxOP'
#     SECRET_KEY = '4rrHe2BF828bI8bQy6bLlx1MelXqa8Z7'
#     client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
#     res = client.basicGeneral(image)
#     if 'words_result' in res.keys():
#         for item in res['words_result']:
#             print(item['words'])
#     else:
#         print(res)