import requests

URL = "https://maps.googleapis.com/maps/api/geocode/json?latlng=40.714224,-73.961452&key=AIzaSyATuLUXcxktLQI9H-WS54eTh-mhlX_X7Bw "

location = input("장소 검색: ")

PARAMS = {'address':location}
r = requests.get(url = URL, params = PARAMS)
data = r.json()

latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lng']
formatted_address = data['results'][0]['formatted_address']

print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
      %(latitude, longitude,formatted_address))
