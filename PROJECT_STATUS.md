# Flight Risk Predictor

## Frontend

* React + Vite + Tailwind CSS
* Flight Number Input
* Flight Date Input
* Analyze Flight Button
* Executive Summary Card
* Flight Details Card
* Route Card
* Flight Status Card
* Airport Information Card
* Weather Card
* Delay Performance Card
* AI Analysis Card
* Risk Breakdown Card
* Dynamic Risk Badge
* Progress Bars

## Backend

* FastAPI
* LangGraph Workflow

### Agents

* Flight Lookup Agent
* Weather Agent
* Airport Agent
* Delay Agent
* Cancellation History Agent
* Risk Agent
* Explanation Agent

## Data Sources

### APIs

* AviationStack (currently used)
* OpenWeather API

### Datasets

* Delay Dataset
* Cancellation Dataset

## Risk Engine

Inputs:

* Weather
* Delay History
* Cancellation History
* ML Probability

Outputs:

* Risk Score
* Risk Level
* AI Explanation

## Current Status

Completed:

* Dashboard UI
* FastAPI Integration
* LangGraph Integration
* Weather Analysis
* Delay Analysis
* Airport Information
* Flight Status
* Risk Breakdown
* Executive Summary

Current Issue:

* AviationStack free plan does not support flight_date filtering.

Next Improvements:

* Replace AviationStack with AeroDataBox/OpenSky
* Use weather forecast based on selected flight date
* Add airport congestion score
* Improve risk model
* Add dashboard animations
