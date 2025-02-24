# app.py
from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)
mergedData = pd.read_csv('../../data/merged_data.csv')


@app.route('/api/data/merged_oil_price_history', methods=['GET'])
def get_merged_oil_price_history():
    return jsonify(mergedData.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
