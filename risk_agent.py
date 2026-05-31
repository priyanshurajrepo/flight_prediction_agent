def calculate_risk(
    probability,
    history,
    delay,
    weather
):

    # Safety checks
    if history is None:
        history = {
            "cancel_rate": 0,
            "technical": 0,
            "commercial": 0,
            "operational": 0,
            "weather": 0,
            "misc": 0
        }

    if delay is None:
        delay = {
            "on_time": 100,
            "delayed_flights": 0,
            "departures": 0
        }

    ml_score = probability

    history_score = min(
        history["cancel_rate"] * 10,
        100
    )

    delay_score = 100 - delay["on_time"]

    weather_score = 0

    if weather["visibility"] < 3:
        weather_score += 40

    elif weather["visibility"] < 5:
        weather_score += 20

    if weather["wind_speed"] > 25:
        weather_score += 30

    if weather["condition"].lower() in [
        "thunderstorm",
        "storm",
        "heavy rain",
        "fog"
    ]:
        weather_score += 40

    final_risk = (
        ml_score * 0.4 +
        history_score * 0.2 +
        delay_score * 0.2 +
        weather_score * 0.2
    )

    return round(
        final_risk,
        2
    )


def get_risk_level(score):

    if score < 25:
        return "LOW"

    elif score < 50:
        return "MODERATE"

    else:
        return "HIGH"