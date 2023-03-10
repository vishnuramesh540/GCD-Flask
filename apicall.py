import requests

currency_api = 'https://api.currencyfreaks.com/latest?apikey=b8423ff89d8e48ac905232ad616f79cc'
currency_api_data = requests.get(url=currency_api)
curr_con = currency_api_data.json()
curr_rates = curr_con['rates']
inr_rate = curr_rates['INR']
inr_rate = float(inr_rate)
