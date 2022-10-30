from requesttocsv import csv_writer

# Latitude (lat) and longitude (lot) of Eskisehir
lat = 39.7667
lot = 30.5256

#Start and end dates in YYYY-MM-DD format (ISO 8601)
startdate = "2022-01-01"
enddate = "2022-01-31"
csvname = "weather_jun.csv"

csv_writer(csvname,lat,lot,startdate,enddate)
