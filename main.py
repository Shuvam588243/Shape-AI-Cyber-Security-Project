import requests

from datetime import datetime

print("**** Weather App *****")

api_key = '6201d1f3e4aa03cd619c561871d094f2'
location = input("Enter the Name of the City : ")

complete_api_link = 'https://api.openweathermap.org/data/2.5/weather?q='+location+"&appid="+api_key

api_link = requests.get(complete_api_link)
api_data = api_link.json()




temp_city = ((api_data['main']['temp']) -273.15)
weather_details = api_data['weather'][0]['description']
humidity = api_data['main']['humidity']
wind_speed = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("---------------------WEATHER STATS -----------------")

print("{} || {}".format(location.upper(), date_time))

print("-----------------------------------------")

print("Current Temperature : {:.2f} deg C".format(temp_city))

print("Current Weather Description :",weather_details)
print("Current Humidity : ",humidity, '%')
print("Current Wind Speed : ", wind_speed , 'kmph')


temp_cel = "Current Temperature : {:.2f} deg C".format(temp_city)

f = open("Weather.txt", "w")
f.write("\n -------------WEATHER REPORT------------------------ \n")
f.write("\n Weather Stats of "+location+" at "+date_time)
f.write("\n \n "+temp_cel)
f.write("\n Current Humity : "+str(humidity)+"%")
f.write("\n Current Wind Speed : "+str(wind_speed)+"kmph")
f.write("\n \n ---------------------------------------- \n")
f.close()