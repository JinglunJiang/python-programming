import sys
import datetime
import urllib.request


def save_json(lat, lng, days):
    """
    Make a request to open-meteo.com's weather API for the last
    {days} days of weather information at the given location.

    Writes a file named "weather.json" containing the historical weather
    information.

    Parameters:
        lat: float  : latitude of location
        lng: float  : longitude of location
        days: int   : number of days in past to request
    """
    # You will use urllib.request and datetime for this. Take a look
    # at the documentation for both of these modules to figure out
    # how to use them.

    #    https://docs.python.org/3/library/urllib.request.html
    #    https://docs.python.org/3/library/datetime.html

    # 1) Get today's date, which we'll use for end_date
    end_date = datetime.date.today()
    # 2) Calculate start_date (Using datetime.timedelta)
    start_date = end_date - datetime.timedelta(days=days)
    # 3) Open a file named "output.json" in binary-write mode ("wb").
    with open("weather.json", "wb") as past_weather:
    # 4) Make a request using urllib.request
    #     Example URL: https://archive-api.open-meteo.com/v1/era5?latitude=41.85&longitude=-87.65&start_date=2022-01-01&end_date=2022-07-13&daily=temperature_2m_max,temperature_2m_min&timezone=auto" # noqa
    #     You will need to change the latitude, longitude, start_date,
    #     and end_date parameters in the URL, you will not need to
    #     change the others.
        url = "https://archive-api.open-meteo.com/v1/era5?latitude={}&longitude={}&start_date={}&end_date={}&daily=temperature_2m_max,temperature_2m_min&timezone=auto".format(lat, lng, start_date, end_date)
        response = urllib.request.urlopen(url)
    # 5) Save the result of reading the response (i.e.: response.read()) to
    #    "weather.json"
        past_weather.write(response.read())


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: download.py <lat> <lng> <days>")
    else:
        save_json(float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]))
