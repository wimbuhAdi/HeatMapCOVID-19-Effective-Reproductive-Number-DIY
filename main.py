import json, time, requests
import paho.mqtt.publish as publish

def check():
	try:
		urls = 'http://api.openweathermap.org/data/2.5/weather?lat=-7.772794&lon=110.379784&appid=!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!&units=metric'
		n=0
		array={}
		#geoCoordinatGenerator
		for y in range(11):
		#for y in range(2):
			lat = -(y/100)-7.74
			for x in range(12):
			#for x in range(2):
				lon = (x/100)+110.32
				#print("%.2f, %.2f"%(lat,lon))
				r = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=%.2f&lon=%.2f&appid=!!!!!!!!!!!!!!!!!!!!!!!&units=metric'%(lat,lon))
				data = r.json()
				temp=data["main"]["temp"]
				humid=data["main"]["humidity"]
				R=3.968-(0.0383*temp)-(0.0224*humid)
				print("R=%.3f"%R)
				n=n+1
				array[str(n)]="%.3f"%R
				print("n-",n)
				time.sleep(0.30)
				print("\n")

		print(array)
		final=[]
		#for key, value in array:
		for key in array.keys():
			print(key, '->', array[key])
			final.append('{"%s":%s}'%(key,array[key]))

		print("\n\n\n")
		payload = str(final).replace("'","")
		print(payload)

		publish.single("heatMap", payload=payload, hostname="localhost", port=1883)
	except :
		pass
while True:
	check()
	print("Sleeping.....")
	time.sleep(30)
