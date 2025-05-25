import requests
from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/dexscreener/<chain>/<pair>')
def dexscreener_price(chain, pair):
    url = f"https://api.dexscreener.com/latest/dex/pairs/{chain}/{pair}"
    response = requests.get(url)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Impossible de récupérer les données"}), 400

