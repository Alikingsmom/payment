import requests

from main import app


# get conversation rate
@app.get('/api/get-currency')
async def currency_rate():
    # connection to CB api
    cb_api = requests.get('https://cbu.uz/ru/arkhiv-kursov-valyut/json/').json()
    usd_rate = cb_api[0]['Rate']
    eur_rate = cb_api[1]['Rate']
    rub_rate = cb_api[2]['Rate']


    # back up
    return {'status': 1, 'rates': {'USD': usd_rate,
                                   'EUR': eur_rate,
                                   'RUB': rub_rate}}
