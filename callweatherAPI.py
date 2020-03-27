import json, time, requests,datetime
import paho.mqtt.publish as publish
now = datetime.datetime.now()

def callData(lat,lon):
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=%.2f&lon=%.2f&appid=14cfbf5f05c879dc3478b63cf49327ae&units=metric'%(lat,lon))
	data = r.json()
	temp=data["main"]["temp"]
	humid=data["main"]["humidity"]
	R=3.968-(0.0383*temp)-(0.0224*humid)
	R="%.3f"%R
	return R

def checkDIY():
	while True:
		#urls = 'http://api.openweathermap.org/data/2.5/weather?lat=-7.772794&lon=110.379784&appid=14cfbf5f05c879dc3478b63cf49327ae&units=metric'
		n=0
		array={}
		final=[]
		#geoCoordinatGenerator
		#for y in range(11):
		for y in range(4):
			lat = -(y/100)-7.74
			#for x in range(12):
			for x in range(4):
				lon = (x/100)+110.32
				n=n+1
				try:
					print(('http://api.openweathermap.org/data/2.5/weather?lat=%.2f&lon=%.2f&appid=14cfbf5f05c879dc3478b63cf49327ae&units=metric'%(lat,lon)))
					R = callData(lat,lon)
					final.append('{"%s":%s}'%(n,R))
					print("n-",n)
					print(R)
					#time.sleep(0.30)
					print("\n")
					#publish.single("heatMapDIY", payload="", hostname="localhost", port=1883, qos=2, retain=True)
				except KeyboardInterrupt:
					print("quitting by request")
					quit()
				except :
					print("retrying get data")
					R = callData(lat,lon)
					final.append('{"%s":%s}'%(n,R))
					print("n-",n)
					print(R)
					#time.sleep(0.30)
					print("\n")
					pass
		#print(array)
		print("\n\n\n")
		payload = str(final).replace("'","")
		print(payload)

		publish.single("heatMapDIY", payload=payload, hostname="localhost", port=1883, qos=2, retain=True)


def checkJAV():
	#while True:
	#urls = 'http://api.openweathermap.org/data/2.5/weather?lat=-7.772794&lon=110.379784&appid=14cfbf5f05c879dc3478b63cf49327ae&units=metric'
	n=0
	array={}
	final=[]
	#geoCoordinatGenerator
	for y in range(16):
	#for y in range(4):
		lat = -(y/5)-5.76
		for x in range(48):
		#for x in range(4):
			lon = (x/5)+105.07
			n=n+1
			#print("%.2f %.2f"%(lat,lon)," ",n)
			
			try:
				R = callData(lat,lon)
				final.append('{"%s":%s}'%(n,R))
				print(R,"%.2f,%.2f"%(lat,lon),"   ",n)
				
				
				#publish.single("heatMapDIY", payload="", hostname="localhost", port=1883, qos=2, retain=True)
			except KeyboardInterrupt:
				print("quitting by request")
				quit()
			except :
				print("retrying get data")
				R = callData(lat,lon)
				final.append('{"%s":%s}'%(n,R))
				print(R,"%.2f,%.2f"%(lat,lon),"   ",n)
				pass
			

		print(array)
		print("\n\n\n")
		payload = str(final).replace("'","")
		print(payload)

		publish.single("heatMapDIY", payload=payload, hostname="localhost", port=1883, qos=2, retain=True)	
		
while True:
	now = datetime.datetime.now()
	print("\n\n\nProgram start at", now.strftime("%Y-%m-%d %H:%M:%S"),"now gathering data..")
	#checkDIY()
	checkJAV()
	now = datetime.datetime.now()
	print("Program end at", now.strftime("%Y-%m-%d %H:%M:%S"))
	#print("Sleeping.....")
	time.sleep(1200)