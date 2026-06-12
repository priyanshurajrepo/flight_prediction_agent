# ✈️ Flight Risk Predictor

A LangGraph-based Multi-Agent AI System that analyzes flight risk using real-time weather data, historical airline performance, delay statistics, and LLM-powered explanations.

## 🚀 Overview

Flight delays and cancellations are influenced by multiple factors such as weather conditions, airline operational efficiency, technical issues, and historical performance.

This project combines multiple AI agents to gather information from different sources, calculate a flight risk score, and generate a human-readable explanation for passengers.

The system is built using:

* LangGraph
* Streamlit
* Groq (Llama 3.3 70B)
* AviationStack API
* OpenWeather API
* CSV-based Retrieval (Lightweight RAG)

---

## 🏗 Architecture

```text
User Input Flight Number
            │
            ▼
Flight Lookup Agent
(AviationStack API)
            │
            ▼
Airport Agent
(Airport Coordinates)
            │
            ▼
Weather Agent
(OpenWeather API)
            │
            ▼
Airline History Agent
(Cancellation Dataset)
            │
            ▼
Delay Agent
(Delay Dataset)
            │
            ▼
Risk Agent
(Custom Risk Engine)
            │
            ▼
Explanation Agent
(Groq + Llama 3.3 70B)
            │
            ▼
Streamlit Dashboard
```

---

## 🤖 Multi-Agent Workflow

### 1. Flight Lookup Agent

Retrieves:

* Airline Name
* Origin Airport
* Destination Airport
* Departure Time

using AviationStack API.

---

### 2. Airport Agent

Maps airport codes to:

* Latitude
* Longitude

using airport datasets.

---

### 3. Weather Agent

Fetches:

* Temperature
* Visibility
* Wind Speed
* Humidity
* Weather Condition

using OpenWeather API.

---

### 4. Airline History Agent

Retrieves historical airline cancellation records:

* Cancellation Rate
* Technical Cancellations
* Operational Cancellations
* Weather Cancellations

from CSV datasets.

---

### 5. Delay Agent

Retrieves:

* On-Time Performance
* Delayed Flights
* Total Departures

from historical delay datasets.

---

### 6. Risk Agent

Calculates a final flight risk score using:

* Weather Conditions
* Historical Cancellation Performance
* Historical Delay Performance

and classifies risk as:

* LOW
* MODERATE
* HIGH

---

### 7. Explanation Agent

Uses Groq's Llama 3.3 70B model to generate an easy-to-understand explanation for passengers.

---

## 📊 Features

✅ Real-time flight lookup

✅ Real-time weather analysis

✅ Historical airline cancellation analysis

✅ Historical delay analysis

✅ Custom flight risk scoring

✅ AI-generated explanations

✅ Multi-Agent LangGraph workflow

✅ Interactive Streamlit dashboard

✅ Deployed on Streamlit Cloud

---

## 🗂 Project Structure

```text
flight_prediction_agent/
│
├── data/
│   ├── airports.csv
│   ├── cancellation.csv
│   └── delay.csv
│
├── airline_history_agent.py
├── airport_agent.py
├── delay_agent.py
├── explanation_agent.py
├── flight_lookup_agent.py
├── graph.py
├── risk_agent.py
├── weather_agent.py
├── streamlit_app.py
│
├── requirements.txt
└── README.md
```

---

## 🛠 Tech Stack

### AI & Orchestration

* LangGraph
* LangChain
* Groq
* Llama 3.3 70B

### Backend

* Python

### Frontend

* Streamlit

### APIs

* AviationStack API
* OpenWeather API

### Data Processing

* Pandas

---

## 🔑 Environment Variables

Create a `.env` file:

```env
AVIATIONSTACK_API_KEY=your_key

OPENWEATHER_API_KEY=your_key

GROQ_API_KEY=your_key
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/flight_prediction_agent.git

cd flight_prediction_agent
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run streamlit_app.py
```

---

## 💡 Challenges Solved

### Flight Number Standardization

Users entered flight numbers in different formats:

```text
6E5275
6E 5275
6e5275
```

A normalization layer was implemented to standardize user input before API lookup.

---

**Airline Name Mismatch**

Different data sources represented airlines differently:

```text
SpiceJet
Spice Jet
```

A normalization strategy was implemented to ensure reliable dataset retrieval.

---

 **API Limitations**

Some flights were unavailable through the aviation API.

Robust validation and error handling were added to prevent system crashes.

---

**LLM Consistency**

Initially, the LLM sometimes generated a risk level different from the calculated score.

The Risk Agent was made the source of truth, while the LLM focuses only on explanation generation.

---

**Airport Code to Weather Mapping**

Weather APIs require geographic coordinates, while flight APIs provide airport codes.

Example:

DEL
BLR
IXB

cannot be directly used for weather retrieval.

Solution:
Built an Airport Agent that maps airport codes to latitude and longitude using airport datasets, allowing accurate weather retrieval.

---

**City Name Inconsistency Across Sources**

Different data sources used different naming conventions for locations and airports.

Examples:

Bangalore
Bengaluru

Delhi
New Delhi

This caused lookup failures during integration.

Solution:
Switched from city-name-based retrieval to coordinate-based retrieval using airport codes and latitude/longitude mapping.

---

**Missing Flight Data from Aviation API**

Certain flight numbers were unavailable despite being valid flights.

Examples:

SG478

The API occasionally returned incomplete or missing data because of free-tier limitations and coverage constraints.

Solution:
Added validation and error handling to prevent application crashes and provide meaningful feedback to users.



## 🎯 Future Improvements

* Live flight status tracking
* Airport congestion analysis
* Delay prediction model
* Additional aviation data sources
* Historical trend visualization
* Cloud database integration

---

## 👨‍💻 Author

**Priyanshu Raj**

NIT Durgapur

Passionate about AI, Multi-Agent Systems, Product Development, and Data Analyst

