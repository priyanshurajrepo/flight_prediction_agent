import pandas as pd

df = pd.read_csv("data/cancellation.csv")


def get_cancellation_history(airline):

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

        "cancel_rate":
        float(latest["% Cancellation"]),

        "technical":
        int(latest["Cancellation Due to Technical"]),

        "commercial":
        int(latest["Cancellation Due to Commercial"]),

        "operational":
        int(latest["Cancellation Due to Operational"]),

        "weather":
        int(latest["Cancellation Due to Weather"]),

        "misc":
        int(latest["Cancellation Due to Misc"])

    }