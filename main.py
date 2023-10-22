from telega import sent_message
from ya_pogoda import pogoda_na_segodnya
import time

if __name__ == '__main__':
	while True:
		time.sleep(59)
		z = time.localtime()
		if z.tm_hour == 7  and z.tm_min == 15: #отправка сообщения о погоде в 7:15
			weather = pogoda_na_segodnya()
			sent_message(weather, 'Olya')
			print(f'{time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime())} - Прогноз погоды отправлен Ольге')
			sent_message(weather, 'Boris')
			print(f'{time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime())} - Прогноз погоды отправлен Борису')

