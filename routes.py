from flask import Blueprint, jsonify
import requests

main = Blueprint("main", __name__)
@main.route("/")
def home():
    return "Hello World from Flask!"

@main.route("/dexscreener-price/<path:pair>")
def dexscreener_price(pair):
    url = f"https://api.dexscreener.com/latest/dex/pairs/{pair}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Impossible de récupérer les données", "details": str(e)}), 500





