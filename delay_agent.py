import pandas as pd

df = pd.read_csv("data/delay.csv")


def get_delay_history(airline):

    airline_data = df[
    df["Airline"]
    .str.replace(" ", "")
    .str.lower()

    ==

    airline
    .replace(" ", "")
    .lower()
]
    

    if len(airline_data) == 0:
        return None

    latest = airline_data.iloc[-1]

    return {

        "on_time":
        float(latest["% On-time Performance"]),

        "delayed_flights":
        int(latest["Number of flights Delayed"]),

        "departures":
        int(latest["Number of Departures"])

    }