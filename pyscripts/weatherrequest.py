import requests
import pandas as pd

def weather_request(latitude:float, longitude:float, startdate:str, enddate:str):
    """This function gets the weather history from open-meteo api. A temperature
    history can be taken between two dates for a specific coordinate.

    Args:
        latitude (float): Latitude of the desired coordinate 
        longitude (float): Longitude of the desired coordinate

    Returns:
        Pandas DataFrame: n by 2 Pandas df of temperature history. Temperature
        is Celsius and timestamps are in "YYYY-MM-DD-THH-MM" format
    """
    str1 = "https://archive-api.open-meteo.com/v1/era5?latitude="
    lat = str(latitude)
    str2 = "&longitude="
    lot = str(longitude)
    str3 = "&start_date="
    strt_date = startdate
    str4 = "&end_date="
    end_date = enddate
    str5 = "&hourly=temperature_2m"
    request_str = str1+lat+str2+lot+str3+strt_date+str4+end_date+str5
    req = requests.get(request_str, timeout=10)
    hourly_time = req.json()['hourly']['time']
    hourly_temp = req.json()['hourly']['temperature_2m']
    temp_history = pd.DataFrame({"Date":hourly_time, "Temperature":hourly_temp})
    return temp_history
