import requests

url='https://earthquake.usgs.gov/fdsnws/event/1/query?'

#user input
'''
:params:latitude:28.253007,longtitude:83.938548,max_radius_km must be > 0 
'''
start_time = input('Enter a start date in format YYYY-MM-DD')
end_time=input('Enter an end date in format YYYY-MM-DD')
latitude=input('Enter latitude')
longtitude=input('Enter longtitude')
max_radius_km=input('Enter max radius in km')
min_magnitude=input('Enter magnitude in BALLS')
response=requests.get(url,headers={'Accept':'application/json'},params={
    'format':'geojson',
    'starttime': start_time,
    'endtime': end_time,
    'latitude':latitude,
    'longitude':longtitude,
    'maxradiuskm':max_radius_km,
    'minmagnitude':min_magnitude
})
data=response.json()

earthquake_list=data['features']
count=0
for earthquake in earthquake_list:
    count+=1
    print(f"{count}.Place:{earthquake['properties']['place']}.Magnitude:{earthquake['properties']['mag']}")
