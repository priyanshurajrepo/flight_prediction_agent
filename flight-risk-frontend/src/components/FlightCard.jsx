function FlightCard({ result }) {
  return (
    <div
      style={{
        marginTop: "30px",
        padding: "25px",
        borderRadius: "15px",
        backgroundColor: "#ffffff",
        boxShadow: "0 4px 12px rgba(0,0,0,0.1)",
      }}
    >
      <h2>✈️ Flight Details</h2>

      <div style={{ marginTop: "15px" }}>
        <p><strong>Flight:</strong> {result.flight}</p>

        <p><strong>Airline:</strong> {result.airline}</p>

        <p><strong>Risk Score:</strong> {result.riskScore}/100</p>

        <p><strong>Risk Level:</strong> {result.riskLevel}</p>
      </div>
    </div>
  );
}

export default FlightCard;