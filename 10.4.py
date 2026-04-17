from flask import Flask
import json

app = Flask(__name__)

airports = {
    "LFLL": {"icao": "LFLL", "name": "Lyon Saint-Exupery Airport", "city": "Lyon", "country": "FR"},
    "EGLL": {"icao": "EGLL", "name": "Heathrow Airport", "city": "London", "country": "GB"},
    "KJFK": {"icao": "KJFK", "name": "John F. Kennedy International Airport", "city": "New York", "country": "US"},
    "WSSS": {"icao": "WSSS", "name": "Singapore Changi Airport", "city": "Singapore", "country": "SG"},
    "VHHH": {"icao": "VHHH", "name": "Hong Kong International Airport", "city": "Hong Kong", "country": "HK"},
}

@app.route("/airport/<icao>", methods=["GET"])
def get_airport(icao):
    icao = icao.upper()
    if icao in airports:
        return json.dumps(airports[icao])
    else:
        return json.dumps({"error": "Airport not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)