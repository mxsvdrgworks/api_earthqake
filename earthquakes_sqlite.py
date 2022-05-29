import requests
import sqlite3

def save_earthquakes(place_magnitude_list):
    conn=sqlite3.connect("earthquakes_db.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE earthquakes (place TEXT,magnitude REAL);")
    cursor.executemany("INSERT INTO earthquakes VALUES (?,?);",place_magnitude_list)
    conn.commit()
    conn.close()

def select_all_earthquakes():
    conn=sqlite3.connect("earthquakes_db.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM earthquakes;")
    data=cursor.fetchall()
    [print(row) for row in data]
    conn.commit()
    conn.close()

url='https://earthquake.usgs.gov/fdsnws/event/1/query?'

#user input
start_time = input('Enter a start date in format YYYY-MM-DD')
end_time=input('Enter an end date in format YYYY-MM-DD')
latitude=input('Enter latitude')
longtitude=input('Enter longtitude')
max_radius_km=input('Enter max radius in km')
min_magnitude=input('Enter magnitude in BALS')

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
place_magnitude_list=[]
count=0
for earthquake in earthquake_list:
    count+=1
    place_magnitude_list.append((earthquake['properties']['place'],earthquake['properties']['mag']))

save_earthquakes(place_magnitude_list)
select_all_earthquakes()
