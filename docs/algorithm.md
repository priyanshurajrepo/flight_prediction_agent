# Algorithm

## Overview

The Flight Risk Predictor estimates the likelihood of flight disruption by combining:

* Flight Information
* Weather Forecast
* Historical Delay Performance
* Historical Cancellation Performance

The system retrieves live flight information and evaluates multiple operational factors before generating a risk score and explanation.

---

## Input Data Sources

### Flight Data

Source: Aerodatabox API

Retrieved information:

* Airline
* Flight Number
* Flight Status
* Origin Airport
* Destination Airport
* Scheduled Departure Time

---

### Weather Data

Source: OpenWeatherMap

Retrieved information:

* Temperature
* Humidity
* Visibility
* Wind Speed
* Weather Condition

If the travel date exceeds the available forecast range, weather data is marked as unavailable.

---

### Delay History

Historical airline performance includes:

* On-Time Performance (%)
* Number of Delayed Flights
* Total Departures

Source: Airline delay dataset

---

### Cancellation History

Historical airline performance includes:

* Cancellation Rate (%)
* Technical Cancellations
* Commercial Cancellations
* Operational Cancellations
* Weather Cancellations
* Miscellaneous Cancellations

Source: DGCA airline statistics dataset

---

## Risk Assessment Logic

The risk engine evaluates three major factors:

### Weather Risk

Weather risk increases when:

* Visibility decreases
* Wind speed increases
* Severe weather conditions exist
* Heavy rainfall or storms are predicted

---

### Delay Risk

Delay risk increases when:

* Airline on-time performance is low
* Historical delayed flights are high

---

### Cancellation Risk

Cancellation risk increases when:

* Historical cancellation rates are high
* Operational disruptions are common
* Weather-related cancellations are frequent

---

## Final Risk Score

Final Risk Score =

Weather Risk +
Delay Risk +
Cancellation Risk

The combined score is normalized to a value between 0 and 100.

---

## Risk Levels

### Low Risk

0 - 25

Minimal likelihood of disruption.

### Moderate Risk

26 - 50

Possible delays or operational disruptions.

### High Risk

51 - 100

Significant likelihood of delays or cancellation.

---

## Explanation Engine

A LangGraph-based explanation module generates a human-readable explanation describing:

* Weather impact
* Delay history impact
* Cancellation history impact
* Overall travel recommendation

---

## Future Improvements

* Machine Learning based delay prediction
* Airline reliability scoring
* Airport congestion analysis
* Route-specific historical performance
* Real-time operational alerts
