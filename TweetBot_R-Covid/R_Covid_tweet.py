from dateutil.tz import gettz
import tweepy, requests,time
import datetime as dt
#now = datetime.datetime.now()

consumer_key = 'theKey'
consumer_secret = 'theKey'
access_token = 'theKey'
access_token_secret = 'theKey'

def callData(lat,lon):
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=%.2f&lon=%.2f&appid={KEY}&units=metric'%(lat,lon))
	data = r.json()
	temp=data["main"]["temp"]
	humid=data["main"]["humidity"]
	R=3.968-(0.0383*temp)-(0.0224*humid)
	R="%.3f"%R
	return R

def autentikasi():
	try:
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		return auth
	except Exception as e:
		return None


while True:
	auth = autentikasi()
	api = tweepy.API(auth)

	#kebumen
	lat=-7.66
	lon=109.65
	theR = callData(-7.66,109.65)
	theMessage='[R-Number] Kalkulasi R number Kebumen kota saat ini adalah %s. Selengkapnya tentang Project R-Number :: https://github.com/wimbuhAdi/HeatMapCOVID-19-Effective-Reproductive-Number-DIY'%(theR)
	#dt.datetime.now().isoformat()
	#print('new tweet posted at ', dt.datetime.now(gettz("GMT+8")))


	try:
		dt.datetime.now().isoformat()
		tm = dt.datetime.now(gettz("GMT+7"))
		if tm.hour == 9 or tm.hour == 12 or tm.hour == 15:
			api.update_status(theMessage)
			print('tweeting at', tm)

	except:
		print("same content as prior")
		pass	


	print('next check in 60m')
	time.sleep(3600) #1 jam
	#time.sleep(28800) #8jam
