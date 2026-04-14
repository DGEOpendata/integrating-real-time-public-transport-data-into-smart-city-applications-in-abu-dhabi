python
import requests
import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# Sample API URL for real-time transport data
API_URL = "https://api.abudhabi.transport/realtime"

@app.route('/get_transport_data', methods=['GET'])
def get_transport_data():
    response = requests.get(API_URL)

    if response.status_code == 200:
        data = response.json()

        # Convert JSON to pandas DataFrame for processing
        df = pd.DataFrame(data['routes'])

        # Perform some data processing (e.g., filtering by route type)
        bus_routes = df[df['type'] == 'bus']

        # Convert back to JSON for API response
        result = bus_routes.to_dict(orient='records')
        return jsonify(result)
    else:
        return jsonify({"error": "Failed to fetch data"}), 500

if __name__ == '__main__':
    app.run(debug=True)
