from flask import Flask, jsonify

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def home():
    return "Welcome to the Sample API!"

# Define a route for the /api/data endpoint
@app.route('/api/data', methods=['GET'])
def get_data():
    # Sample data to return
    data = {
        "id": 1,
        "name": "Sample API",
        "description": "This is a sample API for demonstration purposes."
    }
    return jsonify(data)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
