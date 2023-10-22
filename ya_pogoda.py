import requests
import json
from key import ya_pogoda_key

def pogoda_na_segodnya():
	headers = {'X-Yandex-API-Key' :  ya_pogoda_key}
	params = {
	'lat' : 60.081511, #широта
	'lon' : 30.345477, #долгота
	'lang' : 'ru_RU' } #язык вывода
	url = 'https://api.weather.yandex.ru/v2/informers/'
	request = requests.get(url, headers=headers, params=params)
	res = request.json()
	text = f" Сейчас: Температура: {res['fact']['temp']} градус (ощущается как {res['fact']['feels_like']} градуса), погода - {res['fact']['condition']}, ветер - {res['fact']['wind_speed']} м/c (порывы {res['fact']['wind_gust']} м/c), влажность - {res['fact']['humidity']}% \n \n {res['forecast']['parts'][0]['part_name']}: Температура: {res['forecast']['parts'][0]['temp_avg']} градуса, погода - {res['forecast']['parts'][0]['condition']}, ветер: {res['forecast']['parts'][0]['wind_speed']}м/c (с порывами до {res['forecast']['parts'][0]['wind_gust']}м/c), влажность: {res['forecast']['parts'][0]['humidity']}%, вероятность дождя: {res['forecast']['parts'][0]['prec_prob']}%, продолжительность дождя в мин - {res['forecast']['parts'][0]['prec_period']} \n \n  {res['forecast']['parts'][1]['part_name']}: Температура: {res['forecast']['parts'][1]['temp_avg']} градуса, погода - {res['forecast']['parts'][1]['condition']}, ветер: {res['forecast']['parts'][1]['wind_speed']}м/c (с порывами до {res['forecast']['parts'][1]['wind_gust']}м/c), влажность: {res['forecast']['parts'][1]['humidity']}%, вероятность дождя: {res['forecast']['parts'][1]['prec_prob']}%, продолжительность дождя в мин - {res['forecast']['parts'][1]['prec_period']}"
	return text

