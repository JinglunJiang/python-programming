import json
import statistics
import functools


def summarize_weather(filename="weather.json"):
    """
    Reads weather data from a JSON file and summarizes it.

    Inputs:
        filename (str): Filename for weather data.

    Returns:
        Dictionary with the following keys:
           start_date:      Date of first entry (string)
           end_date:        Date of last entry (string)
           max_high:        Maximum high temperature in the data (float).
           min_low:         Minimum low temperature in the data (float).
           mean_high:    Computed mean of high temperatures (float).
           mean_low:     Computed mean of low temperatures (float).
           std_dev_high:    Computed standard deviation of high temperatures (float).
           std_dev_low:     Computed standard deviation of low temperatures (float).
    """
    # 1) Open weather.json & read data as a string.
    with open(filename, "r") as data_file:
        data = data_file.read()
    # 2) Use json.load to transform data from a string to Python objects.
    data_formatted = json.loads(data)
    # 3) Compute & return statistics as shown in docstring.
    # Relevant modules:
    #   statistics: https://docs.python.org/3/library/statistics.html
    #   json: https://docs.python.org/3/library/json.html

    temperature_high = list(
        temperature for temperature in data_formatted["daily"]["temperature_2m_max"] if temperature)
    temperature_low = list(
        temperature for temperature in data_formatted["daily"]["temperature_2m_min"] if temperature)
    # To filter out the null values

    result = {}
    result["start_date"] = data_formatted["daily"]["time"][0]
    result["end_date"] = data_formatted["daily"]["time"][-1]
    result["max_high"] = float(max(temperature_high))
    result["min_low"] = float(min(temperature_low))
    result["mean_high"] = float(statistics.mean(temperature_high))
    result["mean_low"] = float(statistics.mean(temperature_low))
    result["std_dev_high"] = float(statistics.stdev(temperature_high))
    result["std_dev_low"] = float(statistics.stdev(temperature_low))

    return result


def main():
    """
    Reads in weather data from weather.json and prints out a summary.
    """
    summary = summarize_weather()
    print(
        """       Weather Report
===========================
{start_date}       {end_date}
===========================
High Temperature:   {max_high:>6.1f}
     Average:       {mean_high:>6.1f}
     Std. Dev:      {std_dev_high:>6.1f}
Low Temperature:    {min_low:>6.1f}
     Average:       {mean_low:>6.1f}
     Std. Dev:      {std_dev_low:>6.1f}
          """.format(
            **summary
        )
    )


if __name__ == "__main__":
    main()
