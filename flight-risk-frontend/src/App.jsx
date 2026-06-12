import { useState } from "react";

function App() {
  const [flightNumber, setFlightNumber] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [flightDate, setFlightDate] = useState("");

  const handleAnalyze = async () => {

    setLoading(true);

    try {

      const response = await fetch(
        "http://127.0.0.1:8000/predict",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            flight_number: flightNumber,
            flight_date: flightDate,
          }),
        }
      );

      const data = await response.json();

      setResult(data);

    } catch (error) {

      console.error(error);

    } finally {

      setLoading(false);

    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-blue-950 text-white">
      <div className="max-w-6xl mx-auto px-6 py-16">

        {/* Header */}
        <div className="text-center">
          <h1
            className="
              text-5xl 
              md:text-7xl
              font-extrabold
              mb-4
              bg-gradient-to-r
              from-blue-400
              to-cyan-300
              bg-clip-text
              text-transparent
            "
          >
            ✈️ Flight Risk Predictor
          </h1>

          <div className="mt-6">
            <span
              className="
      bg-blue-500/20
      text-blue-300
      px-5
      py-2
      rounded-full
      border
      border-blue-500/30
      text-sm
      font-medium
    "
            >
              Real-Time Risk Analysis • Weather • Delay Prediction
            </span>
          </div>
        </div>

        {/* Search */}
        <div className="mt-12 max-w-xl mx-auto">
          <input
            type="text"
            placeholder="Enter Flight Number"
            value={flightNumber}
            onChange={(e) => setFlightNumber(e.target.value)}
            className="
              w-full
              px-5
              py-4
              rounded-xl
              bg-white/10
              backdrop-blur-lg
              border
              border-white/20
              text-white
              outline-none
              focus:border-blue-500
              transition-all
              duration-300
              focus:shadow-lg
              focus:shadow-blue-500/20
            "
          />

          <input
            type="date"
            value={flightDate}
            onChange={(e) => setFlightDate(e.target.value)}
            className="
    mt-4
    w-full
    px-5
    py-4
    rounded-xl
    bg-white/10
    backdrop-blur-lg
    border
    border-white/20
    text-white
    outline-none
  "
          />

          <button
            onClick={handleAnalyze}
            className="
  mt-4
  w-full
  py-4
  rounded-xl
  bg-gradient-to-r
  from-blue-600
  to-cyan-500
  text-white
  font-semibold
  transition-all
  duration-300
  hover:scale-[1.02]
  hover:shadow-xl
  hover:shadow-blue-500/30
  active:scale-95
"
          >
            {loading ? "Analyzing..." : " Analyze Flight"}
          </button>
        </div>

        {/* Dashboard */}
        {result && (
          <div className="mt-12">

            <div className="bg-white/10 backdrop-blur-lg border border-white/10 rounded-3xl p-8 shadow-xl">


              <div className="mb-8 bg-gradient-to-r from-blue-900/40 to-cyan-900/40 border border-blue-500/20 rounded-3xl p-8 ">

                <h2 className="text-3xl font-bold mb-6">
                  Executive Summary
                </h2>

                <div className="grid md:grid-cols-4 gap-6">

                  <div>
                    <p className="text-slate-400">
                      Flight
                    </p>

                    <p className="text-xl font-bold mt-2">
                      {result.flight}
                    </p>
                  </div>

                  <div>
                    <p className="text-slate-400">
                      Route
                    </p>

                    <p className="text-xl font-bold mt-2">
                      {result.origin} → {result.destination}
                    </p>
                  </div>

                  <div>
                    <p className="text-slate-400">
                      Status
                    </p>

                    <p className="text-xl font-bold mt-2 text-green-400">
                      {result.flightStatus?.toUpperCase()}
                    </p>
                  </div>

                  <div>
                    <p className="text-slate-400">
                      Risk
                    </p>

                    <p
                      className={`text-xl font-bold mt-2 ${result.riskLevel === "LOW"
                        ? "text-green-400"
                        : result.riskLevel === "MODERATE"
                          ? "text-yellow-400"
                          : "text-red-400"
                        }`}
                    >
                      {result.riskLevel}
                    </p>
                  </div>

                </div>

              </div>

              {/*flight inf */}

              <h2 className="text-2xl font-bold mb-4">
                ✈️ Flight Details
              </h2>

              <div className="mt-4">
                <p className="text-slate-400">
                  Flight Number
                </p>

                <p className="text-xl font-semibold">
                  {result.flight}
                </p>

                <p className="text-slate-400 mt-4">
                  Airline
                </p>

                <p className="text-xl font-semibold">
                  {result.airline}
                </p>
              </div>

              {/* Route */}
              <div className="bg-slate-800 rounded-3xl p-8 mt-6 transition-all duration-300 hover:-translate-y-2 hover:shadow-2xl hover:shadow-blue-500/20">

                <h3 className="text-2xl font-bold mb-6">
                  Flight Route
                </h3>

                <div className="flex items-center justify-between">

                  <div className="text-center">
                    <p className="text-slate-400 text-sm">
                      Origin
                    </p>

                    <h2 className="text-4xl font-bold">
                      {result.origin}
                    </h2>

                    <p className="text-cyan-400 mt-1">
                      {result.originAirport}
                    </p>
                  </div>

                  <div className="flex-1 px-8">

                    <div className="relative">

                      <div className="h-1 bg-slate-600 rounded-full"></div>

                      <div className="absolute left-0 top-1/2 -translate-y-1/2 w-4 h-4 bg-cyan-400 rounded-full"></div>

                      <div className="absolute right-0 top-1/2 -translate-y-1/2 w-4 h-4 bg-cyan-400 rounded-full"></div>

                      <div className="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 text-3xl">
                        ✈️
                      </div>

                    </div>

                  </div>

                  <div className="text-center">
                    <p className="text-slate-400 text-sm">
                      Destination
                    </p>

                    <h2 className="text-4xl font-bold">
                      {result.destination}
                    </h2>

                    <p className="text-cyan-400 mt-1">
                      {result.destinationAirport}
                    </p>
                  </div>

                </div>

              </div>

              {/* Risk Cards */}
              <div className="grid md:grid-cols-2 gap-4 mt-6">

                <div className="bg-slate-800 rounded-2xl p-6 transition-all duration-300 hover:-translate-y-2 hover:shadow-2xl hover:shadow-blue-500/20">

                  <p className="text-slate-400">
                    Cancellation Probability
                  </p>

                  <h3 className="text-4xl font-bold mt-2 text-white">
                    {result.riskScore?.toFixed(2)}%
                  </h3>

                  <div className="w-full bg-slate-700 h-3 rounded-full mt-4">
                    <div
                      className={`h-3 rounded-full ${result.riskLevel === "LOW"
                        ? "bg-green-400"
                        : result.riskLevel === "MODERATE"
                          ? "bg-yellow-400"
                          : "bg-red-400"
                        }`}
                      style={{
                        width: `${result.riskScore}%`,
                      }}
                    />
                  </div>

                </div>

                <div className="bg-slate-800 rounded-2xl p-6 transition-all duration-300 hover:-translate-y-2 hover:shadow-2xl hover:shadow-blue-500/20">

                  <p className="text-slate-400">
                    Risk Level
                  </p>

                  <div className="mt-4">
                    <span
                      className={`px-4 py-2 rounded-full font-bold text-lg ${result.riskLevel === "LOW"
                        ? "bg-green-500/20 text-green-400"
                        : result.riskLevel === "MODERATE"
                          ? "bg-yellow-500/20 text-yellow-400"
                          : "bg-red-500/20 text-red-400"
                        }`}
                    >
                      {result.riskLevel}
                    </span>
                  </div>

                </div>

              </div>

              {/*status */}

              <div className="mt-8 bg-slate-800 rounded-2xl p-6 transition-all duration-300 hover:-translate-y-2 hover:shadow-2xl hover:shadow-blue-500/20">

                <h3 className="text-xl font-bold mb-4">
                  Flight Status
                </h3>

                <div className="flex justify-between items-center">

                  <div>
                    <p className="text-slate-400">
                      Current Status
                    </p>

                    <p
                      className={`text-xl font-bold ${result.flightStatus === "Arrived"
      ? "bg-green-500/20 text-green-400"
      : result.flightStatus === "Departed"
      ? "bg-yellow-500/20 text-yellow-400"
      : result.flightStatus === "Delayed"
      ? "bg-red-500/20 text-red-400"
      : "bg-cyan-500/20 text-cyan-400"
                        }`}
                    >
                      {result.flightStatus?.toUpperCase()}
                    </p>
                  </div>

                  <div className="text-4xl">
                    ✈️
                  </div>

                </div>

              </div>

              <div className="mt-8 bg-slate-800 rounded-2xl p-6 transition-all duration-300 hover:-translate-y-2 hover:shadow-2xl hover:shadow-blue-500/20">

                <h3 className="text-xl font-bold mb-6">
                  📍 Airport Information
                </h3>

                <div className="grid md:grid-cols-2 gap-6">

                  <div>
                    <p className="text-slate-400 mb-2">
                      Origin Airport
                    </p>

                    <p className="font-semibold text-lg">
                      {result.originAirport}
                    </p>

                    <p className="text-blue-400 mt-2">
                      {result.origin}
                    </p>
                  </div>

                  <div>
                    <p className="text-slate-400 mb-2">
                      Destination Airport
                    </p>

                    <p className="font-semibold text-lg">
                      {result.destinationAirport}
                    </p>

                    <p className="text-cyan-400 mt-2">
                      {result.destination}
                    </p>
                  </div>

                </div>

                <div className="mt-6 pt-6 border-t border-slate-700">

                  <p className="text-slate-400">
                    Travel Date
                  </p>

                  <p className="font-semibold text-lg mt-2">
                    {result.travelDate}
                  </p>

                  <p className="text-slate-400 mt-4">
                    Scheduled Departure
                  </p>


                  <p className="font-semibold text-lg mt-2">
                    {result.departureTime}
                  </p>

                </div>

              </div>

              {/* Weather + Delay + Cancellation */}
              <div className="grid md:grid-cols-3 gap-6 mt-8 ">

                {/* Weather */}
                <div className="bg-slate-800 rounded-3xl p-8 h-full">

  <h3 className="text-2xl font-bold mb-6">
     Travel Day Weather
  </h3>

  <p className="text-slate-400 mb-2">
    Condition
  </p>

  <h2 className="text-4xl font-bold text-cyan-400 mb-6 capitalize">
    {result.weather?.condition}
  </h2>

  <div className="grid grid-cols-2 gap-4">

    <div className="bg-slate-700/40 rounded-xl p-4">
      <p className="text-slate-400 text-sm">
        🌡 Temperature
      </p>

      <p className="text-2xl font-bold mt-2">
        {result.weather?.temperature}°C
      </p>
    </div>

    <div className="bg-slate-700/40 rounded-xl p-4">
      <p className="text-slate-400 text-sm">
        👁 Visibility
      </p>

      <p className="text-2xl font-bold mt-2">
        {result.weather?.visibility} km
      </p>
    </div>

    <div className="bg-slate-700/40 rounded-xl p-4">
      <p className="text-slate-400 text-sm">
        💧 Humidity
      </p>

      <p className="text-2xl font-bold mt-2">
        {result.weather?.humidity}%
      </p>
    </div>

    <div className="bg-slate-700/40 rounded-xl p-4">
      <p className="text-slate-400 text-sm">
        🌬 Wind
      </p>

      <p className="text-2xl font-bold mt-2">
        {result.weather?.wind_speed}
      </p>
    </div>

  </div>

</div>

                {/* Delay */}
                <div className="bg-slate-800 rounded-3xl p-8 h-full">

  <h3 className="text-2xl font-bold mb-6">
     Delay Performance
  </h3>

  <p className="text-slate-400 mb-2">
    On-Time Performance
  </p>

  <h2 className="text-4xl font-bold text-cyan-400 mb-6">
    {result.delay?.onTime}%
  </h2>

  <div className="grid grid-cols-2 gap-4">

    <div className="bg-slate-700/40 rounded-xl p-4">
      <p className="text-slate-400 text-sm">
        ✈ Delayed Flights
      </p>

      <p className="text-2xl font-bold mt-2">
        {result.delay?.delayedFlights}
      </p>
    </div>

    <div className="bg-slate-700/40 rounded-xl p-4">
      <p className="text-slate-400 text-sm">
        📊 Departures
      </p>

      <p className="text-2xl font-bold mt-2">
        {result.delay?.departures}
      </p>
    </div>

  </div>

</div>

                {/* Cancellation */}
                <div className="bg-slate-800 rounded-3xl p-8">
                  <h3 className="text-2xl font-bold mb-6">
                    Cancellation History
                  </h3>

                  <div className="mb-6">
                    <p className="text-slate-400 text-sm">
                      Cancellation Rate
                    </p>

                    <p className="text-4xl font-bold text-red-400">
                      {result.history?.cancelRate}%
                    </p>
                  </div>

                  <div className="grid grid-cols-2 gap-4">

                    <div className="bg-slate-700/40 rounded-xl p-3">
                      <p className="text-slate-400 text-sm">
                        🔧 Technical
                      </p>
                      <p className="font-bold text-lg">
                        {result.history?.technical}
                      </p>
                    </div>

                    <div className="bg-slate-700/40 rounded-xl p-3">
                      <p className="text-slate-400 text-sm">
                        🌦 Weather
                      </p>
                      <p className="font-bold text-lg">
                        {result.history?.weather}
                      </p>
                    </div>

                    <div className="bg-slate-700/40 rounded-xl p-3">
                      <p className="text-slate-400 text-sm">
                        ⚙ Operational
                      </p>
                      <p className="font-bold text-lg">
                        {result.history?.operational}
                      </p>
                    </div>

                    <div className="bg-slate-700/40 rounded-xl p-3">
                      <p className="text-slate-400 text-sm">
                        🏢 Commercial
                      </p>
                      <p className="font-bold text-lg">
                        {result.history?.commercial}
                      </p>
                    </div>

                  </div>
                </div>
              </div>

              {/* AI Analysis */}
<div className="mt-8 bg-slate-800 rounded-2xl p-6 transition-all duration-300 hover:-translate-y-2 hover:shadow-2xl hover:shadow-blue-500/20">

  <h3 className="text-xl font-bold mb-4">
    🤖 AI Analysis
  </h3>

  <div className="text-slate-300 leading-relaxed whitespace-pre-line">
    {result.analysis}
  </div>

</div>
              {/*risk breakdown */}

              <div
                className="mt-8 bg-slate-800 rounded-2xl p-6 transition-all duration-300 hover:-translate-y-2 hover:shadow-2xl hover:shadow-blue-500/20"
              >
                <h3 className="text-2xl font-bold mb-5">
                  📊 Risk Breakdown
                </h3>

                <div className="space-y-3">

                  <div className="mb-4">
                    <div className="flex justify-between mb-2">
                      <span>ML Score</span>
                      <span>{result.riskBreakdown?.ml_score}</span>
                    </div>

                    <div className="w-full bg-slate-700 rounded-full h-2">
                      <div
                        className="bg-blue-400 h-2 rounded-full"
                        style={{
                          width: `${result.riskBreakdown?.ml_score}%`
                        }}
                      />
                    </div>
                  </div>

                  <div className="mb-4">
                    <div className="flex justify-between mb-2">
                      <span>Delay Risk</span>
                      <span>{result.riskBreakdown?.delay_score}</span>
                    </div>

                    <div className="w-full bg-slate-700 rounded-full h-2">
                      <div
                        className="bg-yellow-400 h-2 rounded-full"
                        style={{
                          width: `${result.riskBreakdown?.delay_score}%`
                        }}
                      />
                    </div>
                  </div>

                  <div className="mb-4">
                    <div className="flex justify-between mb-2">
                      <span>Cancellation Risk</span>
                      <span>{result.riskBreakdown?.history_score}</span>
                    </div>

                    <div className="w-full bg-slate-700 rounded-full h-2">
                      <div
                        className="bg-red-400 h-2 rounded-full"
                        style={{
                          width: `${result.riskBreakdown?.history_score}%`
                        }}
                      />
                    </div>
                  </div>

                  <div className="mb-4">
                    <div className="flex justify-between mb-2">
                      <span>Weather Risk</span>
                      <span>{result.riskBreakdown?.weather_score}</span>
                    </div>

                    <div className="w-full bg-slate-700 rounded-full h-2">
                      <div
                        className="bg-cyan-400 h-2 rounded-full"
                        style={{
                          width: `${result.riskBreakdown?.weather_score}%`
                        }}
                      />
                    </div>
                  </div>

                  <hr className="border-slate-700" />

                  <div className="mt-6 p-4 rounded-xl bg-slate-900 border border-slate-700">

                    <div className="flex justify-between items-center">

                      <span className="text-lg font-semibold">
                        CANCELLATION PROBABILTY
                      </span>

                      <span className="text-3xl font-bold text-yellow-400">
                        {result.riskBreakdown?.final_risk}
                      </span>

                    </div>

                  </div>

                </div>
              </div>



            </div>

          </div>
        )}

      </div>
    </div>
  );
}

export default App;