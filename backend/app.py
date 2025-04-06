from flask import Flask, request, jsonify
import sys
import os

# Make sure the model folder is on the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.bot_engine import search_query
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/query', methods=['POST'])
def handle_query():
    try:
        data = request.get_json(force=True)
        query = data.get("query", "").strip()

        if not query:
            return jsonify({"error": "No query provided"}), 400

        results = search_query(query)

        # Debug output
        print("RESULTS:", results)

        if not results:
            return jsonify([])

        if isinstance(results, list):
            return jsonify(results)

        return jsonify([results])  # Return as list for consistency

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": "An error occurred.", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
