import os
import datetime

from weatherrequest import weather_request

def csv_writer(filename:str, latitude:float, longitude:float, startdate:str, enddate:str):
    """This function uses weather_request function to request temperature info for a specific
    coordinate and time duration. The requested dataframe is then saved as a .csv file in another
    directory named "files" that is inside same parent directory.

    Args:
        filename (str): Desired filename of csv export of the weather history
        latitude (float): Latitude of the coordinate
        longitude (float): Longitude of the coordinate
        startdate (str): Start date of the request/history 
        enddate (str): End date of the request/history
    """
    weather_history = weather_request(latitude=latitude, longitude=longitude,
                                      startdate=startdate, enddate=enddate)
    files_path = os.path.join(os.path.dirname(__file__), '..', "files")
    csv_path = os.path.join(files_path,filename)

    if os.path.isfile(csv_path):
        curr_time = datetime.datetime.utcnow().replace(microsecond=0).strftime("%Y%m%d%H%M%S")
        weather_history.to_csv(os.path.join(files_path,(curr_time+filename)), index=False)
        print("File is generated with a timestamp in the name")
    else:
        weather_history.to_csv(os.path.join(files_path,filename), index = False)
        print("File is generated")
